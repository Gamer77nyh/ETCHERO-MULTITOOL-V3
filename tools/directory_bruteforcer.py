import requests
from colorama import Fore, init

init(autoreset=True)

def main():
    print(f"\n{Fore.GREEN}--- Directory Bruteforcer ---")
    url = input(f"{Fore.YELLOW}Enter target URL (e.g., http://example.com): ")
    
    if not url:
        print(f"{Fore.RED}❌ URL cannot be empty.")
        return

    if not url.startswith("http"):
        url = "http://" + url
    
    if url.endswith("/"):
        url = url[:-1]

    # Common directory/file names
    wordlist = [
        "admin", "login", "wp-admin", "backup", "db", "api", "config", "test", 
        "dev", "shell", "phpmyadmin", "uploads", "images", "js", "css", 
        "robots.txt", ".env", ".git", ".htaccess", "index.php", "index.html"
    ]

    print(f"{Fore.CYAN}Bruteforcing directories/files for {url}...")
    found_count = 0
    
    for word in wordlist:
        target = f"{url}/{word}"
        try:
            response = requests.get(target, timeout=5)
            if response.status_code == 200:
                print(f"{Fore.GREEN}[+] Found: {Fore.WHITE}{target} (Status: 200)")
                found_count += 1
            elif response.status_code == 403:
                print(f"{Fore.YELLOW}[!] Forbidden: {Fore.WHITE}{target} (Status: 403)")
        except requests.exceptions.RequestException:
            pass
        except Exception as e:
            print(f"{Fore.RED}❌ Error checking {target}: {e}")

    print(f"\n{Fore.CYAN}Bruteforce complete. Found {found_count} items.")

if __name__ == "__main__":
    main()
