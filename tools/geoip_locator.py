import requests
from colorama import Fore, init

init(autoreset=True)

def locate_ip(ip):
    try:
        url = f"http://ip-api.com/json/{ip}"
        response = requests.get(url)
        data = response.json()
        
        if data['status'] == 'success':
            print(f"\n{Fore.GREEN}--- GeoIP Location for {ip} ---")
            print(f"{Fore.CYAN}Country: {Fore.WHITE}{data.get('country')} ({data.get('countryCode')})")
            print(f"{Fore.CYAN}Region: {Fore.WHITE}{data.get('regionName')} ({data.get('region')})")
            print(f"{Fore.CYAN}City: {Fore.WHITE}{data.get('city')}")
            print(f"{Fore.CYAN}Latitude: {Fore.WHITE}{data.get('lat')}")
            print(f"{Fore.CYAN}Longitude: {Fore.WHITE}{data.get('lon')}")
            print(f"{Fore.CYAN}Timezone: {Fore.WHITE}{data.get('timezone')}")
            print(f"{Fore.CYAN}Google Maps: {Fore.WHITE}https://www.google.com/maps/?q={data.get('lat')},{data.get('lon')}")
        else:
            print(f"{Fore.RED}❌ Error: {data.get('message')}")
    except Exception as e:
        print(f"{Fore.RED}❌ Failed to locate IP: {e}")

def main():
    print(f"\n{Fore.GREEN}--- GeoIP Locator ---")
    ip = input(f"{Fore.YELLOW}Enter IP address (leave empty for your own IP): ")
    print(f"{Fore.CYAN}Locating...")
    locate_ip(ip)

if __name__ == "__main__":
    main()
