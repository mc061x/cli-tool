from config.cfCfg import CfConfig
from config.apiCfg import ApiConfig
from config.runCfg import RunCfg
from config.interfaceCfg import InterfaceConfig
from system.structures.configStruct import ConfigStruct
import sys


class GeneralConfig(ConfigStruct):
    def __init__(self) -> None:
        super().__init__()
        self.interfaceCfg = InterfaceConfig()
        self.cfConfig = CfConfig()
        self.apiConfig = ApiConfig()
        self.runCfg = RunCfg()

        if sys.platform == "linux":
            self.unix = True
        else:
            self.unix = False

        self.directory = str()