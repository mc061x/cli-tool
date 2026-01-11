from config.generalCfg import GeneralConfig
from codeforces.structures.problemData import ProblemData
from tabulate import tabulate

def form_headers(cfg: GeneralConfig) -> list:
    headers = []
    headers.append(cfg.interfaceCfg.system('ID'))
    headers.append(cfg.interfaceCfg.system('Time Limit'))
    headers.append(cfg.interfaceCfg.system('Memory Limit'))
    headers.append(cfg.interfaceCfg.system('Interactive'))
    headers.append(cfg.interfaceCfg.system('Sample Count'))
    return headers

def form_row(cfg: GeneralConfig, problem: ProblemData) -> list:
    current_row = []
    current_row.append(cfg.interfaceCfg.success(str(problem.index)))
    current_row.append(cfg.interfaceCfg.warning(str(problem.time_limit)) + cfg.interfaceCfg.warning('s'))
    current_row.append(cfg.interfaceCfg.warning(str(problem.memory_limit)) + cfg.interfaceCfg.warning('MB'))
    current_row.append(cfg.interfaceCfg.success('Yes' if problem.interactive else 'No'))
    current_row.append(cfg.interfaceCfg.success(str(problem.sample_count)))
    return current_row

def display_contest(cfg: GeneralConfig) -> None:
    headers = form_headers(cfg)
    rows = []

    problem: ProblemData
    for problem in cfg.cfConfig.current_contest.problem_data.list:
        current_row = form_row(cfg, problem)
        rows.append(current_row)

    table = tabulate(rows, headers=headers, tablefmt='fancy_grid', stralign='center', numalign='center')
    print(table)

