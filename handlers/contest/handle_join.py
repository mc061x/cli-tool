from codeforces.contest.join_contest import join_contest
from codeforces.contest.display_contest import display_contest
from config.generalCfg import GeneralConfig
from exceptions import *

class ContestJoinHandler:
    def __init__(self, cfg: GeneralConfig) -> None:
        self.cfg = cfg

    def handle(self, command: str):
        command = command[1:]
        if len(command) == 0:
            handle_exception(self.cfg.interfaceCfg.error, RuntimeError('Contest ID is not specified'))
            return
        if len(command) > 1:
            handle_exception(self.cfg.interfaceCfg.error, RuntimeError('Too many parameters'))
            return
        try:
            join_contest(contest_id=command[0], cfg=self.cfg)
        except Exception as exc:
            handle_exception(self.cfg.interfaceCfg.error, exc)
            return
        print(self.cfg.interfaceCfg.success(f'Successfully joined contest №{command[0]}'))
        display_contest(self.cfg)