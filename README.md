# ToolboxCyber
ToolBox Cybersecuriter Sup de Vinci

CLEMBOX est une boîte à outils de cybersécurité conçue pour aider les professionnels de la sécurité dans leurs tâches quotidiennes. Elle inclut divers scripts pour des opérations de sécurité courantes telles que les attaques bruteforce SSH, la vérification de mots de passe et la numérisation de réseaux.

Fonctionnalités
Attaque Bruteforce SSH : Tente d'accéder à un système via SSH en utilisant une liste de noms d'utilisateurs et de mots de passe.
Vérificateur de Mot de Passe : Valide la robustesse et la conformité des mots de passe avec les politiques de sécurité.
Scanner de Réseau : Utilise Nmap pour scanner et rapporter les appareils réseau.
Installation
Prérequis
Python 3.x
Étapes
Clonez le dépôt :


git clone https://github.com/Momollait/toolbox-CS-SLD.git
cd toolbox-CS-SLD
Exécutez la boîte à outils :


python main.py
Utilisation
Chaque script peut être exécuté via l'interface principale fournie par main.py.

Attaque Bruteforce SSH
L'outil d'attaque bruteforce SSH tente de se connecter à une machine via SSH en utilisant une liste de noms d'utilisateurs et de mots de passe. Il est utile pour tester la robustesse des mots de passe SSH.

Vérificateur de Mot de Passe
Cet outil vérifie la robustesse d'un mot de passe en évaluant sa longueur, sa complexité et sa conformité avec les politiques de sécurité.

Scanner de Réseau
Le Scanner de Réseau utilise Nmap pour scanner un réseau et identifier les appareils connectés, les ports ouverts et les services en cours d'exécution.


Licence
Ce projet est  sous la licence SupDeVinci. Merci à vous.


Structure du Dépôt
main.py : Interface principale de la boîte à outils.
bruteforcessh.py : Script pour les attaques bruteforce SSH.
check_password.py : Script pour vérifier la robustesse des mots de passe.
scannmap.py : Script pour le scan de réseau.
README.md : Documentation du projet.
