# Utilisation d'une image de base Python
FROM python:3.8-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires
COPY . /app

# Installer les dépendances
RUN pip install -r requirements.txt

# Commande pour démarrer l'application
CMD ["python", "app.py"]
