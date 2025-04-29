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

4. Pour lancer le serveur de l'application, naviguez vers `src/moovitamix_fastapi/` et exécutez:

```
python -m uvicorn main:app
```

5. Pour lancer le flux de données, naviguez vers `src/pipeline/` et exécutez:

```
python main.py
```

Après l’extraction et la transformation, le flux de données enregistre les données localement dans `src/pipeline/data/`.

6. Pour exécuter les test unitaires, naviguez à la racine du projet et exécutez [^1]:

```
pytest
```

[^1]: Selon votre configuration, vous devrez peut-être exécuter la commande suivanate à la place: `python -m pytest`

## Questions (étapes 4 à 7)

### Étape 4

_votre réponse ici_

### Étape 5

_votre réponse ici_

### Étape 6

_votre réponse ici_

### Étape 7

_votre réponse ici_
