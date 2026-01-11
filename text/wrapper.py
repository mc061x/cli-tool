from text.bindings import add_autocomplete_binding
from text.command_list import COMMAND_LIST
from text.lexer import LexerWrapper, MyLexer
from text.suggestor import MySuggsetor
import colorama

BOLD = '\033[1m'
RESET_BOLD = '\033[0m'

from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit import PromptSession, ANSI

from config.generalCfg import GeneralConfig

class TextWrapper:
    def __init__(self, cfg: GeneralConfig) -> None:
        self.cfg = cfg

        self.bindings = KeyBindings()
        add_autocomplete_binding(self.bindings)
    
        self.lexerWrapper = LexerWrapper(cfg)
        self.lexer = MyLexer(self.lexerWrapper)

        self.suggestor = MySuggsetor(COMMAND_LIST)
        
        self.session = PromptSession(
            auto_suggest=self.suggestor,
            key_bindings=self.bindings,
            lexer=self.lexer
        )

        self.prompt = str()

    def get_prompt(self):
        self.cfg.cfConfig.handle = '160cm'

        self.prompt = BOLD + self.cfg.interfaceCfg.system('$') + self.cfg.interfaceCfg.system(self.cfg.cfConfig.handle)
        if self.cfg.cfConfig.current_contest.contest_id != '':
            self.prompt += f'@{self.cfg.cfConfig.current_contest.contest_id}{self.cfg.cfConfig.current_contest.current_problem_index}'
        self.prompt += '> '
        self.prompt += RESET_BOLD
        return self.prompt

    def get_command(self):
        text = self.session.prompt(ANSI(self.get_prompt()), lexer=self.lexer)
        return text
    