import subprocess
import pyfiglet as pyg
from colorama import init, Fore

def execute_program(program_name):
    try:
        subprocess.run(["python", program_name], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing {program_name}: {e}")

def main():
    res = pyg.figlet_format("Excy", font="speed")
    print()
    print(f"{Fore.CYAN}{res}")
    print("1. Remove Duplicates")
    print("2. Search and Save Results")

    user_choice = input("Enter your choice (1 or 2): ")

    if user_choice == "1":
        execute_program("modules/remove-dups.py")
    elif user_choice == "2":
        execute_program("modules/search-and-save.py")
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
