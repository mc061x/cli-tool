from system.structures.dummyStruct import DummyStruct
from codeforces.structures.member import Member as Member
from system.structures.typelist import MyList


class Party(DummyStruct):
    def __init__(self) -> None:
        super().__init__()
        self.contestId = str()
        self.members = MyList(Member)
        self.participantType = str()
        self.teamId = int()
        self.teamName = str()
        self.ghost = bool()
        self.room = int()
        self.startTimeSeconds = int()
