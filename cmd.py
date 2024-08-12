import os
import subprocess

def main():
    while True:
        current_dir = os.getcwd()
        command = input(f"{current_dir}> ")

        # Check for special commands
        if command == "exit":
            break
        elif command.startswith("cd"):
            try:
                new_dir = command.split(" ")[1] if len(command.split(" ")) > 1 else os.path.expanduser("~")
                os.chdir(new_dir)
            except OSError as e:
                print(f"Error changing directory: {e}")
        else:
            try:
                # Use subprocess for better control and security
                subprocess.run(command, shell=True, check=True)
            except subprocess.CalledProcessError as e:
                print(f"Error executing command: {e}")

if __name__ == "__main__":
    main()
