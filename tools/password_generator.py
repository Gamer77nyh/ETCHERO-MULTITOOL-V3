import random
import string
from colorama import Fore, init

init(autoreset=True)

def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print(f"\n{Fore.GREEN}--- Password Generator ---")
    try:
        length = int(input(f"{Fore.YELLOW}Enter password length: "))
        use_digits = input(f"{Fore.YELLOW}Include numbers? (y/n): ").lower() == 'y'
        use_special = input(f"{Fore.YELLOW}Include special characters? (y/n): ").lower() == 'y'
        
        password = generate_password(length, use_digits, use_special)
        print(f"\n{Fore.GREEN}✅ Generated Password: {Fore.WHITE}{password}")
    except ValueError:
        print(f"{Fore.RED}Invalid input. Please enter a number for length.")

if __name__ == "__main__":
    main()
