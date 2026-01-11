from codeforces.structures.party import Party
from system.structures.dummyStruct import DummyStruct
from system.structures.typelist import MyList
from codeforces.structures.problemResult import ProblemResult


class RanklistRow(DummyStruct):
    def __init__(self) -> None:
        super().__init__()
        self.party = Party()
        self.rank = int()
        self.points = float()
        self.penalty = int()
        self.successfulHackCount = int()
        self.unsuccessfulHackCount = int()
        self.problemResults = MyList(ProblemResult)
        self.lastSubmissionTimeSeconds = int()

