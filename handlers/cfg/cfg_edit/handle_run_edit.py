from config.generalCfg import GeneralConfig
from config.runCfg import *
from config.interfaceCfg import InterfaceConfig
from handlers.modify_cfg import modify_cfg
from config.get_config import dump_config
from exceptions import *
import os

from handlers.run_util import get_alias, print_aliases

def check_files(cfg: RunSettings):
    fullInputPath = cfg.input_file_path
    if not fullInputPath == '' and (not os.path.exists(fullInputPath) or not os.path.isfile(fullInputPath)):
        raise InvalidAttributeValue(f'Input file at path {fullInputPath} not found')
    
    fullOutputPath =cfg.output_file_path
    if not fullOutputPath == '' and (not os.path.exists(fullOutputPath) or not os.path.isfile(fullOutputPath)):
        raise InvalidAttributeValue(f'Output file at path {fullOutputPath} not found')

def check_changes(cfg: RunSettings):
    check_files(cfg=cfg)
    
    return True

class RunCfgModifier:
    def handle(self, cfg: GeneralConfig, command: list):
        if '-a' in command:
            try:
                alias = command[command.index('-a') + 1]
            except IndexError:
                handle_exception(cfg.interfaceCfg.error, IndexError('Alias not specified'))
        else:
            alias = get_alias(cfg)
        
        try:
            check_for_alias(alias=alias, cfg_list=cfg.runCfg.runOptionList)
        except ConfigNotFoundException as exc:
            handle_exception(cfg.interfaceCfg.error, exc)
            return

        current_option = find_option(alias=alias, cfg_list=cfg.runCfg.runOptionList).option
        current_option = modify_cfg(current_option, cfg.interfaceCfg, check_changes)
        if current_option is None:
            return
        cfg.runCfg.change_run_config(alias=alias, newCfg=current_option)
        dump_config(cfg)