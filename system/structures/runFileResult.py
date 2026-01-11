class RunFileResult:
    def __init__(self, run_time, run_memory, run_returncode) -> None:
        self.time = round(run_time, 3)
        self.memory = run_memory
        self.returncode = run_returncode
