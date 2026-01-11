from system.structures.configStruct import ConfigStruct
from colorama import Fore, Back

reset_all = Fore.RESET + Back.RESET


class InterfaceConfig(ConfigStruct):
    def __init__(self):
        self.text_color = Fore.WHITE
        self.text_background = Back.RESET
        self.success_color = Fore.GREEN
        self.success_background = Back.RESET
        self.error_color = Fore.RED
        self.error_background = Back.RESET
        self.system_color = Fore.CYAN
        self.system_background = Back.RESET
        self.warning_color = Fore.YELLOW
        self.warning_background = Back.RESET

        self.highlight_files = True

        self.command_color = 'SpringGreen'
        self.file_color = 'OrangeRed'
        self.regular_color = 'Wheat'
        self.flag_color = 'HotPink'

    def success(self, message: str):
        return self.success_color + self.success_background + message + reset_all

    def error(self, message: str):
        return self.error_color + self.error_background + message + reset_all
    
    def warning(self, message: str):
        return self.warning_color + self.warning_background + message + reset_all

    def text(self, message: str):
        return self.text_color + self.text_background + message + reset_all

    def system(self, message: str):
        return self.system_color + self.system_background + message + reset_all