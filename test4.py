from codeforces.structures.submission import Submission
from codeforces.API import ApiConfig, API
from codeforces.requester import Requester

import sys
import colorama

if len(sys.argv) < 2:
    print(f'{colorama.Fore.RED}Handle not specified!{colorama.Style.RESET_ALL}')
    exit(0)

current_handle = sys.argv[1]

cfg = ApiConfig()

cfg.timeout = 5

sub_count = 8

api = API(cfg)
method = 'user.status?'
args = {
    'handle' : current_handle,
    'count' : sub_count
}

import sys, time
from codeforces.requester import Requester
from codeforces.structures.submission import Submission
# sys.stdout = open('logs/log.txt', 'w')

import reprint
import datetime
from exceptions import *
import json

columns = ['name', 'language', 'verdict', 'tests', 'time', 'memory', 'testset']

def center(s, ln: int) -> str:
    need_spaces = ln - len(str(s))
    right_spaces = need_spaces // 2
    left_spaces = need_spaces - right_spaces
    return ' ' * left_spaces + str(s) + ' ' * right_spaces

def tabulate_submissions(submissions: list[Submission]):
    table = dict()
    mx_len = dict()
    for column in columns: table[column] = mx_len[column] = list()
    for sub in submissions:
        table['name'].append(sub.problem.index + '-' + sub.problem.name)
        table['verdict'].append(sub.verdict)
        table['language'].append(sub.programmingLanguage)
        table['time'].append(sub.timeConsumedMillis)
        table['memory'].append(sub.memoryConsumedBytes)
        table['tests'].append(sub.passedTestCount)
        table['testset'].append(sub.testset)
    for idx in range(len(table['memory'])):
        table['memory'][idx] //= 1024
        table['memory'][idx] = str(table['memory'][idx]) + ' KB'
    for idx in range(len(table['time'])):
        table['time'][idx] = str(table['time'][idx]) + ' ms'
    for column in columns:
        mx_len[column] = max(len(str(x)) for x in table[column])
        mx_len[column] = max(mx_len[column], len(column))
        idx = 0
        for item in table[column]:
            current_len = len(str(item))
            need_spaces = mx_len[column] - current_len
            right_spaces = need_spaces // 2
            left_spaces = need_spaces - right_spaces
            table[column][idx] = ' ' * left_spaces + str(item) + ' ' * right_spaces
            idx += 1
    return table
    # print(json.dumps(table, indent=4), file=open('logs/log.txt', 'w'))

colors = {
    'name' : colorama.Fore.BLUE,
    'language' : colorama.Fore.MAGENTA,
    'tests' : colorama.Fore.MAGENTA,
    'time' : colorama.Fore.CYAN,
    'memory' : colorama.Fore.CYAN,
    'testset' : colorama.Fore.CYAN
}

with reprint.output(initial_len=sub_count + 2) as output:
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        try:
            req = Requester(api)
            x = req.user_status(args, authorize=False).user_status.list
            table = tabulate_submissions(x)
            
            for i in range(sub_count + 2):
                output[i] = ''

            for column in columns:
                output[0] += f'{colorama.Fore.YELLOW}{center(column, len(table[column][0]))}{colorama.Style.RESET_ALL} | '
                for idx in range(len(table[column])):
                    if column != 'verdict' and column != 'tests':
                        output[idx + 1] += f'{colors[column]}{table[column][idx]}{colorama.Style.RESET_ALL} | '
                    else:
                        vd = table['verdict'][idx]
                        col = ''
                        if 'OK' in vd:
                            col = colorama.Fore.GREEN
                        elif 'TESTING' in vd:
                            col = colorama.Fore.YELLOW
                        else:
                            col = colorama.Fore.RED
                        output[idx + 1] += f'{col}{table[column][idx]}{colorama.Style.RESET_ALL} | '
            output[sub_count + 1] = f'{colorama.Fore.RED}{colorama.Back.BLACK}Refreshed at: {current_time} | API status : OK {colorama.Style.RESET_ALL}'
        except KeyboardInterrupt:
            break
        except InternalAPIErrorException as exc:
            output[sub_count + 1] = f'{colorama.Fore.RED}{colorama.Back.BLACK}Refreshed at: {current_time} | API status : NOT WORKING {colorama.Style.RESET_ALL}'
        except RequestTimeoutException as exc:
            output[sub_count + 1] = f'{colorama.Fore.RED}{colorama.Back.BLACK}Refreshed at: {current_time} | API status : TIMEOUT {colorama.Style.RESET_ALL}'
        except:
            output[sub_count + 1] = f'{colorama.Fore.RED}{colorama.Back.BLACK}Refreshed at: {current_time} | API status : UNKNOWN {colorama.Style.RESET_ALL}'
        time.sleep(5)
        
