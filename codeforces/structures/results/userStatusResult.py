from system.structures.dummyStruct import DummyStruct
from system.structures.typelist import MyList
from codeforces.structures.submission import Submission


class UserStatusResult(DummyStruct):
    def __init__(self, object: list) -> None:
        super().__init__()
        self.user_status = MyList(Submission)
        self.user_status.from_json(array=object)

