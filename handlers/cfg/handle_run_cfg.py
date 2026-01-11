from config.generalCfg import GeneralConfig
from handlers.cfg.cfg_edit.handle_run_edit import RunCfgModifier
from handlers.cfg.cfg_print.handle_run_print import RunCfgPrinter
from handlers.cfg.cfg_add.handle_run_add import RunCfgAdder
from handlers.cfg.cfg_select.handle_run_select import RunCfgSelector
from handlers.cfg.cfg_rm.handle_run_rm import RunCfgRemover

from text.print_cfg import print_cfg

class RunCfgHandler:
    def __init__(self, cfg: GeneralConfig) -> None:
        self.cfg = cfg
    
    def handle(self, command: list) -> None:
        command = command[1:]

        if command[0] == 'edit':
            RunCfgModifier().handle(cfg=self.cfg, command=command)
            return
    
        if command[0] == 'print':
            RunCfgPrinter().handle(cfg=self.cfg, command=command)
            return

        if command[0] == 'add':
            RunCfgAdder().handle(cfg=self.cfg, command=command)
            return
        
        if command[0] == 'sel':
            RunCfgSelector().handle(cfg=self.cfg, command=command)
            return
        
        if command[0] == 'rm':
            RunCfgRemover().handle(cfg=self.cfg, command=command)
            return
        
        print(self.cfg.interfaceCfg.error(f'Unknown command: cfg run {" ".join(command)}')) 