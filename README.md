## Data

### Source des Données

Les données utilisées dans ce projet proviennent d'un dataset public disponible sur Kaggle. Pour reproduire les résultats et utiliser le script de récupération des données, veuillez suivre les étapes ci-dessous.

### Configuration et Téléchargement des Données

1. **Configurer l'API Kaggle** : 
   - Créez un compte sur [Kaggle](https://www.kaggle.com/) si ce n'est pas déjà fait.
   - Allez dans vos paramètres de compte (Account) et téléchargez votre clé API `kaggle.json`.
   - Placez le fichier `kaggle.json` dans le dossier `~/.kaggle/` sous Linux/Mac ou `%USERPROFILE%\.kaggle\` sous Windows.
   - Assurez-vous que le fichier a les permissions correctes (en lecture seule).

2. **Télécharger les Données** :
   - Dans le terminal, lancez le script `get_data.py` :
     ```bash
     python src/utils/get_data.py
     ```
   - Ce script téléchargera le fichier CSV brut et le stockera dans le dossier `data/raw/` du projet.

### Détails des Données

- **Format** : CSV
- **Emplacement** : `data/raw/rawdata.csv`

### Liens vers le Dataset Kaggle

- Lien vers le dataset sur Kaggle : [Nom du Dataset](https://www.kaggle.com/username/dataset-name)