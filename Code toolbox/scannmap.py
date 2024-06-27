import subprocess
import sys
import nmap
import customtkinter as ctk
from tkinter import messagebox, filedialog
import os

def install_dependencies():
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'python-nmap'])
    except Exception as e:
        print(f"Failed to install dependencies: {str(e)}")
        sys.exit(1)

def run_scan():
    target = target_entry.get()
    if not target:
        messagebox.showerror("Input Error", "Please enter a target IP address.")
        return

    scanner = nmap.PortScanner()
    try:
        scanner.scan(target, arguments='-T4 -A -v')
        save_results(scanner, target)
        display_results(scanner)
    except Exception as e:
        messagebox.showerror("Scan Error", str(e))

def save_results(scanner, target):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(script_dir, "scannmap_results.txt")
    with open(filename, "w") as file:
        file.write(f"Scan Results for {target}:\n")
        for host in scanner.all_hosts():
            file.write(f"Host: {host} ({scanner[host].hostname()})\n")
            file.write(f"State: {scanner[host].state()}\n")
            for protocol in scanner[host].all_protocols():
                file.write(f"Protocol: {protocol}\n")
                ports = scanner[host][protocol].keys()
                for port in ports:
                    port_info = scanner[host][protocol][port]
                    file.write(f"Port: {port}\tState: {port_info['state']}\tService: {port_info['name']}\tVersion: {port_info['version']}\n")
            file.write("\n")

def display_results(scanner):
    result_textbox.delete(1.0, ctk.END)
    for host in scanner.all_hosts():
        result_textbox.insert(ctk.END, f"Host: {host} ({scanner[host].hostname()})\n")
        result_textbox.insert(ctk.END, f"State: {scanner[host].state()}\n")
        for protocol in scanner[host].all_protocols():
            result_textbox.insert(ctk.END, f"Protocol: {protocol}\n")
            ports = scanner[host][protocol].keys()
            for port in ports:
                port_info = scanner[host][protocol][port]
                result_textbox.insert(ctk.END, f"Port: {port}\tState: {port_info['state']}\tService: {port_info['name']}\tVersion: {port_info['version']}\n")
        result_textbox.insert(ctk.END, "\n")

def create_gui():
    global target_entry, result_textbox

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    root = ctk.CTk()
    root.title("Nmap GUI Scanner")
    root.configure(bg='#333333')

    frame = ctk.CTkFrame(root, corner_radius=10)
    frame.pack(padx=20, pady=20, fill="both", expand=True)

    target_label = ctk.CTkLabel(frame, text="Target IP:")
    target_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    target_entry = ctk.CTkEntry(frame, width=200)
    target_entry.grid(row=0, column=1, padx=10, pady=10)

    scan_button = ctk.CTkButton(frame, text="Scan", command=run_scan, fg_color="blue", hover_color="blue")
    scan_button.grid(row=0, column=2, padx=10, pady=10)

    result_textbox = ctk.CTkTextbox(frame, width=600, height=400, wrap="none")
    result_textbox.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    install_dependencies()
    create_gui()