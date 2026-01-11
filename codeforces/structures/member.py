from system.structures.dummyStruct import DummyStruct


class Member(DummyStruct):
    def __init__(self) -> None:
        super().__init__()
        self.handle = str()
        self.name = str()
