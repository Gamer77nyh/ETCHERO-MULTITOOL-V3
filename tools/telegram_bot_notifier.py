import requests
from colorama import Fore, init

init(autoreset=True)

def send_telegram_message(bot_token, chat_id, message):
    try:
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        payload = {
            "chat_id": chat_id,
            "text": message
        }
        response = requests.post(url, json=payload)
        
        if response.status_code == 200:
            print(f"\n{Fore.GREEN}✅ Message sent successfully!")
        else:
            print(f"\n{Fore.RED}❌ Failed to send message. Error: {response.text}")
    except Exception as e:
        print(f"\n{Fore.RED}❌ Error: {e}")

def main():
    print(f"\n{Fore.GREEN}--- Telegram Bot Notifier ---")
    print(f"{Fore.CYAN}Allows you to send a message via your Telegram Bot.")
    
    bot_token = input(f"{Fore.YELLOW}Enter Bot Token: ")
    chat_id = input(f"{Fore.YELLOW}Enter Chat ID: ")
    message = input(f"{Fore.YELLOW}Enter Message: ")

    if not bot_token or not chat_id or not message:
        print(f"{Fore.RED}❌ All fields are required.")
        return

    print(f"{Fore.CYAN}Sending message...")
    send_telegram_message(bot_token, chat_id, message)

if __name__ == "__main__":
    main()
