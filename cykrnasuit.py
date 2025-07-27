import os, sys, json, datetime, getpass, hashlib, time

CONFIG_FILE = os.path.expanduser("~/cykrna_suite/config.json")
LOG_FILE = os.path.expanduser("~/cykrna_suite/data/usage.log")

# --- Password Hashing ---
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# --- Load & Save Config ---
def load_config():
    if not os.path.exists(CONFIG_FILE):
        config = {"password": ""}
        save_config(config)
    with open(CONFIG_FILE, "r") as f:
        return json.load(f)

def save_config(config):
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=2)

# --- Logging ---
def log_usage(module):
    with open(LOG_FILE, "a") as f:
        f.write(f"[{datetime.datetime.now()}] {module}\n")

# --- Password ---
def check_password(config):
    if config["password"] == "":
        print("\033[93m[!] First-time setup: Create your password.\033[0m")
        new_pass = getpass.getpass("Set new password: ")
        confirm = getpass.getpass("Confirm password: ")
        if new_pass == confirm:
            config["password"] = hash_password(new_pass)
            save_config(config)
            print("\033[92m[+] Password set successfully!\033[0m")
            time.sleep(1)
        else:
            print("\033[91m[-] Passwords do not match. Exiting.\033[0m")
            sys.exit()
    else:
        entered = getpass.getpass("Enter password: ")
        if hash_password(entered) != config["password"]:
            print("\033[91m[-] Incorrect password.\033[0m")
            sys.exit()

# --- Splash Screen ---
def splash():
    os.system("clear")
    print("\033[95mInitializing Cykrna Suite...\033[0m")
    for i in range(3):
        print("." * (i+1))
        time.sleep(0.5)
    os.system("clear")

# --- Banner ---
def banner():
    colors = ["\033[96m", "\033[94m", "\033[95m"]
    text = """
   ____       _             _        
  / ___|  ___| | ___  _ __ | |_ __ _ 
  \___ \ / _ \ |/ _ \| '_ \| __/ _` |
   ___) |  __/ | (_) | | | | || (_| |
  |____/ \___|_|\___/|_| |_|\__\__,_|
    """
    for i, line in enumerate(text.splitlines()):
        print(colors[i % len(colors)] + line + "\033[0m")
        time.sleep(0.05)
    print("\033[92m   Welcome to Cykrna Suite — All-in-One Toolkit\033[0m\n")

# --- About Page ---
def show_about():
    os.system("clear")
    print("\033[95m--- About Cykrna Suite ---\033[0m\n")
    print("Version: 1.0")
    print("Developed by: Cykrna Team")
    print("Description: All-in-One Cyber & Utility Toolkit for Termux and Linux.")
    print("Website: Coming Soon")
    print("\nPress Enter to return...")
    input()

# --- Main Menu ---
def main_menu():
    banner()
    print("""
\033[96m[1]\033[0m Lisa AI Assistant
\033[96m[2]\033[0m WhatsApp Toolkit
\033[96m[3]\033[0m MediaGrabber
\033[96m[4]\033[0m YouTube Downloader
\033[96m[5]\033[0m Cybersecurity Hub
\033[96m[6]\033[0m CCTV Surveillance
\033[96m[7]\033[0m Captcha & OTP Generator
\033[96m[8]\033[0m House Planner
\033[93m[A]\033[0m About Cykrna
\033[93m[U]\033[0m Update Suite
\033[91m[0]\033[0m Exit
""")

# --- Run Selected Module ---
def run_module(choice):
    modules = {
        "1": "modules/lisa_ai.py",
        "2": "modules/whatsapp_toolkit.py",
        "3": "modules/mediagrabber.py",
        "4": "modules/ytdownloader.py",
        "5": "modules/cyber_hub.py",
        "6": "modules/cctv_surveillance.py",
        "7": "modules/captcha_otp.py",
        "8": "modules/house_planner.py"
    }
    if choice.upper() == "U":
        os.system("python3 modules/updater.py")
    elif choice.upper() == "A":
        show_about()
    elif choice in modules:
        log_usage(modules[choice])
        os.system(f"python3 {modules[choice]}")
    else:
        print("\033[91mExiting...\033[0m")
        sys.exit()

# --- Main Execution ---
if __name__ == "__main__":
    config = load_config()
    splash()
    check_password(config)
    while True:
        main_menu()
        choice = input("Select: ")
        if choice == "0":
            print("\033[93mGoodbye!\033[0m")
            break
        run_module(choice)
