from system.structures.dummyStruct import DummyStruct


class User(DummyStruct):
    def __init__(self) -> None:
        super().__init__()
        self.handle = str()
        self.email = str()
        self.firstName = str()
        self.lastName = str()
        self.country = str()
        self.city = str()
        self.organization = str()
        self.contribution = int()
        self.rank = str()
        self.rating = int()
        self.maxRank = str()
        self.maxRating = int()
        self.lastOnlineSeconds = int()
        self.registrationTimeSeconds = int()
        self.friendOfCount = int()
