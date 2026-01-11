import subprocess, time, psutil, os, colorama

from copy import deepcopy
from exceptions import *
from system.config.runSettings import RunSettings
from system.structures.runFileResult import RunFileResult
from system.structures.buildResult import BuildResult


def kill(proc_pid) -> None:
    process = psutil.Process(proc_pid)
    for proc in process.children(recursive=True):
        proc.kill()
    process.kill()


def get_time(timeStart: float):
    return time.perf_counter() - timeStart


def get_memory(process: psutil.Process):
    RAM = process.memory_info().rss
    for child in process.children(recursive=True):
        RAM += child.memory_info().rss
    return RAM


def get_outfile_size(path_to_file: str):
    return os.path.getsize(path_to_file)

def format_err_lines(lines: list):
    result = colorama.Fore.RESET + colorama.Back.RESET
    for i in lines:
        result += i.decode('utf-8')
    return result


class FileRunner:
    def __init__(self, cfg: RunSettings, file_path: str) -> None:
        self.config = deepcopy(cfg)
        self.config.format_commands('$FILENAME', file_path)
        self.config.format_run_command()
        self.path_to_file = file_path

    def check_for_outfile_usage(self):
        return self.config.output_file_path != ''

    def build(self) -> BuildResult:
        buildCommand = f"{self.config.build_command} {self.config.build_args}"
        timeStart = time.perf_counter()
        with subprocess.Popen(buildCommand, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True) as proc:
            errors = proc.stdout.read().decode().splitlines()
            if self.config.buildErrorLines != 0:
                errors = errors[:self.config.buildErrorLines]
            timeEnd = time.perf_counter()
        if errors:
            return BuildResult(success=0, errors=errors, time=timeEnd - timeStart)
        return BuildResult(success=1, errors=[], time=timeEnd - timeStart)

    def get_run_command(self, unix: bool):
        runCommand = f"{self.config.run_command} {self.config.run_args}"
        unix_prefix = f"ulimit -s {10 * self.config.memory_limit} && ulimit -v {10 * self.config.memory_limit} && "
        if unix:
            runCommand = unix_prefix + runCommand
        return runCommand

    def run(self, unix: bool) -> RunFileResult:
        runCommand = self.get_run_command(unix=unix)
        proc = subprocess.Popen(runCommand, shell=True, stderr=subprocess.PIPE)
        currentTime, timeStart, MAX_RAM = 0, time.perf_counter(), 0
        while proc.poll() is None:
            currentTime = get_time(timeStart=timeStart)
            try:
                p = psutil.Process(proc.pid)
                MAX_RAM = max(MAX_RAM, get_memory(process=p))
                if self.config.memory_limit != 0 and MAX_RAM >= self.config.memory_limit * 1024:
                    kill(proc.pid)
                    raise MemoryLimitExceededException(f'Configured memory limit of {self.config.memory_limit}KB has been exceeded')
                if self.config.time_limit != 0.0 and currentTime > self.config.time_limit:
                    kill(proc.pid)
                    raise TimeLimitExceededException(f'Configured time limit of {self.config.time_limit}s has been exceeded')
                if self.check_for_outfile_usage() and get_outfile_size(self.config.output_file_path) >= self.config.output_file_size_limit * 1024:
                    kill(proc.pid)
                    raise OutputFileTooLargeException(f'Output file at {self.config.output_file_path} exceeded the configured limit of {self.config.output_file_size_limit}KB')
            except psutil.NoSuchProcess:
                break
            except KeyboardInterrupt:
                kill(proc.pid)
                raise KeyboardInterrupt
            time.sleep(self.config.runner_poll_time)
        if proc.poll() != 0:
            raise RuntimeErrorException(f'Caught a runtime error with code {proc.poll()}:{colorama.Fore.RESET + colorama.Back.RESET}\n{format_err_lines(proc.stderr.readlines())}')
        return RunFileResult(run_time=currentTime, run_memory=MAX_RAM, run_returncode=proc.poll())

    def cleanup(self):
        os.system(self.config.cleanup_command)