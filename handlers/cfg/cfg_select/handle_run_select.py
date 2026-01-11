from config.runCfg import *
from config.generalCfg import GeneralConfig
from config.get_config import dump_config
from exceptions import *

from handlers.run_util import get_alias, print_aliases

class RunCfgSelector:
    def handle(self, cfg: GeneralConfig, command: str) -> None:
        command = command[1:]
        if len(command):
            alias = command[0]
            try:
                check_for_alias(alias=command[0], cfg_list=cfg.runCfg.runOptionList)
            except ConfigNotFoundException as exc:
                handle_exception(cfg.interfaceCfg.error, exc)
                return
        else:
            alias = get_alias(cfg, message='select')
        option = find_option(alias=alias, cfg_list=cfg.runCfg.runOptionList).option
        cfg.runCfg.currentRunOption = option
        cfg.runCfg.currentRunAlias = alias
        print(cfg.interfaceCfg.success(f'Successfully selected config {alias}'))
        dump_config(cfg)