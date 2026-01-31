import requests
from colorama import Fore, init

init(autoreset=True)

CURRENT_VERSION = "3.0"
REPO_URL = "https://api.github.com/repos/DTwinz/MEXICAN-MULTITOOL-V3/releases/latest" # Example URL

def check_update():
    print(f"\n{Fore.GREEN}--- Update Checker ---")
    print(f"{Fore.CYAN}Current Version: {Fore.WHITE}v{CURRENT_VERSION}")
    print(f"{Fore.CYAN}Checking for updates...")
    
    try:
        # In a real scenario, this would check a valid GitHub repo or a version file on a server
        # For now, we simulate the check.
        
        # response = requests.get(REPO_URL, timeout=5)
        # latest_version = response.json()["tag_name"]
        
        # Simulating no update for now as the repo doesn't exist yet
        latest_version = "3.0" 
        
        if latest_version > CURRENT_VERSION:
            print(f"\n{Fore.GREEN}✅ New version available: v{latest_version}")
            print(f"{Fore.WHITE}Please download it from the official repository.")
        else:
            print(f"\n{Fore.GREEN}✅ You are using the latest version.")
            
    except Exception as e:
        print(f"{Fore.RED}❌ Failed to check for updates: {e}")

def main():
    check_update()

if __name__ == "__main__":
    main()
