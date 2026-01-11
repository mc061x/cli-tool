from system.structures.configStruct import ConfigStruct
from config.interfaceCfg import InterfaceConfig
import colorama

def print_cfg(cfg: ConfigStruct, intf: InterfaceConfig):
    attrs = cfg.get_printable_attrs()
    mx_name_len = 0
    for name in attrs:
        mx_name_len = max(mx_name_len, len(name))
    for i, attr in enumerate(attrs):
        first = str(i) + ' ' * (1 + int(len(attrs) >= 10) - len(str(i))) + ' | '
        print(intf.system(first), end='')

        second = str(attr) + ' ' * (mx_name_len - len(attr)) + ' = ' 
        print(intf.success(second), end='')

        third = str(attrs[attr])
        print(intf.system(third), end='')

        print(colorama.Fore.YELLOW + '(', type(attrs[attr]).__name__, ')' + colorama.Fore.RESET, sep='')