import requests
from colorama import Fore, init

init(autoreset=True)

def track_ip(ip):
    try:
        url = f"http://ip-api.com/json/{ip}"
        response = requests.get(url)
        data = response.json()
        
        if data['status'] == 'success':
            print(f"\n{Fore.GREEN}--- IP Information for {ip} ---")
            print(f"{Fore.CYAN}Country: {Fore.WHITE}{data.get('country')}")
            print(f"{Fore.CYAN}Region: {Fore.WHITE}{data.get('regionName')}")
            print(f"{Fore.CYAN}City: {Fore.WHITE}{data.get('city')}")
            print(f"{Fore.CYAN}ZIP: {Fore.WHITE}{data.get('zip')}")
            print(f"{Fore.CYAN}ISP: {Fore.WHITE}{data.get('isp')}")
            print(f"{Fore.CYAN}Org: {Fore.WHITE}{data.get('org')}")
            print(f"{Fore.CYAN}AS: {Fore.WHITE}{data.get('as')}")
            print(f"{Fore.CYAN}Lat/Lon: {Fore.WHITE}{data.get('lat')}, {data.get('lon')}")
        else:
            print(f"{Fore.RED}❌ Error: {data.get('message')}")
    except Exception as e:
        print(f"{Fore.RED}❌ Failed to track IP: {e}")

def main():
    print(f"\n{Fore.GREEN}--- IP Tracker ---")
    ip = input(f"{Fore.YELLOW}Enter IP address to track (leave empty for your own IP): ")
    print(f"{Fore.CYAN}Tracking...")
    track_ip(ip)

if __name__ == "__main__":
    main()
