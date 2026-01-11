from system.structures.dummyStruct import DummyStruct
from typing import Callable
from copy import deepcopy
from exceptions import *


def convert(new_value, old_value) -> any:
    if type(old_value) == list:
        result = list()
        for element in new_value.split():
            result.append(element.strip())
        return result

    try:
        return type(old_value)(new_value)
    except ValueError:
        raise WrongAttributeTypeException(f'Value {new_value} cannot be converted to {type(old_value).__name__}')


class ConfigStruct(DummyStruct):
    def __init__(self):
        super().__init__()

    def change_attribute(self, attr_name: str, new_value: str):
        try:
            old_value = getattr(self, attr_name)
        except AttributeError:
            raise ConfigAttributeNotFoundException(f'Attribute {attr_name} not found')

        new_value = convert(new_value=new_value, old_value=old_value)

        setattr(self, attr_name, new_value)

    def modify(self, attr_name: str, new_value: str, validator_func: Callable[..., bool]):
        new_copy = deepcopy(self)
        new_copy.change_attribute(attr_name=attr_name, new_value=new_value)
        if validator_func(new_copy):
           return new_copy
    
        