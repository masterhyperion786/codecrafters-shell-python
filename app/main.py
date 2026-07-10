import os
import sys
import shutil


def main():
    # TODO: Uncomment the code below to pass the first stage

    builtin_commands = ["exit", "echo", "type"]

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
        else:
            print(f"{input_commands[0]}: command not found")
    
def find_executable(command, paths):
    for path in paths:
        executable_path = os.path.join(path, command)
        if os.path.isfile(executable_path) and os.access(executable_path, os.X_OK):
            return executable_path
    return None

if __name__ == "__main__":
    main()