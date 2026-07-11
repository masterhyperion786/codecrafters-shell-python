import sys
import shutil
import shlex
import subprocess
import os

def cmd_exit(args):
    sys.exit(int(args[0]) if args else 0)

def cmd_echo(args):
    print(" ".join(args))

def cmd_type(args):
    if args[0] in ["exit", "echo", "type", "pwd", "cd"]:
        print(f"{args[0]} is a shell builtin")
    elif shutil.which(args[0]):
        print(f"{args[0]} is {shutil.which(args[0])}")
    else:
        print(f"{args[0]}: not found")

def cmd_pwd(args):
    print(os.getcwd())

def cmd_cd(args):
    try:
        if args and args[0] == "~":
            os.chdir(os.path.expanduser("~"))
        elif args:
            os.chdir(args[0])
        else:
            print("cd: missing operand")
    except FileNotFoundError:
        print(f"cd: {args[0]}: No such file or directory")

def redirect_output_to_file(command, filename):
    try:
        with open(filename, 'w') as f:
            result = subprocess.run(command, stdout=f, stderr=subprocess.PIPE)
            if result.returncode != 0:
                print(f"{result.stderr.decode()}")
    except Exception as e:
        print(f"Error redirecting output: {e}")

def execute_program(command):
    if shutil.which(command[0]):
        try:
            result = subprocess.run(command, check=True)
            return result.returncode
        except subprocess.CalledProcessError as e:
            print(f"Error executing {command[0]}: {e}")
            return e.returncode
    

BUILTIN_COMMANDS = {
    "exit": cmd_exit,
    "echo": cmd_echo,
    "type": cmd_type,
    "pwd": cmd_pwd,
    "cd": cmd_cd
}

OPERATORS = {
    '>': "redirect_output_to_file",
    '1>': "redirect_output_to_file",
}

def main():
    # TODO: Uncomment the code below to pass the first stage
    while True:
        try:
            command_input = input("$ ")
            if not command_input.strip():
                continue
            shlexed_input = shlex.split(command_input)
            command_parts = shlexed_input

            command_name = command_parts[0]
            command_args = command_parts[1:]

            if len(command_parts) > 1 and any([i in command_parts for i in OPERATORS.keys()]):
                redirect_output_to_file([command_name] + command_args[:-2], command_args[-1])
            elif command_name in BUILTIN_COMMANDS:
                BUILTIN_COMMANDS[command_name](command_args)
            elif execute_program([command_name] + command_args) is None:
                print(f"{command_name}: command not found")
        except EOFError:
            print("\nExiting shell.")
            break
        except KeyboardInterrupt:
            print("\nUse 'exit' to quit the shell.")

if __name__ == "__main__":
    main()