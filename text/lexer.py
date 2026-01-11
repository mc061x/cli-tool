from typing import Callable
from prompt_toolkit.document import Document
from prompt_toolkit.formatted_text.base import StyleAndTextTuples
from prompt_toolkit.lexers import Lexer
from text.command_list import *
from config.generalCfg import GeneralConfig
from re import finditer

import os

class LexerWrapper:
    def __init__(self, cfg: GeneralConfig) -> None:
        self.cfg = cfg

    def color_commands(self, current_command: str, cols: list):
        for command in COMMAND_LIST:
            occurences = [m.start() for m in finditer(command, current_command)]
            for occ in occurences:
                for j in range(len(command)):
                    cols[occ+j] = self.cfg.interfaceCfg.command_color

    def color_files(self, current_command: str, cols: list):
        files_in_command = list()
        for j in current_command.split():
            current_path = os.path.join(self.cfg.directory, j)
            if os.path.exists(current_path) and os.path.isfile(current_path):
                files_in_command.append(j)
        for file in files_in_command:
            occurences = [m.start() for m in finditer(file, current_command)]
            for occ in occurences:
                for j in range(len(file)):
                    cols[occ+j] = self.cfg.interfaceCfg.file_color
    
    def color_flags(self, current_command: str, cols: list):
        for flag in FLAG_LIST:
            occurences = [m.start() for m in finditer(flag, current_command)]
            for occ in occurences:
                for j in range(len(flag)):
                    cols[occ+j] = self.cfg.interfaceCfg.flag_color

    def get_colors(self, current_command: str):
        length = len(current_command)
        cols = [self.cfg.interfaceCfg.regular_color] * length
        self.color_commands(current_command=current_command, cols=cols)
        self.color_flags(current_command=current_command, cols=cols)
        if self.cfg.interfaceCfg.highlight_files:
            self.color_files(current_command=current_command, cols=cols)
        return cols

class MyLexer(Lexer):
    def __init__(self, wrapper: LexerWrapper) -> None:
        super().__init__()
        self.wrapper = wrapper

    def lex_document(self, document: Document) -> Callable[[int], StyleAndTextTuples]:
        
        def get_line(lineno):
            res = []

            command = document.lines[lineno]
            colors = self.wrapper.get_colors(command)
            for char, col in zip(command, colors):
                res.append((col, char))    
            return res
        
        return get_line
