#!/usr/bin/env python3

import requests
import json
import os

# ========================
# CONFIGURA ESTAS VARIABLES
# ========================

NPM_HOST = "https://npm.ezample.com"
USERNAME = "acladmin@example.com"  # <-- tu usuario NPM
PASSWORD = "tupasswordsupersegura"  # <-- tu contraseña NPM
ACCESS_LIST_ID = 1
ACCESS_LIST_NAME = "MI_ZONA"
LAST_IP_FILE = "/tmp/last_public_ip.txt"

# ========================
# FUNCIONES
# ========================

def get_public_ip():
    return requests.get("https://api.ipify.org").text.strip()

def get_token():
    url = f"{NPM_HOST}/api/tokens"
    headers = {"Content-Type": "application/json"}
    data = {
        "identity": USERNAME,
        "secret": PASSWORD
    }

    resp = requests.post(url, headers=headers, json=data)
    resp.raise_for_status()
    return resp.json()["token"]

def update_access_list(ip, token):
    url = f"{NPM_HOST}/api/nginx/access-lists/{ACCESS_LIST_ID}"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    payload = {
        "name": ACCESS_LIST_NAME,
        "satisfy_any": True,
        "pass_auth": False,
        "items": [],
        "clients": [{"address": f"{ip}/32", "directive": "allow"}]
    }

    resp = requests.put(url, headers=headers, json=payload)
    resp.raise_for_status()
    print(f"[+] Lista de acceso actualizada con IP {ip}")

def load_last_ip():
    if os.path.exists(LAST_IP_FILE):
        with open(LAST_IP_FILE, "r") as f:
            return f.read().strip()
    return None

def save_last_ip(ip):
    with open(LAST_IP_FILE, "w") as f:
        f.write(ip)

# ========================
# MAIN
# ========================

def main():
    current_ip = get_public_ip()
    last_ip = load_last_ip()

    if current_ip == last_ip:
        print("[=] La IP no ha cambiado, no se hace nada.")
        return

    print(f"[~] IP cambiada de {last_ip} a {current_ip}, actualizando...")
    token = get_token()
    update_access_list(current_ip, token)
    save_last_ip(current_ip)

if __name__ == "__main__":
    main()
