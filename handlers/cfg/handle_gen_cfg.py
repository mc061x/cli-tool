from config.generalCfg import GeneralConfig
from handlers.cfg.cfg_edit.handle_gen_edit import GeneralCfgModifier
from handlers.cfg.cfg_print.handle_gen_print import GenCfgPrinter

from text.print_cfg import print_cfg

class GenCfgHandler:
    def __init__(self, cfg: GeneralConfig) -> None:
        self.cfg = cfg
    
    def handle(self, command: list) -> None:
        command = command[1:]

        if command[0] == 'edit':
            GeneralCfgModifier.handle(cfg=self.cfg)
            return
    
        if command[0] == 'print':
            GenCfgPrinter(cfg=self.cfg).handle(command)
            return
