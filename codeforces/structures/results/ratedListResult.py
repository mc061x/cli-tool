from codeforces.structures.user import User
from system.structures.dummyStruct import DummyStruct
from system.structures.typelist import MyList


class RatedListResult(DummyStruct):
    def __init__(self, array: list) -> None:
        super().__init__()
        self.rated_list = MyList(User)
        self.from_json(object=array)

        self.list_fill = ['rated_list']