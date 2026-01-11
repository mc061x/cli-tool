from codeforces.API import *
from codeforces.structures.header import *
from codeforces.structures.results.hacksResult import HacksResult
from codeforces.structures.results.ratedListResult import RatedListResult
from codeforces.structures.results.standingsResult import StandingsResult
from codeforces.structures.results.ratingResult import RatingResult
from codeforces.structures.results.userStatusResult import UserStatusResult

class Requester:
    def __init__(self, api: API) -> None:
        self.api = api

    def standings(self, args: dict, authorize=False) -> StandingsResult:
        return StandingsResult(self.api.request(method='contest.standings?', args=args, authorize=authorize))

    def hacks(self, args: dict, authorize=False) -> HacksResult:
        return HacksResult(self.api.request(method='contest.hacks?', args=args, authorize=authorize))

    def rated_list(self, args: dict, authorize=False) -> RatedListResult:
        return RatedListResult(self.api.request(method='contest.ratedList?', args=args, authorize=authorize))

    def rating(self, args: dict, authorize=False) -> RatingResult:
        return RatingResult(self.api.request(method='user.rating?', args=args, authorize=authorize))

    def user_status(self, args: dict, authorize=False) -> UserStatusResult:
        return UserStatusResult(self.api.request(method='user.status?', args=args, authorize=authorize))