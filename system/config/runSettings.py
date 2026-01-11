from system.structures.configStruct import ConfigStruct


class RunSettings(ConfigStruct):
    def __init__(self) -> None:
        super().__init__()
        self.buildErrorLines = 10
        self.time_limit = 2.0
        self.memory_limit = 256 * 1024
        self.output_file_size_limit = 16 * 1024
        self.input_file_path = ''
        self.output_file_path = ''

        self.build_command = f'g++ $FILENAME'
        self.build_args = '-std=c++20 -fdiagnostics-color=always -fmax-errors=2 -o $FILENAME.out'

        self.run_command = f'/$FILENAME.out'
        self.run_args = ''

        self.cleanup_command = f'rm $FILENAME.out'

        self.runner_poll_time = 0.05
    
    def format_commands(self, pattern_old: str, pattern_new: str) -> None:
        old_dict: dict = self.__dict__
        for key in old_dict:
            old_instance: str = getattr(self, key)
            if type(old_instance) != str:
                continue
            setattr(self, key, old_instance.replace(pattern_old, pattern_new))
    
    def format_run_command(self):
        if self.input_file_path != '':
            self.run_command += f'< {self.input_file_path}'
        if self.output_file_path != '':
            self.run_command += f'> {self.output_file_path}'
