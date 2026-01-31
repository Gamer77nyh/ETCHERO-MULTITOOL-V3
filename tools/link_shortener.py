import requests
from colorama import Fore, init

init(autoreset=True)

def shorten_link(url):
    try:
        api_url = f"http://tinyurl.com/api-create.php?url={url}"
        response = requests.get(api_url)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except Exception as e:
        print(f"{Fore.RED}Error: {e}")
        return None

def main():
    print(f"\n{Fore.GREEN}--- Link Shortener ---")
    url = input(f"{Fore.YELLOW}Enter the URL to shorten: ")
    
    if not url.startswith("http"):
        print(f"{Fore.RED}Invalid URL. Please include http:// or https://")
        return

    print(f"{Fore.CYAN}Shortening...")
    short_url = shorten_link(url)
    
    if short_url:
        print(f"\n{Fore.GREEN}✅ Shortened URL: {Fore.WHITE}{short_url}")
    else:
        print(f"{Fore.RED}❌ Failed to shorten URL.")

if __name__ == "__main__":
    main()
