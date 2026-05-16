# dsite/admin_cli.py

import sys
from pathlib import Path


VERSION = "1.0.0"


# =========================================
# ADMIN CLI COMMANDS
# =========================================

def create_superuser():
    print("[DSite Admin] Creazione superuse")
    username = input("Username: ")
    password = input("Password: ")
    confirm_password = input("Conferma password: ")
    if confirm_password==password:
       print(f"[DSite Admin] Superuser '{username}' creato (simulato per la prima versione)")
    else:
       print("[DSite Admin] La password non corrisponde.")


def list_projects():
    print("[DSite Admin] Progetti nella cartella corrente:\n")

    for item in Path(".").iterdir():
        if item.is_dir():
            print(" -", item.name)


def main():

    args = sys.argv

    # ---------------------------------
    # VERSION
    # ---------------------------------

    if "--version" in args:
        print(f"DSite Admin CLI {VERSION}")
        return

    # ---------------------------------
    # COMMANDS
    # ---------------------------------

    if len(args) >= 2:

        command = args[1]

        if command == "createsuperuser":
            create_superuser()

        elif command == "listprojects":
            list_projects()

        else:
            print(f"[DSite Admin] Comando sconosciuto: {command}")

        return

    # ---------------------------------
    # HELP
    # ---------------------------------

    print("")
    print("DSite Admin CLI")
    print("")
    print("Comandi:")
    print("")
    print("dsite-admin --version")
    print("dsite-admin createsuperuser")
    print("dsite-admin listprojects")
    print("")
    

if __name__ == "__main__":
    main()
