from system.structures.dummyStruct import DummyStruct

class ProblemData(DummyStruct):
    def __init__(self) -> None:
        self.index = str()
        self.interactive = bool()
        self.input = list()
        self.output = list()
        self.time_limit = float()
        self.memory_limit = int()
        self.sample_count = int()