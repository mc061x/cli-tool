from config.generalCfg import GeneralConfig
from handlers.cfg.handle_run_cfg import RunCfgHandler
from handlers.cfg.handle_gen_cfg import GenCfgHandler

class CfgHandler:
    def __init__(self, cfg: GeneralConfig) -> None:
        self.cfg = cfg
    
    def handle(self, command: str) -> None:
        command = command[1:]
        if command[0] == 'run':
            handler = RunCfgHandler(cfg=self.cfg)
            handler.handle(command)
        elif command[0] == 'gen':
            handler = GenCfgHandler(cfg=self.cfg)
            handler.handle(command)