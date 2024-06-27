import customtkinter as ctk
from tkinter import messagebox
import os
import subprocess
import sys

def install_dependencies():
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'customtkinter'])
    except Exception as e:
        print(f"Failed to install dependencies: {str(e)}")
        sys.exit(1)

def verify_password():
    password = password_entry.get()
    if len(password) == 0:
        messagebox.showerror("Erreur", "Veuillez entrer un mot de passe.")
        return

    score = 0
    if len(password) < 12:
        message = "Faible: Votre mot de passe est trop court. Il doit contenir au moins 12 caractères."
    else:
        score += 1
        if any(char.isdigit() for char in password):
            score += 1
        if any(char.isupper() for char in password):
            score += 1
        if any(char.islower() for char in password):
            score += 1
        if any(not char.isalnum() for char in password):
            score += 1
        
        if score < 3:
            message = "Moyen: Votre mot de passe est moyen. Essayez d'utiliser des chiffres, des lettres majuscules, et des caractères spéciaux."
        elif score < 5:
            message = "Bon: Votre mot de passe est bon, mais peut être amélioré."
        else:
            message = "Excellent: Votre mot de passe est excellent."

    result_label.configure(text=message)
    save_results(password, message)

def save_results(password, evaluation):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(script_dir, "check_password_results.txt")
    with open(filename, "w") as file:
        file.write(f"Password: {password}\n")
        file.write(f"Evaluation: {evaluation}\n")

app = ctk.CTk()
app.title("Vérificateur de mot de passe")

label = ctk.CTkLabel(app, text="Entrez votre mot de passe:", font=("Arial", 13))
label.pack(pady=20)

password_entry = ctk.CTkEntry(app, width=300, font=("Arial", 13), show="*")
password_entry.pack(pady=10)

verify_button = ctk.CTkButton(app, text="Vérifier", command=verify_password)
verify_button.pack(pady=20)

result_label = ctk.CTkLabel(app, text="", font=("Arial", 13))
result_label.pack(pady=10)

if __name__ == "__main__":
    install_dependencies()
    app.mainloop()