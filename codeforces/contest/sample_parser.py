import re
from bs4 import BeautifulSoup as BS
from codeforces.API import API

from codeforces.contest.url_util import get_all_statements_url
from codeforces.structures.problemData import ProblemData
from system.structures.typelist import MyList

def get_problems_html(api: API, contest_id: int) -> BS:
    page = api.page_request(get_all_statements_url(contest_id=contest_id))
    html = BS(page, 'html.parser')
    return html

def parse_problem_ids(html: BS) -> list:
    problem_ids = [problem['problemindex'] for problem in html.select('.problemindexholder')]
    return problem_ids

def parse_problem_samples(problem_section: BS, current_problem: ProblemData) -> None:
    for stream in ['input', 'output']:
        for testcase in problem_section.select(f'.{stream} > pre'):
            data = [element.strip() for element in testcase.stripped_strings]
            if stream == 'input':
                current_problem.input.append('\n'.join(data))
            else:
                current_problem.output.append([line.strip() for element in data for line in element.split('\n')])
    current_problem.sample_count = len(current_problem.input)

def parse_interaction(problem_section: BS, current_problem: ProblemData) -> None:
    current_problem.interactive = any('Interaction' in i for i in problem_section.select('.section-title'))

def parse_problem_constraints(problem_section: BS, current_problem: ProblemData) -> None:
    time_limit_text = problem_section.select_one('.time-limit').text.strip()
    time_limit_match = re.search(r'\d+(\.\d+)?', time_limit_text)
    current_problem.time_limit = float(time_limit_match.group())

    memory_limit_text = problem_section.select_one('.memory-limit').text.strip()
    memory_limit_match = re.search(r'\d+', memory_limit_text)
    current_problem.memory_limit = int(memory_limit_match.group())

def parse_problem_data(html: BS) -> MyList(ProblemData):
    problem_data = MyList(ProblemData)

    for problem_id in parse_problem_ids(html):
        current_problem = ProblemData()
        current_problem.index = problem_id
        problem_section = html.select_one(f'div[problemindex="{problem_id}"]')

        parse_problem_samples(problem_section, current_problem)
        parse_problem_constraints(problem_section, current_problem)
        parse_interaction(problem_section, current_problem)
        problem_data.list.append(current_problem)

    return problem_data