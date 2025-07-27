import os, sys, time, getpass, hashlib, json

CONFIG_FILE = os.path.expanduser("~/cykrna_suite/config.json")

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def load_config():
    if not os.path.exists(CONFIG_FILE):
        return {"password": ""}
    with open(CONFIG_FILE, "r") as f:
        return json.load(f)

def save_config(config):
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=2)

def check_password(config):
    if config["password"] == "":
        print("\033[93m[!] First-time setup: Create a password.\033[0m")
        new_pass = getpass.getpass("Set new password: ")
        confirm = getpass.getpass("Confirm password: ")
        if new_pass == confirm:
            config["password"] = hash_password(new_pass)
            save_config(config)
            print("\033[92m[+] Password set successfully!\033[0m")
        else:
            print("\033[91m[-] Passwords do not match. Exiting.\033[0m")
            sys.exit()
    else:
        entered = getpass.getpass("Enter password: ")
        if hash_password(entered) != config["password"]:
            print("\033[91m[-] Incorrect password.\033[0m")
            sys.exit()

def splash():
    os.system("clear")
    print("\033[95mLoading Cykrna Suite...\033[0m")
    for i in range(3):
        print("." * (i+1))
        time.sleep(0.5)
    os.system("clear")

def banner():
    print("""
\033[96m   ____       _             _        
  / ___|  ___| | ___  _ __ | |_ __ _ 
  \___ \ / _ \ |/ _ \| '_ \| __/ _` |
   ___) |  __/ | (_) | | | | || (_| |
  |____/ \___|_|\___/|_| |_|\__\__,_|
\033[0m
    \033[92mAll-in-One Cyber & Utility Toolkit\033[0m
    """)

def launcher():
    splash()
    banner()
    print("""
\033[96m[1]\033[0m Run CLI Mode
\033[96m[2]\033[0m Run Web Dashboard
\033[91m[0]\033[0m Exit
""")
    choice = input("Select: ")
    if choice == "1":
        os.system("python3 cykrna_suite.py")
    elif choice == "2":
        os.system("python3 web_dashboard.py")
    else:
        print("\033[93mExiting...\033[0m")
        sys.exit()

if __name__ == "__main__":
    config = load_config()
    check_password(config)
    launcher()
