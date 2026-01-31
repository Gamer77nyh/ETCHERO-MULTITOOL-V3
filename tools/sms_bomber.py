import requests
import time
from colorama import Fore, init

init(autoreset=True)

def main():
    print(f"\n{Fore.GREEN}--- SMS API Tester ---")
    print(f"{Fore.CYAN}Note: This tool is for testing YOUR OWN SMS APIs only.")
    print(f"{Fore.CYAN}It allows you to stress test an endpoint you control.")
    
    url = input(f"{Fore.YELLOW}Enter your SMS API Endpoint URL: ")
    method = input(f"{Fore.YELLOW}Method (GET/POST): ").upper()
    count = input(f"{Fore.YELLOW}Number of requests to send: ")
    
    try:
        count = int(count)
    except ValueError:
        print(f"{Fore.RED}❌ Invalid number.")
        return

    if not url.startswith("http"):
        print(f"{Fore.RED}❌ Invalid URL.")
        return

    print(f"\n{Fore.CYAN}Starting test on {url}...")
    
    success = 0
    failed = 0
    
    for i in range(count):
        try:
            if method == "POST":
                # Assuming a generic payload structure, user would typically customize this
                response = requests.post(url, data={"test": "data"}, timeout=5)
            else:
                response = requests.get(url, timeout=5)
            
            if response.status_code == 200:
                print(f"{Fore.GREEN}[+] Request {i+1}/{count} Success")
                success += 1
            else:
                print(f"{Fore.YELLOW}[!] Request {i+1}/{count} Failed (Status: {response.status_code})")
                failed += 1
        except Exception as e:
            print(f"{Fore.RED}[-] Request {i+1}/{count} Error: {e}")
            failed += 1
        
        time.sleep(0.5) # Slight delay to avoid instant IP ban on most test services

    print(f"\n{Fore.GREEN}--- Test Complete ---")
    print(f"{Fore.CYAN}Successful: {Fore.WHITE}{success}")
    print(f"{Fore.RED}Failed: {Fore.WHITE}{failed}")

if __name__ == "__main__":
    main()
