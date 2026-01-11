from config.generalCfg import GeneralConfig
from exceptions import *

class ProblemSwitchHandler:
    def __init__(self, cfg: GeneralConfig) -> None:
        self.cfg = cfg

    def handle(self, command: str):
        if command[0] == 'nxt':
            current_index = self.cfg.cfConfig.current_contest.current_problem_index
            current_index = self.cfg.cfConfig.current_contest.problem_list.index(current_index)

            next_index = (current_index + 1) % len(self.cfg.cfConfig.current_contest.problem_list)
            self.cfg.cfConfig.current_contest.current_problem_index = self.cfg.cfConfig.current_contest.problem_list[next_index]

        if command[0] == 'prev':
            current_index = self.cfg.cfConfig.current_contest.current_problem_index
            current_index = self.cfg.cfConfig.current_contest.problem_list.index(current_index)

            prev_index = (current_index - 1) % len(self.cfg.cfConfig.current_contest.problem_list)
            self.cfg.cfConfig.current_contest.current_problem_index = self.cfg.cfConfig.current_contest.problem_list[prev_index]
        
        if command[0] == 'prob':
            if len(command) == 1:
                handle_exception(self.cfg.interfaceCfg.error, Exception('No problem specified'))
                return
            if len(command) > 2:
                handle_exception(self.cfg.interfaceCfg.error, Exception('Too many parameters'))
                return
            
            if command[1] not in self.cfg.cfConfig.current_contest.problem_list:
                handle_exception(self.cfg.interfaceCfg.error, Exception(f'Problem {command[1]} not found'))
                return
            self.cfg.cfConfig.current_contest.current_problem_index = command[1]
        
            