from config.generalCfg import GeneralConfig
from config.runCfg import RunConfigOption

def get_alias(cfg: GeneralConfig, message='modify'):
    print_aliases(cfg)
    print(cfg.interfaceCfg.system(f'Which config do you want to {message}(alias)? > '), end='')
    alias = input().strip()

    return alias

def print_aliases(cfg: GeneralConfig):
    attrs = list()
    option: RunConfigOption
    for option in cfg.runCfg.runOptionList.list:
        attrs.append(option.alias)

    mx_name_len = 0
    for name in attrs:
        mx_name_len = max(mx_name_len, len(name))
    for i, attr in enumerate(attrs):
        first = str(i) + ' ' * (1 + int(len(attrs) >= 10) - len(str(i))) + ' | '
        print(cfg.interfaceCfg.system(first), end='')

        second = str(attr) + ' ' * (mx_name_len - len(attr)) 
        print(cfg.interfaceCfg.success(second))