from text.print_cfg import print_cfg
from config.generalCfg import GeneralConfig
from exceptions import *

class GenCfgPrinter:
    def __init__(self, cfg: GeneralConfig) -> None:
        self.cfg = cfg
    
    def handle(self, command: list):
        command = command[1:]
        if len(command):
            handle_exception(self.cfg.interfaceCfg.error, RuntimeError('This function does not take parameters'))
        
        print_cfg(cfg=self.cfg, intf=self.cfg.interfaceCfg)