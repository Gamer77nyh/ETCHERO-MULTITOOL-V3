import re
import dns.resolver
from colorama import Fore, init

init(autoreset=True)

def is_valid_syntax(email):
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(regex, email)

def get_mx_record(domain):
    try:
        records = dns.resolver.resolve(domain, 'MX')
        mx_record = str(records[0].exchange)
        return mx_record
    except Exception:
        return None

def main():
    print(f"\n{Fore.GREEN}--- Email Verifier ---")
    email = input(f"{Fore.YELLOW}Enter email address to verify: ")
    
    if not email:
        print(f"{Fore.RED}❌ Email cannot be empty.")
        return

    print(f"{Fore.CYAN}Checking syntax...")
    if not is_valid_syntax(email):
        print(f"{Fore.RED}❌ Invalid email format.")
        return
    print(f"{Fore.GREEN}✅ Syntax is valid.")

    domain = email.split('@')[1]
    print(f"{Fore.CYAN}Checking MX records for {domain}...")
    
    mx_record = get_mx_record(domain)
    if mx_record:
        print(f"{Fore.GREEN}✅ Domain has valid MX records: {Fore.WHITE}{mx_record}")
        print(f"\n{Fore.GREEN}✅ The email address is likely valid.")
    else:
        print(f"{Fore.RED}❌ No MX records found. Domain may not handle email.")

if __name__ == "__main__":
    main()
