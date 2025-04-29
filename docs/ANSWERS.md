# Réponses du test

## _Utilisation de la solution (étape 1 à 3)_

_Inscrire la documentation technique_

1. Créer un environnement virtuel:

```
python3.12 -m venv .venv
```

2. Activer de l'environnement virtuel:

```
source .venv/bin/activate
```

3. Installer les dépendances:

```
pip install -r requirements.txt
```

4. Lancer le serveur de l'application:

```
cd src/moovitamix_fastapi/   # par rapport à la racine du projet
python -m uvicorn main:app
```

5. Lancer la flux de données:

```
cd src/pipeline/ # par rapport à la racine du projet
python main.py
```

6. Pour exécuter les test unitaires, déplacez-vous à la racine du projet et exécuter:

```
pytest
```

## Questions (étapes 4 à 7)

### Étape 4

_votre réponse ici_

### Étape 5

_votre réponse ici_

### Étape 6

_votre réponse ici_

### Étape 7

_votre réponse ici_
