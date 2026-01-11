import os, json
from config.generalCfg import GeneralConfig

DEFUALT_FOLDER = 'tool-data'
DEFAULT_NAME = 'general-cfg.json'
FULL_PATH = os.path.join(DEFUALT_FOLDER, DEFAULT_NAME)


def create_file(path: str) -> None:
    f = open(path, 'x')
    f.close()

def dump_config(cfg: GeneralConfig):
    json.dump(obj=cfg.to_json(), fp=open(FULL_PATH, 'w'), indent=2)

def assure_cfg_exists():
    if not os.path.exists(DEFUALT_FOLDER):
        print('i')
        init = GeneralConfig()
        os.mkdir(DEFUALT_FOLDER)
        create_file(FULL_PATH)
        dump_config(cfg=init)        

def fix_directory(cfg: GeneralConfig):
    if not cfg.directory.strip() or not os.path.exists(cfg.directory):
        cfg.directory = os.getcwd()

def get_cfg():
    assure_cfg_exists()
    ret = GeneralConfig()
    ret.from_json(json.load(open(FULL_PATH, 'r')))
    fix_directory(ret)
    return ret