# Codeforces Contest Helper 
## Features

- **Interactive shell** with syntax highlighting and autocompletion
- **Contest mode** 
	- use ```contest join <id>``` to join a contest and download vital contest data like problem indices, sample inputs/outputs and more.
	- use ```contest nxt```, ```contest prev```, or simply ```contest prob <idx>``` to move between problems.
	- use ```contest submit <file>``` to quickly open the submit page and have the file copied into your buffer.
- **Runner**
	- ```run <file>``` builds and runs your solution using the **highly customizable run config**.
	- **Enforces** things like time limit, memory limit, and output file size limit so that your code **never** crashes!
	- use ```run -s <file>``` to run your solutions on all samples of the selected contest problem and display per-line match/mismatch.

## Configuration

In order to change your configuration, use ```cfg <configuration> edit```, then follow instructions displayed in the console

There are two configuration types:
1. **General**
	1. use ```cfg gen print``` to display the general configuration.
	2. use ```cfg gen edit``` followed by the index of the option that you want modified.
	As it stands, the only option to modify is the ```directory``` in which your solution files are based in.
2. **Run**
	1. use ```cfg run print``` to display the alias of your current run configuration.
	2. use ```cfg run edit``` followed by the alias of the configuration that you want to edit. Additionally, you can type ```cfg run edit -a <alias>``` to avoid the extra steps.
	3. use ```cfg run print -a <alias>``` to print all of the options of a single configuration.
	4. use ```cfg run print -all``` to print all of the options of all of the configurations.
	5. use ```cfg run print -cur``` to print all of the options of your current selected configuration.
	6. use ```cfg run sel <alias>``` to select a new run configuration. 
	7. use ```cfg run add <new_alias>``` to create a new configuration. Since there are a lot of options that may be annoying to redeclare over and over, you can use ```cfg run add <new_alias> -from <existing_alias>``` to create a new configuration and copy all of the options from an existing one.
	8. use ```cfg run rm -a <alias>``` to remove an existing configuration.

In the **Run** configurations, there is a variety of settings you can tweak to fit your personal workflow:
1. ```buildErrorLines <int>```--the amount of lines displayed when catching build error. If you compile with warnings, you may see over 1000 lines of them with certain compilation flags, and if you prefer not to flood your console with them, you can customize this setting to avoid that problem.
2. ```time_limit <float>```--the amount of seconds that your program is allowed to run for before terminating. This does not include the build time, and you can set the number to $0$ if you don't want any time restrictions.
3. ```memory_limit <int>```--the amount of kilobytes of RAM that your program is allowed to consume before terminating. Similarly, you can set the limit to $0$ if you don't want one.
4. ```output_file_size_limit <int>```--the maximal size of the output file in kilobytes. If while running the output file starts growing larger than this limit, it is going to terminate. This is introduced to prevent code editor freezing/crashing when processing a large amount of text. Similarly, set it to $0$ if you don't want this limitation.
5. ```build_command <str>```--the command used to build your file (without the compilation flags). For C++ it would be ```g++ $FILENAME```, where `$FILENAME` is a built-in placeholder for the file path. For Python, you would leave it blank.
6. ```build_args <str>```--the arguments(compilation flags) used to compile your program. For C++ it can look something like ```-std=c++20 -fmax-errors=2 -o $FILENAME.out```.
7. ```run_command <str>```--the command used to run your file. For C++ it may look like ```/$FILENAME.out```, for Python it may look like ```python3 $FILENAME```.
8. ```run_args```--the arguments used to run your program. Do **NOT** use I/O redirection here, as it is already handled by the tool.
9. ```cleanup_command <str>```--the command used after your program terminates. Can be used to remove the files created during compilation, for example. It may look something like ```rm $FILENAME.out```.
10. ```runner_poll_time <float>```--the time in seconds between polls that the tool uses to enforce mentioned limits. If you are running on a CPU with few cores, it is recommended to set it to $0.05$ or above. Otherwise you may opt on something around $0.01$ or lower.
11. ```input_file_path <str>```--the full path to your input file. Leave blank if you don't want to use one.
12. ```output_file_path <str>```--the full path to your output file. Leave blank if you don't want to use one, or want to run interactive problems on this configuration. Note that the "Time limit" setting would still apply even when awaiting user input.

If you don't feel like switching between configs to run your file, you can use ```run <file> -c <config_alias>``` to run your solution using a different configuration without switching!
