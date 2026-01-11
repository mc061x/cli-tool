from codeforces.structures.contest import Contest
from system.structures.typelist import MyList
from codeforces.structures.problem import Problem
from codeforces.structures.ranklistRow import RanklistRow
from system.structures.dummyStruct import DummyStruct


class StandingsResult(DummyStruct):
    def __init__(self, json: dict) -> None:
        super().__init__()
        self.contest = Contest()
        self.problems = MyList(Problem)
        self.rows = MyList(RanklistRow)

        self.from_json(object=json)
