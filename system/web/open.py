import webbrowser
from config.generalCfg import GeneralConfig

def get_problems_link(contest_id: str):
    return f"https://codeforces.com/contest/{contest_id}/problems"

def get_standings_link(contest_id: str, friends: bool = False):
    return f"https://codeforces.com/contest/{contest_id}/standings/friends/{'true' if friends else 'false'}"

def open_problems(cfg: GeneralConfig) -> bool:
    return webbrowser.open(get_problems_link(cfg.cfConfig.current_contest.contest_id))

def open_standings(cfg: GeneralConfig, friends: bool) -> bool:
    return webbrowser.open(get_standings_link(cfg.cfConfig.current_contest.contest_id, friends))
