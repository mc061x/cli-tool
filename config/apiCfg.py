from system.structures.configStruct import ConfigStruct


class ApiConfig(ConfigStruct):
    def __init__(self) -> None:
        super().__init__()
        self.key = ''
        self.secret = ''
        self.timeout = 10