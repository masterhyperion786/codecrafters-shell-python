import sys
import os


def main():
    # TODO: Uncomment the code below to pass the first stage

    acceptable_paths = os.environ.get("PATH", "").split(os.pathsep)
    
    while True:
        sys.stdout.write("$ ")
        command = input()
        if command == "exit":
            break
        elif command.startswith("echo "):
            print(command[5:])
        elif command.startswith("type "):
            if command[5:] in ["exit", "echo", "type"]:
                print(f"{command[5:]} is a shell builtin")
            else:
                match = find_executable(command[5:], acceptable_paths)
                if match:
                    print(f"{command[5:]} is {match}")
                else:
                    print(f"{command[5:]}: not found")
        else:
            print(f"{command}: command not found")
    
def find_executable(command, paths):
    for path in paths:
        executable_path = os.path.join(path, command)
        if os.path.isfile(executable_path) and os.access(executable_path, os.X_OK):
            return executable_path
    return None

if __name__ == "__main__":
    main()