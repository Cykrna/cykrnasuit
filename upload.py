import os, json, subprocess

CONFIG_PATH = os.path.expanduser("~/.cykrna_github.json")

def load_config():
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, "r") as f:
            return json.load(f)
    return {"token": "", "repo": ""}

def save_config(data):
    with open(CONFIG_PATH, "w") as f:
        json.dump(data, f, indent=2)

def setup():
    print("[*] GitHub setup")
    token = input("Enter your GitHub Token: ").strip()
    repo = input("Enter your repository (e.g., username/repo): ").strip()
    save_config({"token": token, "repo": repo})
    print("[+] Saved configuration.")

def upload():
    cfg = load_config()
    if not cfg["token"] or not cfg["repo"]:
        print("[-] GitHub not configured. Run setup first.")
        return
    os.environ["GITHUB_TOKEN"] = cfg["token"]
    cmds = [
        "git init",
        "git add .",
        'git commit -m "Auto-update from Cykrna Suite"',
        f"git remote set-url origin https://{cfg['token']}@github.com/{cfg['repo']}.git || git remote add origin https://{cfg['token']}@github.com/{cfg['repo']}.git",
        "git branch -M main",
        "git push -u origin main --force"
    ]
    for c in cmds:
        subprocess.run(c, shell=True)
    print("[+] Code uploaded to GitHub!")

if __name__ == "__main__":
    print("1. Setup GitHub\n2. Upload Now")
    ch = input("Choice: ")
    if ch == "1": setup()
    elif ch == "2": upload()
