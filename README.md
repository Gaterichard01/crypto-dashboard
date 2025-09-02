Tableau de bord Crypto
Ce projet est un tableau de bord simple pour afficher et suivre les données de cryptomonnaies en temps réel. Il est développé avec un backend en Python (Flask) et un frontend en React (JavaScript, HTML, CSS).

Fonctionnalités
Affichage en temps réel : Affiche le top 50 des cryptomonnaies, mises à jour toutes les 60 secondes.

Recherche : Filtre les cryptos par nom ou symbole.

Tri : Trie la liste par prix ou par capitalisation boursière.

Détails des cryptos : Affiche un graphique de l'historique des prix sur 7 jours quand vous cliquez sur une crypto.

Installation
Prérequis
Python 3.x

pip (le gestionnaire de paquets de Python)

Étape 1 : Cloner le dépôt
Clonez ce dépôt Git sur votre machine locale.

git clone [https://github.com/Gaterichard01/crypto-dashboard.git]((https://github.com/Gaterichard01/crypto-dashboard).git)
cd crypto-dashboard

Étape 2 : Installer les dépendances
Installez les bibliothèques Python nécessaires pour le backend.

pip install Flask Flask-Cors requests

Étape 3 : Lancer le backend
Lancez le serveur Flask à partir du terminal.

python app.py

Le serveur devrait se lancer sur http://127.0.0.1:5000. Laissez ce terminal ouvert.

Étape 4 : Lancer le frontend
Ouvrez le fichier index.html dans votre navigateur web. Vous pouvez simplement double-cliquer dessus ou utiliser une extension comme "Live Server" dans VS Code pour un développement plus facile.

Auteurs
Fait avec l'aide de Google Gemini
