import psutil
import platform
import os
from colorama import Fore, init

init(autoreset=True)

def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

def main():
    print(f"\n{Fore.GREEN}--- System Information ---")
    
    # System info
    uname = platform.uname()
    print(f"{Fore.CYAN}System:{Fore.WHITE} {uname.system}")
    print(f"{Fore.CYAN}Node Name:{Fore.WHITE} {uname.node}")
    print(f"{Fore.CYAN}Release:{Fore.WHITE} {uname.release}")
    print(f"{Fore.CYAN}Version:{Fore.WHITE} {uname.version}")
    print(f"{Fore.CYAN}Machine:{Fore.WHITE} {uname.machine}")
    print(f"{Fore.CYAN}Processor:{Fore.WHITE} {uname.processor}")

    # CPU info
    print(f"\n{Fore.GREEN}--- CPU Info ---")
    print(f"{Fore.CYAN}Physical cores:{Fore.WHITE} {psutil.cpu_count(logical=False)}")
    print(f"{Fore.CYAN}Total cores:{Fore.WHITE} {psutil.cpu_count(logical=True)}")
    print(f"{Fore.CYAN}CPU Usage:{Fore.WHITE} {psutil.cpu_percent()}%")

    # Memory info
    print(f"\n{Fore.GREEN}--- Memory Info ---")
    svmem = psutil.virtual_memory()
    print(f"{Fore.CYAN}Total:{Fore.WHITE} {get_size(svmem.total)}")
    print(f"{Fore.CYAN}Available:{Fore.WHITE} {get_size(svmem.available)}")
    print(f"{Fore.CYAN}Used:{Fore.WHITE} {get_size(svmem.used)}")
    print(f"{Fore.CYAN}Percentage:{Fore.WHITE} {svmem.percent}%")

    # Disk info
    print(f"\n{Fore.GREEN}--- Disk Info ---")
    partitions = psutil.disk_partitions()
    for partition in partitions:
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
            print(f"{Fore.CYAN}Device:{Fore.WHITE} {partition.device}")
            print(f"{Fore.CYAN}  Mountpoint:{Fore.WHITE} {partition.mountpoint}")
            print(f"{Fore.CYAN}  Total Size:{Fore.WHITE} {get_size(partition_usage.total)}")
            print(f"{Fore.CYAN}  Used:{Fore.WHITE} {get_size(partition_usage.used)}")
            print(f"{Fore.CYAN}  Free:{Fore.WHITE} {get_size(partition_usage.free)}")
            print(f"{Fore.CYAN}  Percentage:{Fore.WHITE} {partition_usage.percent}%")
        except PermissionError:
            continue

if __name__ == "__main__":
    main()
