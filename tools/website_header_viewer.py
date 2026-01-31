import requests
from colorama import Fore, init

init(autoreset=True)

def view_headers(url):
    if not url.startswith("http"):
        url = "http://" + url
    try:
        response = requests.get(url)
        print(f"\n{Fore.GREEN}--- Headers for {url} ---")
        for header, value in response.headers.items():
            print(f"{Fore.CYAN}{header}: {Fore.WHITE}{value}")
    except Exception as e:
        print(f"{Fore.RED}❌ Failed to retrieve headers: {e}")

def main():
    print(f"\n{Fore.GREEN}--- Website Header Viewer ---")
    url = input(f"{Fore.YELLOW}Enter website URL (e.g., google.com): ")
    print(f"{Fore.CYAN}Retrieving headers...")
    view_headers(url)

if __name__ == "__main__":
    main()
