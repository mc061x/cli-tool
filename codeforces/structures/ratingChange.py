from system.structures.dummyStruct import DummyStruct


class RatingChange(DummyStruct):
    def __init__(self):
        super().__init__()
        self.contestId = int()
        self.contestName = str()
        self.handle = str()
        self.rank = int()
        self.ratingUpdateTimeSeconds = int()
        self.oldRating = int()
        self.newRating = int()