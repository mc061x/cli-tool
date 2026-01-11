from text.print_cfg import print_cfg
from config.generalCfg import GeneralConfig
from config.runCfg import find_option, check_for_alias, RunConfigOption
from exceptions import *

class RunCfgPrinter:
    def handle(self, cfg: GeneralConfig, command: list):
        if '-a' in command:
            alias: str = str()
            try:
                alias = command[command.index('-a') + 1]
            except IndexError:
                handle_exception(cfg.interfaceCfg.error, IndexError('Alias not specified'))
                return
            try:
                check_for_alias(alias=alias, cfg_list=cfg.runCfg.runOptionList)
            except ConfigNotFoundException as exc:
                handle_exception(cfg.interfaceCfg.error, exc)
                return
            option = find_option(alias=alias, cfg_list=cfg.runCfg.runOptionList).option
            print_cfg(cfg=option, intf=cfg.interfaceCfg)
        elif '-all' in command:
            option: RunConfigOption
            for option in cfg.runCfg.runOptionList.list:
                print(cfg.interfaceCfg.error(option.alias))
                print_cfg(cfg=option.option, intf=cfg.interfaceCfg)
        elif '-cur' in command:
            print_cfg(cfg=cfg.runCfg.currentRunOption, intf=cfg.interfaceCfg)
        else:
            print_cfg(cfg=cfg.runCfg, intf=cfg.interfaceCfg)