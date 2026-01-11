from codeforces.structures.hacks import Hack
from system.structures.typelist import MyList
from system.structures.dummyStruct import DummyStruct


class HacksResult(DummyStruct):
    def __init__(self, json: list) -> None:
        super().__init__()
        self.hack_list = MyList(Hack)
        self.from_json(object=json)
