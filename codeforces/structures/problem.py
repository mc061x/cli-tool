from system.structures.dummyStruct import DummyStruct


class Problem(DummyStruct):
    def __init__(self) -> None:
        super().__init__()
        self.contestId = str()
        self.problemsetName = str()
        self.index = str()
        self.name = str()
        self.type = str()
        self.rating = int()
        self.tags = list()
