import requests
from colorama import Fore, init

init(autoreset=True)

def check_spam_link(url):
    # This is a basic check using a public blacklist API (e.g., Google Safe Browsing or VirusTotal would be better but require API keys)
    # For this educational tool, we'll check redirects and basic reachability, and simulate a "reputation" check.
    
    if not url.startswith("http"):
        url = "http://" + url

    print(f"{Fore.CYAN}Checking {url}...")
    
    try:
        response = requests.get(url, timeout=5, allow_redirects=True)
        print(f"{Fore.GREEN}✅ Site is reachable (Status: {response.status_code})")
        
        if len(response.history) > 0:
            print(f"{Fore.YELLOW}⚠️  Redirects detected:")
            for resp in response.history:
                print(f"  -> {resp.url} ({resp.status_code})")
            print(f"  -> Final: {response.url}")
        
        # Simple heuristic check
        suspicious_keywords = ["free", "win", "prize", "login", "bank", "update", "verify"]
        if any(keyword in url.lower() for keyword in suspicious_keywords):
            print(f"\n{Fore.RED}⚠️  Warning: URL contains suspicious keywords!")
        else:
            print(f"\n{Fore.GREEN}✅ URL pattern looks clean.")
            
    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}❌ Could not reach site: {e}")

def main():
    print(f"\n{Fore.GREEN}--- Spam Link Tester ---")
    url = input(f"{Fore.YELLOW}Enter URL to test: ")
    
    if not url:
        print(f"{Fore.RED}❌ URL cannot be empty.")
        return

    check_spam_link(url)

if __name__ == "__main__":
    main()
