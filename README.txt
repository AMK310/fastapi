# FastAPI - Projet d'Évaluation

## Introduction
Ce dossier contient des applications FastAPI développées en réponse aux exercices présentés dans les différents modules du cours de FastAPI. Chaque fichier Python correspond à une étape précise du cours, comme décrit ci-dessous.

---

## Structure des fichiers
- **`app1.py`** : Application correspondant au **Module 1** du cours. Cette application implémente une structure de base d'une API FastAPI avec des routes simples et des concepts fondamentaux.
  
- **`app2.py`** : Application liée au **Module 2**, introduisant les paramètres de requête, les types de données, et la validation avec Pydantic.

- **`app3.py`** : Application du **Module 3**, mettant en œuvre des fonctionnalités avancées telles que les réponses JSON personnalisées et l'utilisation de modèles.

- **`app4_manage_Exceptions.py`** : Application du **Module 4**, se concentrant sur la gestion des exceptions et les réponses d'erreur personnalisées.

- **`app5_asynch.py`** : Application du **Module 5**, explorant les fonctionnalités asynchrones offertes par FastAPI, y compris les tâches asynchrones avec `async/await`.

- **`test_requests_app5.py`** : Fichier de tests pour l'application du **Module 5**, démontrant l'utilisation de la bibliothèque `requests` pour tester les points d'entrée de l'API.

- **`source.py`** : Code source complémentaire utilisé pour les démonstrations ou les exemples pratiques.

---

## Remarques
1. Chaque fichier est autonome et peut être exécuté séparément pour observer les fonctionnalités décrites dans les modules.
2. Le fichier `requirements.txt` contient les dépendances nécessaires pour exécuter les applications. Assurez-vous d'installer ces dépendances avant d'exécuter les fichiers.
3. Un effort particulier a été fait pour documenter le code et rendre chaque module facile à comprendre.

---

## Instructions pour l'exécution
1. Assurez-vous d'être dans un environnement virtuel Python configuré avec `poetry` ou `pip`.
2. Installez les dépendances via `poetry install` ou `pip install -r requirements.txt`.
3. Lancez l'application de votre choix avec `uvicorn` :
   ```bash
   uvicorn app1:app --reload
