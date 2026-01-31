import webbrowser
from colorama import Fore, init

init(autoreset=True)

def main():
    print(f"\n{Fore.GREEN}--- Google Dorker ---")
    domain = input(f"{Fore.YELLOW}Enter target domain (e.g., example.com): ")
    
    dorks = {
        "1": {"name": "Publicly exposed documents", "query": f"site:{domain} filetype:pdf OR filetype:doc OR filetype:docx OR filetype:xls OR filetype:xlsx"},
        "2": {"name": "Directory listing", "query": f"site:{domain} intitle:index.of"},
        "3": {"name": "Configuration files", "query": f"site:{domain} ext:xml OR ext:conf OR ext:cnf OR ext:reg OR ext:inf OR ext:rdp OR ext:cfg OR ext:txt OR ext:ora OR ext:ini"},
        "4": {"name": "Database files", "query": f"site:{domain} ext:sql OR ext:dbf OR ext:mdb"},
        "5": {"name": "Log files", "query": f"site:{domain} ext:log"},
        "6": {"name": "Backup and old files", "query": f"site:{domain} ext:bkp OR ext:bak OR ext:old OR ext:backup"},
        "7": {"name": "Login pages", "query": f"site:{domain} inurl:login OR inurl:signin OR intitle:Login"},
        "8": {"name": "SQL Errors", "query": f"site:{domain} intext:\"sql syntax near\" OR intext:\"syntax error has occurred\" OR intext:\"incorrect syntax near\""},
        "9": {"name": "PHP Info", "query": f"site:{domain} ext:php intitle:phpinfo \"published by the PHP Group\""}
    }

    print(f"\n{Fore.CYAN}Select a dork type to generate URL:")
    for key, value in dorks.items():
        print(f"[{key}] {value['name']}")
    print("[0] Back")

    choice = input(f"\n{Fore.YELLOW}Select an option: ")
    
    if choice == '0':
        return
    
    if choice in dorks:
        query = dorks[choice]['query']
        url = f"https://www.google.com/search?q={query.replace(' ', '+').replace(':', '%3A').replace('\"', '%22')}"
        print(f"\n{Fore.GREEN}✅ Generated Dork URL:")
        print(f"{Fore.WHITE}{url}")
        
        open_browser = input(f"\n{Fore.YELLOW}Open in browser? (y/n): ").lower()
        if open_browser == 'y':
            webbrowser.open(url)
    else:
        print(f"{Fore.RED}❌ Invalid option.")

if __name__ == "__main__":
    main()
