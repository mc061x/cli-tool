from copy import deepcopy

class Flag:
    def __init__(self, name = str(), arg_count = 0) -> None:
        self.name = name
        self.present = False
        self.arg_count = arg_count
        self.arg_list = list()

class FlagParser:
    def __init__(self, arg_list: list) -> None:
        self.arg_list = deepcopy(arg_list)

    def parse_command(self, command: list) -> [list, list]:
        key: Flag
        for key in self.arg_list:
            if key.name in command:
                key.present = True
                occ = command.index(key.name)
                command.remove(key.name)

                try:
                    for _ in range(key.arg_count):
                        key.arg_list.append(command[occ])
                        command.remove(command[occ])
                except IndexError:
                    raise IndexError(f'Error: flag {key.name} expected {key.arg_count} args, got {len(key.arg_list)} instead')
        return command