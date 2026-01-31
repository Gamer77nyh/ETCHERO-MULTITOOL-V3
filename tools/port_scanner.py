import socket
from colorama import Fore, init

init(autoreset=True)

def scan_port(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((host, port))
        if result == 0:
            print(f"{Fore.GREEN}[+] Port {port} is OPEN")
        s.close()
    except Exception:
        pass

def main():
    print(f"\n{Fore.GREEN}--- Port Scanner ---")
    host = input(f"{Fore.YELLOW}Enter target host (e.g., 127.0.0.1): ")
    try:
        start_port = int(input(f"{Fore.YELLOW}Enter start port: "))
        end_port = int(input(f"{Fore.YELLOW}Enter end port: "))
        
        print(f"{Fore.CYAN}Scanning {host} from port {start_port} to {end_port}...")
        for port in range(start_port, end_port + 1):
            scan_port(host, port)
        print(f"{Fore.GREEN}Scan complete.")
    except ValueError:
        print(f"{Fore.RED}❌ Invalid port numbers.")

if __name__ == "__main__":
    main()
