from config.generalCfg import GeneralConfig
from config.runCfg import *
from system.structures.flag import *
from config.get_config import dump_config
from exceptions import *

flags = [
    Flag(name='-from', arg_count=1),
]

parser = FlagParser(flags)

class RunCfgAdder:
    def handle(self, cfg: GeneralConfig, command: list):
        command = command[1:]
        try:
            parser.parse_command(command)

            if len(command) > 1:
                handle_exception(cfg.interfaceCfg.error, RuntimeError('Too many parameters'))
                return
            
            if len(command) == 0:
                handle_exception(cfg.interfaceCfg.error, RuntimeError('Alias not specified'))
                return
            
            try:
                new_alias = command[0]
            except IndexError as exc:
                handle_exception(cfg.interfaceCfg.error, exc)
                return
            
            flag: Flag
            for flag in parser.arg_list:
                if flag.name == '-from' and flag.present:
                    
                    alias = flag.arg_list[0]
                    try:
                        check_for_alias(alias=alias, cfg_list=cfg.runCfg.runOptionList)
                    except ConfigNotFoundException as exc:
                        handle_exception(cfg.interfaceCfg.error, exc)
                        return
                    
                    cfg.runCfg.add_run_option(new_alias=new_alias, copy_from=alias)
                    dump_config(cfg)

                    print(cfg.interfaceCfg.success(f'Successfully added new config {new_alias} and copied from {alias}'))
                    return
        
        except IndexError as exc:
            handle_exception(cfg.interfaceCfg.error, exc)
            return

        cfg.runCfg.add_run_option(new_alias=new_alias)
        dump_config(cfg)
        print(cfg.interfaceCfg.success(f'Successfully added config {new_alias} with default options'))