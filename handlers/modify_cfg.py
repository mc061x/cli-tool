from system.structures.configStruct import ConfigStruct
from config.interfaceCfg import InterfaceConfig
from text.print_cfg import print_cfg
from exceptions import *
from typing import Callable

def modify_cfg(cfg: ConfigStruct, interface: InterfaceConfig, validator: Callable[[ConfigStruct], bool]) -> ConfigStruct:
    print_cfg(cfg, interface)

    print(interface.system('Which option do you want to modify(index)? > '), end='')
    index = input().strip()
    try:
        index = int(index)
    except:
        handle_exception(interface.error, ValueError(f'Index must be an Integer, not \'{index}\''))
        return None

    attrs = cfg.get_printable_attrs()
    if index not in range(len(attrs)):
        handle_exception(interface.error, ValueError(f'Index {index} out of range'))
        return None
    attr = list(attrs.keys())[index]

    print(interface.system('Enter new'), interface.success(f'{attr}'), interface.system('value: > '), end='')
    new_value = input().strip()
    try:
        cfg = cfg.modify(attr_name=attr, new_value=new_value, validator_func=validator)
    except InvalidAttributeValue as exc:
        handle_exception(interface.error, exc)
        return None
    except WrongAttributeTypeException as exc:
        handle_exception(interface.error, exc)
        return None
    
    print(interface.success(f'Successfully modified {attr} to {new_value}'))
    return cfg