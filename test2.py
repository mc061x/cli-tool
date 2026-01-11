from config.generalCfg import GeneralConfig
from exceptions import *
from system.runFile import FileRunner
from colorama import Fore
import os


def format_command(command: str):
    formatted = command.split()
    formatted.remove('run')
    return formatted


def assure_file_exists(file_path: str):
    if os.path.exists(file_path):
        return
    raise FileNotFoundException(f'File {file_path} not found in the current directory')


def run_handle(cfg: GeneralConfig, command: str):
    formatted = format_command(command)

    path_to_file = formatted[0]

    try:
        assure_file_exists(path_to_file)
    except FileNotFoundException as exc:
        handle_exception(cfg.interfaceCfg.error, exc)
        return

    runner = FileRunner(cfg=cfg.runCfg.currentRunOption, file_path=path_to_file)

    if cfg.runCfg.currentRunOption.build_command + cfg.runCfg.currentRunOption.build_args != '':
        buildResult = runner.build()
        if not buildResult.success:
            print(cfg.interfaceCfg.error('Build failed :('))
            buildResult.errors = buildResult.errors[:10]
            for i in buildResult.errors:
                print(i)
            return

        print(cfg.interfaceCfg.success(f'Build finished successfully in {buildResult.time}s'))

    try:
        runResult = runner.run(cfg.unix)
    except TimeLimitExceededException as exc:
        handle_exception(cfg.interfaceCfg.error, exc)
        return
    except MemoryLimitExceededException as exc:
        handle_exception(cfg.interfaceCfg.error, exc)
        return
    except RuntimeErrorException as exc:
        handle_exception(cfg.interfaceCfg.error, exc)
        return

    print(cfg.interfaceCfg.success(f'\nRun finished successfully with code {runResult.returncode}'))
    print(cfg.interfaceCfg.system(f'Time : {runResult.time}s | Memory : {runResult.memory / 1024}KB'))
    runner.cleanup()


cfg = GeneralConfig()
# cfg.runCfg.modify_run_config('main', 'build_command', '')
# cfg.runCfg.modify_run_config('main', 'build_args', '')
# cfg.runCfg.modify_run_config('main', 'run_command', 'python3 $FILENAME')
cfg.runCfg.modify_run_config('main', 'output_file_path', 'logs/log.txt')
# cfg.runCfg.modify_run_config('main', 'cleanup_command', '')

# cfg.interfaceCfg.change_attribute('text_background', colorama.Back.BLACK)

while True:
    print(cfg.interfaceCfg.text_color + cfg.interfaceCfg.text_background, end='')
    a = input(f'{colorama.Fore.BLACK}1{colorama.Fore.RESET + colorama.Fore.RED}60cm{colorama.Fore.RESET}> ').strip()
    print(colorama.Fore.RESET + colorama.Back.RESET, end='')
    if a == 'quit':
        break
    run_handle(cfg, a)

