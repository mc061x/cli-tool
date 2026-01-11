from system.structures.typelist import MyList
from system.structures.configStruct import ConfigStruct
from system.config.runSettings import RunSettings
from system.config.runConfigOption import RunConfigOption
from exceptions import *
from copy import deepcopy


def check_for_alias(alias: str, cfg_list: MyList) -> None:
    option: RunConfigOption
    for option in cfg_list.list:
        if option.alias == alias:
            return
    raise ConfigNotFoundException(f'Config with alias {alias} not found')


def check_for_last_config(cfg_list: MyList) -> None:
    if len(cfg_list.list) == 1:
        raise CannotLeaveEmptyConfigListException(f'Cannot remove the last config')


def find_option(alias: str, cfg_list: MyList) -> RunConfigOption:
    option: RunConfigOption
    for option in cfg_list.list:
        if option.alias == alias:
            return option


class RunCfg(ConfigStruct):
    def __init__(self):
        super().__init__()
        self.runOptionList = MyList(RunConfigOption)
        self.currentRunOption = RunSettings()
        self.currentRunAlias = 'main'

        self.add_run_option(new_alias='main')

    def add_run_option(self, new_alias: str, copy_from: str = -1):
        if copy_from != -1:
            check_for_alias(copy_from, self.runOptionList)

            current_option = find_option(alias=copy_from, cfg_list=self.runOptionList)

            self.runOptionList.list.append(
                deepcopy(RunConfigOption(alias=new_alias, runSettings=current_option.option)))

        else:
            self.runOptionList.list.append(
                deepcopy(RunConfigOption(alias=new_alias, runSettings=RunSettings())))

    def remove_run_config(self, alias: str, checkForLast: bool = True, change_option: bool = True):
        check_for_alias(alias=alias, cfg_list=self.runOptionList)
        if checkForLast:
            check_for_last_config(cfg_list=self.runOptionList)

        current_option = find_option(alias=alias, cfg_list=self.runOptionList)
        self.runOptionList.list.remove(current_option)

        if self.currentRunAlias == current_option.alias and change_option == True:
            first_option: RunConfigOption = self.runOptionList.list[0]

            self.currentRunAlias = first_option.alias
            self.currentRunOption = first_option.option

    def change_run_config(self, alias: str, newCfg: RunSettings):
        self.remove_run_config(alias=alias, checkForLast=False, change_option=False)
        self.runOptionList.list.append(
            deepcopy(RunConfigOption(alias=alias, runSettings=newCfg))
        )

        if alias == self.currentRunAlias:
            self.currentRunOption = deepcopy(newCfg)
    
    def select_run_config(self, alias: str):
        check_for_alias(alias=alias, cfg_list=self.runOptionList)
        self.currentRunAlias = alias
        self.currentRunOption = find_option(alias=alias, cfg_list=self.runOptionList).option