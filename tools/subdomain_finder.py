import socket
from colorama import Fore, init

init(autoreset=True)

def main():
    print(f"\n{Fore.GREEN}--- Subdomain Finder ---")
    domain = input(f"{Fore.YELLOW}Enter target domain (e.g., example.com): ")
    
    if not domain:
        print(f"{Fore.RED}❌ Domain cannot be empty.")
        return

    # A small list of common subdomains
    subdomains = [
        "www", "mail", "ftp", "localhost", "webmail", "smtp", "pop", "ns1", "webdisk", 
        "ns2", "cpanel", "whm", "autodiscover", "autoconfig", "m", "dev", "test", 
        "stage", "api", "blog", "shop", "admin", "vpn", "portal", "cloud"
    ]

    print(f"{Fore.CYAN}Scanning common subdomains for {domain}...")
    found_count = 0
    
    for sub in subdomains:
        target = f"{sub}.{domain}"
        try:
            ip = socket.gethostbyname(target)
            print(f"{Fore.GREEN}[+] Found: {Fore.WHITE}{target} ({ip})")
            found_count += 1
        except socket.gaierror:
            pass
        except Exception as e:
            print(f"{Fore.RED}❌ Error checking {target}: {e}")

    print(f"\n{Fore.CYAN}Scan complete. Found {found_count} subdomains.")

if __name__ == "__main__":
    main()
