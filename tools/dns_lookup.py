import socket
from colorama import Fore, init

init(autoreset=True)

def dns_lookup(domain):
    try:
        ip = socket.gethostbyname(domain)
        print(f"\n{Fore.GREEN}✅ IP address for {domain}: {Fore.WHITE}{ip}")
    except socket.gaierror:
        print(f"{Fore.RED}❌ Could not resolve domain.")
    except Exception as e:
        print(f"{Fore.RED}❌ Error: {e}")

def main():
    print(f"\n{Fore.GREEN}--- DNS Lookup ---")
    domain = input(f"{Fore.YELLOW}Enter domain (e.g., google.com): ")
    print(f"{Fore.CYAN}Resolving...")
    dns_lookup(domain)

if __name__ == "__main__":
    main()
