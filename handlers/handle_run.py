from codeforces.structures.problemData import ProblemData
from exceptions import *
from config.generalCfg import GeneralConfig
from system.runFile import FileRunner
from system.structures.flag import Flag, FlagParser
from config.runCfg import check_for_alias, find_option
from copy import deepcopy
import os

run_flags = [Flag('-s', 0), Flag('-c', 1)]

sample_input_file = './tool-data/input.in'
sample_output_file = './tool-data/output.out'

def assure_file_exists(file_path: str):
    if os.path.exists(file_path):
        return
    raise FileNotFoundException(f'File {file_path} not found in the current directory')

def format_command(command: str):
    formatted = command.split()
    formatted.remove('run')
    return formatted

class RunHandler:
    def __init__(self, cfg: GeneralConfig) -> None:
        self.cfg = cfg
        self.parser = FlagParser(run_flags)
        self.samples = False
        self.option = cfg.runCfg.currentRunOption

    def handle(self, command: list):
        try:
            command = self.parser.parse_command(command)
        except IndexError as exc:
            handle_exception(self.cfg.interfaceCfg.error, exc)
            return
        
        current_option = deepcopy(self.option)

        flag: Flag
        for flag in self.parser.arg_list:
            if flag.name == '-s' and flag.present:
                self.samples = True
            if flag.name == '-c' and flag.present:
                alias = flag.arg_list[0]
                try:
                    check_for_alias(alias, self.cfg.runCfg.runOptionList)
                except ConfigNotFoundException as exc:
                    handle_exception(self.cfg.interfaceCfg.error, exc)
                    return
                current_option = deepcopy(find_option(alias, self.cfg.runCfg.runOptionList).option)
                
        if self.samples == True:
            current_option.input_file_path = sample_input_file
            current_option.output_file_path = sample_output_file

        command = command[1:]
        path_to_file = os.path.join(self.cfg.directory, command[0])
        

        try:
            assure_file_exists(path_to_file)
        except FileNotFoundException as exc:
            handle_exception(self.cfg.interfaceCfg.error, exc)
            return

        runner = FileRunner(cfg=current_option, file_path=path_to_file)

        if current_option.build_command + current_option.build_args != '':
            buildResult = runner.build()
            if not buildResult.success:
                print(self.cfg.interfaceCfg.error('Build failed :('))
                buildResult.errors = buildResult.errors[:current_option.buildErrorLines]
                for i in buildResult.errors:
                    print(i)
                return

            print(self.cfg.interfaceCfg.success(f'Build finished successfully in {buildResult.time}s'))
        
        if self.samples == False:
            try:
                runResult = runner.run(self.cfg.unix)
            except TimeLimitExceededException as exc:
                handle_exception(self.cfg.interfaceCfg.error, exc)
                runner.cleanup()
                return
            except MemoryLimitExceededException as exc:
                handle_exception(self.cfg.interfaceCfg.error, exc)
                runner.cleanup()
                return
            except RuntimeErrorException as exc:
                handle_exception(self.cfg.interfaceCfg.error, exc)
                runner.cleanup()
                return
            except OutputFileTooLargeException as exc:
                handle_exception(self.cfg.interfaceCfg.error, exc)
                runner.cleanup()
                return

            print(self.cfg.interfaceCfg.success(f'Run finished successfully with code {runResult.returncode}'))
            print(self.cfg.interfaceCfg.system(f'Time : {runResult.time}s | Memory : {runResult.memory / 1024}KB'))
            
            runner.cleanup()
        
        if self.samples == True:
            current_contest = self.cfg.cfConfig.current_contest

            samples_index = current_contest.problem_list.index(current_contest.current_problem_index)

            samples : ProblemData = current_contest.problem_data.list[samples_index]
            for index, sample in enumerate(samples.input):
                print(60 * '-')
                print(self.cfg.interfaceCfg.system(f'Sample №{index + 1}'), end='\n\n')
                infile = open(sample_input_file, 'w')
                infile.write(sample)
                infile.close()
                try:
                    runResult = runner.run(self.cfg.unix)
                except TimeLimitExceededException as exc:
                    handle_exception(self.cfg.interfaceCfg.error, exc)
                    continue
                except MemoryLimitExceededException as exc:
                    handle_exception(self.cfg.interfaceCfg.error, exc)
                    continue
                except RuntimeErrorException as exc:
                    handle_exception(self.cfg.interfaceCfg.error, exc)
                    continue
                except OutputFileTooLargeException as exc:
                    handle_exception(self.cfg.interfaceCfg.error, exc)
                    continue
                outfile = open(sample_output_file, 'r')
                expected = '\n'.join(samples.output[index])
                got = [line.strip() for line in outfile.readlines()]

                width = max(len(line) for line in got)
                
                print(self.cfg.interfaceCfg.warning('Expected output:' + '\n' + expected))
                print(self.cfg.interfaceCfg.success(f'Your output:'))
                for line_index, line in enumerate(got):
                    print(line, end=' ' * (width - len(line) + 4))
                    if line_index < len(samples.output[index]) and got[line_index] != samples.output[index][line_index]:
                        print(self.cfg.interfaceCfg.error(' | Mismatch!'))
                    elif line_index < len(samples.output[index]):
                        print(self.cfg.interfaceCfg.success(' | Match!'))
                    else:
                        print()
                    
                outfile.close()
                print()

                print(self.cfg.interfaceCfg.success(f'Run finished successfully with code {runResult.returncode}'))
                print(self.cfg.interfaceCfg.system(f'Time : {runResult.time}s | Memory : {runResult.memory / 1024}KB'))
            print(60 * '-')
            runner.cleanup()
                