import sys
import os


def main():
    # TODO: Uncomment the code below to pass the first stage

    acceptable_paths = os.environ['PATH'].split(os.pathsep)
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
                match = next((s for s in acceptable_paths if command[5:] in s), None)
                if match and os.access(match, os.X_OK):
                    print(f"{command[5:]} is {match}")
                else:
                    print(f"{command[5:]}: not found")
        else:
            print(f"{command}: command not found")
    


if __name__ == "__main__":
    main()
