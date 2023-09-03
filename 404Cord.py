
import webbrowser

def print_red_text(text):
    print("\033[91m" + text + "\033[0m")

def send_spam(webhook_url, spam_words):
    
    for word in spam_words:
        print(f"Word Sended")

def token_login(token):
    
    webbrowser.open(f"https://discord.com/login?token={token}")
    print("Login Done 👍🏻")

def delete_webhook(webhook_url):
    print("Enter Webhook: ", webhook_url)
    print("Deleted")

def main():
    print_red_text(" /$$   /$$  /$$$$$$  /$$   /$$  /$$$$$$                            /$$")
    print("| $$  | $$ /$$$_  $$| $$  | $$ /$$__  $$                          | $$")
    print("| $$  | $$| $$$$\ $$| $$  | $$| $$  \__/  /$$$$$$   /$$$$$$   /$$$$$$$")
    print("| $$$$$$$$| $$ $$ $$| $$$$$$$$| $$       /$$__  $$ /$$__  $$ /$$__  $$")
    print("|_____  $$| $$\ $$$$|_____  $$| $$      | $$  \ $$| $$  \__/| $$  | $$")
    print("      | $$| $$ \ $$$      | $$| $$    $$| $$  | $$| $$      | $$  | $$")
    print("      | $$|  $$$$$$/      | $$|  $$$$$$/|  $$$$$$/| $$      |  $$$$$$$")
    print("      |__/ \______/       |__/ \______/  \______/ |__/       \_______/")
    print("\n")
    print("1. Spam Webhook.")
    print("2. Token Login.")
    print("3. Delete Webhook.")
    print("4. Create Token. (Not Working)")

    choice = int(input("Enter 1-3"))

    if choice == 1:
        webhook_url = input("Enter Webhook: ")
        spam_words = input("Enter Word Will Spam (مفصولة بفواصل): ").split(",")
        send_spam(webhook_url, spam_words)
    elif choice == 2:
        token = input("Enter Token: ")
        token_login(token)
    elif choice == 3:
        webhook_url = input("Enter Webhook: ")
        delete_webhook(webhook_url)
    elif choice == 4:
        print("Working On It")
    else:
        print("Error !.")

if __name__ == "__main__":
    main()
  
