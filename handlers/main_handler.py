from config.generalCfg import GeneralConfig
from text.command_list import COMMAND_LIST
from handlers.handle_run import RunHandler 
from handlers.handle_cfg import CfgHandler
from handlers.handle_contest import ContestHandler

from copy import deepcopy

class MainHandler:
    def __init__(self, cfg: GeneralConfig) -> None:
        self.cfg = cfg
    
    def handle(self, command: str) -> None:
        command = command.strip()
        if command == '':
            return
        words = command.split()

        if words[0] not in COMMAND_LIST:
            print(self.cfg.interfaceCfg.error(f'Unknown command: {command}'))
            return
        

        if words[0] == 'run':
            handler = RunHandler(cfg=self.cfg)
            handler.handle(words)
            
        if words[0] == 'cfg':
            handler = CfgHandler(cfg=self.cfg)
            handler.handle(words)
        
        if words[0] == 'contest':
            handler = ContestHandler(cfg=self.cfg)
            handler.handle(words)
