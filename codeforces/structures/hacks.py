from codeforces.structures.party import Party
from codeforces.structures.problem import Problem
from system.structures.dummyStruct import DummyStruct


class Hack(DummyStruct):
    def __init__(self) -> None:
        super().__init__()
        self.id = int()
        self.creationTimeSeconds = int()
        self.hacker = Party()
        self.defender = Party()
        self.verdict = str()
        self.problem = Problem()
        self.test = str()
        self.judgeProtocol = dict()
