from config.generalCfg import GeneralConfig
from handlers.run_util import get_alias
from config.get_config import dump_config
from config.runCfg import *
from system.structures.flag import *

flags = [
    Flag(name='-a', arg_count=1),
]

parser = FlagParser(flags)

class RunCfgRemover:
    def handle(self, cfg: GeneralConfig, command: list) -> None:
        command = command[1:]
        parser.parse_command(command)

        flag: Flag
        for flag in parser.arg_list:
            if flag.name == '-a' and flag.present:
                alias = flag.arg_list[0]
                try:
                    check_for_alias(alias=alias, cfg_list=cfg.runCfg.runOptionList)
                except ConfigNotFoundException as exc:
                    handle_exception(cfg.interfaceCfg.error, exc)
                    return
                cfg.runCfg.remove_run_config(alias)
                dump_config(cfg)
                print(cfg.interfaceCfg.success(f'Successfully removed config {alias}'))
                return
        alias = get_alias(cfg, message='remove')
        cfg.runCfg.remove_run_config(alias)
        dump_config(cfg)
        print(cfg.interfaceCfg.success(f'Successfully removed config {alias}'))