from exceptions import *
from codeforces.structures.party import Party
from codeforces.structures.member import Member
from codeforces.structures.ranklistRow import RanklistRow
from system.structures.typelist import MyList

import time, math

class Contestant:
    def __init__(self) -> None:
        self.rating = int()
        self.points = float()
        self.rank = int()
        self.delta = int()
        self.handle = str()
        self.performance = int()

class Predictor:
    def get_elo_win_probability(self, ra: float, rb: float) -> float:
        return 1 / (1 + math.pow(10, (rb - ra) / 400))
    
    def get_party_rating(self, party: Party) -> float:
        if len(party.members.list) == 1:
            only_member: Member = party.members.list[0]
            return self.ratings[only_member.handle]
        
        left, right = 1.0, 1e4
        for _ in range(20):
            mid = (left + right) / 2
            winsProbability = 1
            for member in party.members.list:
                winsProbability *= self.get_elo_win_probability(mid, self.ratings[member.handle])
            rating = math.log10(1 / winsProbability - 1) * 400 + mid

            if rating > mid:
                left = mid
            else:
                right = mid
        return round((right + left) / 2)
    
    def __init__(self, to_predict: list[str]) -> None:
        self.ratings = dict()
        self.contestants = list()
        self.noted_contestants = list()
        self.to_predict = to_predict
    
    def init_process(self, rows: MyList(RanklistRow)):
        row: RanklistRow
        for row in rows.list:
            current_contestant = Contestant()

            noted = False
            for member in row.party.members.list:
                if member.handle in self.to_predict:
                    noted = True
                current_contestant.handle += member.handle + ' '

            current_contestant.points = row.points
            current_contestant.rank = row.rank
            current_contestant.rating = self.get_party_rating(row.party)
            self.contestants.append(current_contestant)
            if noted:
                self.noted_contestants.append(current_contestant)

    def get_seed(self, rating) -> float:
        res = 1.0
        for contestant in self.contestants:
            res += self.get_elo_win_probability(contestant.rating, rating)
        return res
    
    def get_rating_to_rank(self, rank: float) -> float:
        left, right = 1, 8000
        while right - left > 1:
            mid = (left + right) // 2
            if self.get_seed(mid) < rank:
                right = mid
            else:
                left = mid
        return left
    
    def reassignRanks(self):
        self.contestants.sort(key=lambda x: x.points, reverse=True)

        contestant : Contestant
        for contestant in self.contestants:
            contestant.rank = 0
            contestant.delta = 0

        first = 0
        points = self.contestants[0].points

        for i in range(1, len(self.contestants)):
            if self.contestants[i].points < points:
                for j in range(first, i):
                    self.contestants[j].rank = i
                first = i
                points = self.contestants[i].points
        
        rank = len(self.contestants)
        for j in range(first, len(self.contestants)):
            self.contestants[j].rank = rank
    
    def calculate_delta(self, contestant : Contestant) -> float:
        return int((self.get_rating_to_rank(contestant.rank) - contestant.rating) / 2)
    
    def process(self) -> None:
        if len(self.contestants) == 0:
            return
        
        self.reassignRanks()
        for c in self.noted_contestants:
            midRank = math.sqrt(c.rank * self.get_seed(c.rating))
            needRating = self.get_rating_to_rank(midRank)
            delta = (needRating - c.rating) / 2
            c.delta = delta
            c.performance = self.calculate_performance(c)
    
    def calculate_performance(self, contestant : Contestant) -> float:
        low, high = -500, 6000
        while high - low > 1:
            mid = (high + low) // 2

            seed = self.get_seed(mid)
            midRank = math.sqrt(contestant.rank * seed)
            needRating = self.get_rating_to_rank(midRank)
            delta = (needRating - mid) / 2

            if delta <= 0:
                high = mid
            else:
                low = mid
        return low