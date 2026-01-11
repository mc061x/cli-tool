from system.structures.configStruct import ConfigStruct
from codeforces.contest.contestStruct import ContestData


class CfConfig(ConfigStruct):
    def __init__(self) -> None:
        super().__init__()
        self.handle = str()
        self.friend_handles = list()

        self.current_contest = ContestData()

        