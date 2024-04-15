# Utiliser une image de base Python
FROM python:3.8-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires
COPY ./app /app

# Installer les dépendances
RUN pip install -r requirements.txt

# Exposer le port sur lequel l'application va tourner
EXPOSE 5000

# Définir la commande pour démarrer l'application
CMD ["python", "app.py"]
