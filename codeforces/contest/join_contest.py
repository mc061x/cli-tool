import codeforces.contest.sample_parser as SampleParser
from codeforces.API import API
from config.generalCfg import GeneralConfig

def join_contest(contest_id: int, cfg: GeneralConfig) -> None:
    html = SampleParser.get_problems_html(API(api_cfg=cfg.apiConfig), contest_id)
    cfg.cfConfig.current_contest.problem_list = SampleParser.parse_problem_ids(html)
    if len(cfg.cfConfig.current_contest.problem_list) == 0:
        raise Exception(f'No problems found in contest {contest_id}')
    try:
        cfg.cfConfig.current_contest.problem_data = SampleParser.parse_problem_data(html)
    except Exception as exc:
        raise Exception(f'Failed to parse problem data: {exc}')
    cfg.cfConfig.current_contest.contest_id = contest_id
    cfg.cfConfig.current_contest.current_problem_index = cfg.cfConfig.current_contest.problem_list[0]

    
