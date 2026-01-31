import subprocess
import re
import os
import platform

def get_wifi_passwords():
    print("\n=== WiFi Password Grabber ===")
    
    if platform.system() != "Windows":
        print("[-] This tool is currently optimized for Windows systems.")
        return

    try:
        # Get profiles
        profiles_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="ignore")
        profiles = re.findall(r"All User Profile\s*:\s*(.*)", profiles_data)
        
        if not profiles:
            print("[-] No WiFi profiles found.")
            return

        print(f"[+] Found {len(profiles)} profiles. Extracting passwords...\n")
        print(f"{'WiFi Name (SSID)':<30} | {'Password'}")
        print("-" * 50)

        for profile in profiles:
            profile = profile.strip()
            try:
                profile_info = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear']).decode('utf-8', errors="ignore")
                password_match = re.search(r"Key Content\s*:\s*(.*)", profile_info)
                
                if password_match:
                    password = password_match.group(1)
                else:
                    password = "[None / Open]"
                
                print(f"{profile:<30} | {password}")
            except subprocess.CalledProcessError:
                print(f"{profile:<30} | [Error accessing profile]")

    except Exception as e:
        print(f"[-] An error occurred: {e}")

if __name__ == "__main__":
    get_wifi_passwords()
    input("\nPress Enter to return to menu...")
