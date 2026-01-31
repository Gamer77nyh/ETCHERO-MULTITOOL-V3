import time
import random
from colorama import Fore, init

init(autoreset=True)

def fake_scan():
    print(f"\n{Fore.GREEN}--- System Virus Scanner ---")
    print(f"{Fore.CYAN}Initializing database...")
    time.sleep(2)
    
    print(f"{Fore.CYAN}Scanning system files...")
    files = ["System32", "Windows/Boot", "Program Files", "Users/Data", "Registry/Keys", "Network/Config"]
    
    for _ in range(20):
        file = random.choice(files) + "/" + "".join(random.choices("abcdef123456", k=8)) + ".dll"
        print(f"{Fore.WHITE}Scanning: {file}")
        time.sleep(random.uniform(0.1, 0.5))

    print(f"\n{Fore.YELLOW}⚠️  Suspicious activity detected!")
    time.sleep(1)
    print(f"{Fore.RED}❌ VIRUS FOUND: Trojan.Win32.Generic")
    print(f"{Fore.RED}❌ VIRUS FOUND: Malware.Ransom.WannaCry")
    time.sleep(2)
    
    print(f"\n{Fore.CYAN}Attempting to quarantine...")
    time.sleep(3)
    
    if random.choice([True, False]):
        print(f"{Fore.GREEN}✅ Threats successfully removed!")
    else:
        print(f"{Fore.RED}❌ CRITICAL ERROR: Unable to delete virus. System compromise imminent!")

    print(f"\n{Fore.WHITE}Scan finished.")

def main():
    fake_scan()

if __name__ == "__main__":
    main()
