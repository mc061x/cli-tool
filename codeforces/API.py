import requests, urllib.parse, random
from exceptions import *
from config.apiCfg import ApiConfig
from time import time
from hashlib import sha512

def calc_sha(data):
    return sha512(data.encode('utf-8')).hexdigest()

class API:
    def __init__(self, api_cfg: ApiConfig) -> None:
        self.url = 'https://codeforces.com/api/'
        self.ok_status = 'OK'
        self.ok_code = 200
        self.json_response = dict()
        self.cfg = api_cfg
        self.request_result = requests.Response

    def authorize(self, args: dict, method: str) -> dict:
        rand = str(random.randrange(100000, 1000000))
        time_arg = round(time())
        unhashed_string = f'{rand}/{method}'

        args['time'] = time_arg
        args['apiKey'] = self.cfg.key

        sorted_args = list()
        for arg in args:
            sorted_args.append((arg, args[arg]))
        sorted_args.sort()

        for arg in sorted_args:
            unhashed_string += f'{arg[0]}={arg[1]}&'
        unhashed_string = unhashed_string[:-1] + '#' + self.cfg.secret
        
        args['apiSig'] = f'{rand}{calc_sha(unhashed_string)}'

        return args

    def handle_misc_errors(self) -> None:
        if self.request_result.status_code != self.ok_code and self.request_result.status_code != 400:
            raise InternalAPIErrorException('API returned status code ' + str(self.request_result.status_code))

    def request_to_json(self) -> dict:
        result = self.request_result.json()
        if result['status'] != self.ok_status:
            raise InternalAPIErrorException(result['comment'])
        return result['result']

    def request(self, method: str, args: dict, authorize=False) -> dict | list:
        if authorize:
            args = self.authorize(args, method)
        # args['lang'] = 'en'
        full_request_url = self.url + method + urllib.parse.urlencode(args)
        # print(full_request_url)
        try:
            self.request_result = requests.get(url=full_request_url, timeout=self.cfg.timeout)
        except requests.ConnectionError:
            raise RequestConnectionErrorException('User not connected to the internet')
        except requests.Timeout:
            raise RequestTimeoutException(f'Request to {full_request_url} exceeded time limit of {self.cfg.timeout}s')
        except Exception:
            raise UndefinedAPIErrorException(f'Unknown error occured when requesting to {full_request_url}')

        self.handle_misc_errors()

        return self.request_to_json()
    
    def page_request(self, url: str) -> str:
        try:
            self.request_result = requests.get(url=url, timeout=self.cfg.timeout)
        except requests.ConnectionError:
            raise RequestConnectionErrorException('User not connected to the internet')
        except requests.Timeout:
            raise RequestTimeoutException(f'Request to {url} exceeded time limit of {self.cfg.timeout}s')
        except Exception:
            raise UndefinedAPIErrorException(f'Unknown error occured when requesting to {url}')
        
        return self.request_result.content