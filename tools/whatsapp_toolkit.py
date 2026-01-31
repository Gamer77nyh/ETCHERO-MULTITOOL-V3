import webbrowser
from colorama import Fore, init
import urllib.parse

init(autoreset=True)

def main():
    print(f"\n{Fore.GREEN}--- WhatsApp Toolkit ---")
    print(f"{Fore.CYAN}Generate and open direct WhatsApp message links.")
    
    phone = input(f"{Fore.YELLOW}Enter Phone Number (with country code, e.g., 521234567890): ")
    message = input(f"{Fore.YELLOW}Enter Message (optional): ")
    
    if not phone:
        print(f"{Fore.RED}❌ Phone number is required.")
        return

    # Clean phone number
    phone = ''.join(filter(str.isdigit, phone))

    # Encode message
    encoded_message = urllib.parse.quote(message)
    
    url = f"https://wa.me/{phone}?text={encoded_message}"
    
    print(f"\n{Fore.GREEN}✅ Generated Link:")
    print(f"{Fore.WHITE}{url}")
    
    open_link = input(f"\n{Fore.YELLOW}Open in browser? (y/n): ").lower()
    if open_link == 'y':
        print(f"{Fore.CYAN}Opening WhatsApp Web/App...")
        webbrowser.open(url)

if __name__ == "__main__":
    main()
