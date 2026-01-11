from codeforces.API import API
from codeforces.requester import Requester
from codeforces.structures.hacks import Hack
from codeforces.structures.member import Member
from config.generalCfg import GeneralConfig
from system.structures.typelist import MyList
from exceptions import *


def assert_handle_not_empty(cfg: GeneralConfig):
    if cfg.cfConfig.handle == '':
        raise HandleNotSetException


def is_being_targeted(cfg: GeneralConfig) -> MyList(Hack):
    assert_handle_not_empty(cfg=cfg)

    current_api = API(api_cfg=cfg.apiConfig)
    requester = Requester(api=current_api)

    hacks = requester.hacks({
        'contestId': cfg.cfConfig.current_contest
    }).hack_list.list

    result = MyList(Hack)

    current_hack: Hack
    for current_hack in hacks:
        member: Member
        for member in current_hack.defender.members.list:
            if member.handle == cfg.cfConfig.handle:
                result.list.append(current_hack)

    return result


def my_targets(cfg: GeneralConfig) -> MyList(Hack):
    assert_handle_not_empty(cfg=cfg)

    current_api = API(api_cfg=cfg.apiConfig)
    requester = Requester(api=current_api)

    hacks = requester.hacks({
        'contestId': cfg.cfConfig.current_contest
    }).hack_list.list

    result = MyList(Hack)

    current_hack: Hack
    for current_hack in hacks:  #
        member: Member
        for member in current_hack.hacker.members.list:
            if member.handle == cfg.cfConfig.handle:
                result.list.append(current_hack)

    return result
