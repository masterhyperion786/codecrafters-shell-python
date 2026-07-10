import sys
import shutil
import subprocess
import os


def main():
    # TODO: Uncomment the code below to pass the first stage

    builtin_commands = ["exit", "echo", "type", "pwd", "cd"]

    while True:
        sys.stdout.write("$ ")
        command = input()
        input_commands = command.strip().split()

        if input_commands[0] == "exit":
            break
        elif input_commands[0] == "echo":
            print(" ".join(input_commands[1:]))
        elif input_commands[0] == "type":
            if input_commands[1] in builtin_commands:
                print(f"{input_commands[1]} is a shell builtin")
            elif shutil.which(input_commands[1]):
                print(f"{input_commands[1]} is {shutil.which(input_commands[1])}")
            else:
                print(f"{input_commands[1]}: not found")
        elif input_commands[0] == "pwd":
            print(os.getcwd())
        elif input_commands[0] == "cd":
            try:
                if input_commands[1] == "~":
                    os.chdir(os.path.expanduser("~"))
                else:
                    os.chdir(input_commands[1])
            except IndexError:
                print("cd: missing operand")
            except FileNotFoundError:
                print(f"cd: {input_commands[1]}: No such file or directory")
        else:
            if execute_program(input_commands) is None:
                print(f"{input_commands[0]}: command not found")

def execute_program(command):
    if shutil.which(command[0]):
        try:
            result = subprocess.run(command, check=True)
            return result.returncode
        except subprocess.CalledProcessError as e:
            print(f"Error executing {command[0]}: {e}")
            return e.returncode



if __name__ == "__main__":
    main()