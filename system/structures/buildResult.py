class BuildResult:
    def __init__(self, success: int, errors: list, time: float):
        self.success = success
        self.errors = errors
        self.time = round(time, 3)
