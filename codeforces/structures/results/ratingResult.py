from system.structures.dummyStruct import DummyStruct
from system.structures.typelist import MyList
from codeforces.structures.ratingChange import RatingChange


class RatingResult(DummyStruct):
    def __init__(self, object: list) -> None:
        super().__init__()
        self.rating_changes = MyList(RatingChange)
        self.rating_changes.from_json(array=object)

