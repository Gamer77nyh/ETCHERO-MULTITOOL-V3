import whois
from colorama import Fore, init

init(autoreset=True)

def main():
    print(f"\n{Fore.GREEN}--- Whois Lookup ---")
    domain = input(f"{Fore.YELLOW}Enter domain (e.g., google.com): ")
    
    if not domain:
        print(f"{Fore.RED}❌ Domain cannot be empty.")
        return

    print(f"{Fore.CYAN}Fetching Whois information...")
    try:
        w = whois.whois(domain)
        print(f"\n{Fore.GREEN}✅ Results for {domain}:")
        print(f"{Fore.CYAN}Domain Name: {Fore.WHITE}{w.domain_name}")
        print(f"{Fore.CYAN}Registrar: {Fore.WHITE}{w.registrar}")
        print(f"{Fore.CYAN}Creation Date: {Fore.WHITE}{w.creation_date}")
        print(f"{Fore.CYAN}Expiration Date: {Fore.WHITE}{w.expiration_date}")
        print(f"{Fore.CYAN}Updated Date: {Fore.WHITE}{w.updated_date}")
        print(f"{Fore.CYAN}Name Servers: {Fore.WHITE}{w.name_servers}")
        print(f"{Fore.CYAN}Status: {Fore.WHITE}{w.status}")
        print(f"{Fore.CYAN}Emails: {Fore.WHITE}{w.emails}")
        print(f"{Fore.CYAN}Country: {Fore.WHITE}{w.country}")
    except Exception as e:
        print(f"{Fore.RED}❌ Error: {e}")

if __name__ == "__main__":
    main()
