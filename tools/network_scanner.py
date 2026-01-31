import socket
import threading
from queue import Queue
from colorama import Fore, init

init(autoreset=True)

# Basic ARP scan requires root/admin privileges and scapy, which might be too heavy.
# We'll implement a ping sweeper or a basic connect scanner for the local subnet.

def check_host(ip):
    try:
        # We'll try to connect to common ports to see if host is up
        # This is faster than OS ping in python without admin rights
        for port in [80, 443, 22, 445, 135]:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            result = s.connect_ex((ip, port))
            s.close()
            if result == 0:
                try:
                    hostname = socket.gethostbyaddr(ip)[0]
                except socket.herror:
                    hostname = "Unknown"
                print(f"{Fore.GREEN}[+] Host Up: {Fore.WHITE}{ip} ({hostname})")
                return
    except Exception:
        pass

def worker(queue):
    while not queue.empty():
        ip = queue.get()
        check_host(ip)
        queue.task_done()

def main():
    print(f"\n{Fore.GREEN}--- Network Scanner ---")
    print(f"{Fore.CYAN}Scans local subnet for active hosts.")
    
    base_ip = input(f"{Fore.YELLOW}Enter Base IP (e.g., 192.168.1): ")
    
    if not base_ip:
        print(f"{Fore.RED}❌ Base IP required.")
        return

    # Validate format roughly
    if base_ip.count('.') != 3 and not base_ip.endswith('.'):
         base_ip += "."

    if base_ip.count('.') != 3:
         print(f"{Fore.RED}❌ Invalid IP format. Use format like 192.168.1")
         return
         
    if base_ip.endswith('.'):
        base_ip = base_ip[:-1] # Remove trailing dot if user added it, logic below handles it

    print(f"{Fore.CYAN}Scanning subnet {base_ip}.1 - {base_ip}.254 ...")
    
    queue = Queue()
    
    for i in range(1, 255):
        queue.put(f"{base_ip}.{i}")
        
    threads = []
    for _ in range(50): # 50 threads for speed
        t = threading.Thread(target=worker, args=(queue,))
        t.start()
        threads.append(t)
        
    for t in threads:
        t.join()

    print(f"\n{Fore.GREEN}Scan complete.")

if __name__ == "__main__":
    main()
