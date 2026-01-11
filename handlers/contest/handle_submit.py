from config.generalCfg import GeneralConfig
from exceptions import *
import os, webbrowser, pyperclip

def assure_file_exists(file_path: str):
    if os.path.exists(file_path):
        return
    raise FileNotFoundException(f'File {file_path} not found in the current directory')

class ContestSubmitHandler:
    def __init__(self, cfg: GeneralConfig) -> None:
        self.cfg = cfg

    def handle(self, command: str):
        command = command[1:]
        if len(command) == 0:
            handle_exception(self.cfg.interfaceCfg.error, RuntimeError('File is not specified'))
            return
        if len(command) > 1:
            handle_exception(self.cfg.interfaceCfg.error, RuntimeError('Too many parameters'))
            return
        contest_id = self.cfg.cfConfig.current_contest.contest_id
        contest_problem_id = self.cfg.cfConfig.current_contest.current_problem_index
        try:
            f = open(command[0], 'r')
        except:
            handle_exception(self.cfg.interfaceCfg.error, FileNotFoundError(f'File {command[0]} not found'))
            return
        webbrowser.open(f'https://codeforces.com/contest/{contest_id}/submit/{contest_problem_id}')
        pyperclip.copy(f.read())