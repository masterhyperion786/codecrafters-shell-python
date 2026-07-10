import sys


def main():
    # TODO: Uncomment the code below to pass the first stage
    sys.stdout.write("$ ")
    sys.stdout.flush()
    command = sys.stdin.readline().strip()
    sys.stdout.write(f"{command}: command not found\n")

    pass
    


if __name__ == "__main__":
    main()
