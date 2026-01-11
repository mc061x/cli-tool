from system.structures.configStruct import ConfigStruct
from system.config.runSettings import RunSettings


class RunConfigOption(ConfigStruct):
    def __init__(self, alias: str = str(), runSettings: RunSettings = RunSettings()):
        super().__init__()

        self.alias = alias
        self.option = runSettings
