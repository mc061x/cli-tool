from codeforces.structures.contest import Contest
from codeforces.structures.problem import Problem
from codeforces.structures.problemData import ProblemData
from system.structures.typelist import MyList
from system.structures.dummyStruct import DummyStruct

class ContestData(DummyStruct):
    def __init__(self) -> None:
        self.contest_id = str()
        self.problem_list = list()
        self.problem_data = MyList(ProblemData)

        self.current_problem_index = str()