from config.generalCfg import GeneralConfig
from handlers.contest.handle_join import ContestJoinHandler
from handlers.contest.handle_problem_switch import ProblemSwitchHandler
from handlers.contest.handle_submit import ContestSubmitHandler
from config.get_config import dump_config
from exceptions import *


class ContestHandler:
    def __init__(self, cfg: GeneralConfig) -> None:
        self.cfg = cfg
    
    def handle(self, command: str):
        command = command[1:]

        if command[0] == 'join':
            handler = ContestJoinHandler(cfg=self.cfg)
            handler.handle(command)
            dump_config(cfg=self.cfg)
        
        if command[0] in ['nxt', 'prev', 'prob']:
            handler = ProblemSwitchHandler(cfg=self.cfg)
            handler.handle(command)
            dump_config(cfg=self.cfg)

        if command[0] == 'submit':
            handler = ContestSubmitHandler(cfg=self.cfg)
            handler.handle(command)
            dump_config(cfg=self.cfg)