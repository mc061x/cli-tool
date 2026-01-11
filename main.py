from text.wrapper import TextWrapper
from config.generalCfg import GeneralConfig
from config.get_config import get_cfg, dump_config
from handlers.main_handler import MainHandler

cfg: GeneralConfig = get_cfg()
wrapper = TextWrapper(cfg=cfg)
handler = MainHandler(cfg=cfg)


while True:
    command: str = wrapper.get_command()
    if command == 'quit':
        break

    handler.handle(command)
    
    cfg = get_cfg()