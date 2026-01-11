from codeforces.structures.problem import Problem
from codeforces.structures.party import Party
from system.structures.dummyStruct import DummyStruct


class Submission(DummyStruct):
    def __init__(self) -> None:
        super().__init__()
        self.id = int()
        self.contestId = int()
        self.creationTimeSeconds = int()
        self.relativeTimeSeconds = int()
        self.problem = Problem()
        self.author = Party()
        self.programmingLanguage = str()
        self.verdict = str()
        self.testset = str()
        self.passedTestCount = int()
        self.timeConsumedMillis = int()
        self.memoryConsumedBytes = int()
        self.points = int()
