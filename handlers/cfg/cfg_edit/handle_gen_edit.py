from config.generalCfg import GeneralConfig
from handlers.modify_cfg import modify_cfg
from config.get_config import dump_config
from exceptions import *
import os

def check_directory(cfg: GeneralConfig) -> bool:
    if not os.path.exists(cfg.directory):
        raise InvalidAttributeValue(f'Directory {cfg.directory} not found')

def check_changes(new: GeneralConfig) -> bool:
    check_directory(cfg=new)

    return True

class GeneralCfgModifier:
    def handle(cfg: GeneralConfig):
        result = modify_cfg(cfg, cfg.interfaceCfg, check_changes)
        if result != None:
            cfg=result
        dump_config(cfg)