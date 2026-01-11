from copy import deepcopy


class DummyStruct:
    def __init__(self) -> None:
        pass

    def from_json(self, object: list | dict) -> None:
        attr_list, key_list = self.__dict__.keys(), object.keys()
        for attr in attr_list:
            if attr in key_list:
                if hasattr(getattr(self, attr), 'to_json'):
                    new_value = getattr(self, attr)
                    new_value.from_json(deepcopy(object[attr]))
                    setattr(self, attr, new_value)
                else:
                    setattr(self, attr, deepcopy(object[attr]))

    def to_json(self) -> list | dict:
        attr_list = self.__dict__.keys()

        result = dict()
        for attr in attr_list:
            value = getattr(self, attr)
            if hasattr(value, 'to_json'):
                result[attr] = value.to_json()
            else:
                result[attr] = value
        return result
    
    def get_printable_attrs(self) -> dict:
        attrs = dict()
        for attr_name in self.__dict__.keys():
            attr = getattr(self, attr_name)
            if type(attr) == int or type(attr) == str or type(attr) == float or type(attr) == list:
                attrs[attr_name] = attr
        return attrs
