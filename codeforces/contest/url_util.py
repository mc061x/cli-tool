main_link = 'https://codeforces.com'
safe_link = 'https://m1.codeforces.com'

def get_contest_url(contest_id: int, safe_link: bool = False):
    link = main_link if not safe_link else safe_link
    return f'{link}/contest/{contest_id}'

def get_all_statements_url(contest_id: int, safe_link: bool = False):
    link = main_link if not safe_link else safe_link
    return f'{link}/contest/{contest_id}/problems'


 
