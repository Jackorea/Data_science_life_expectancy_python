# Projet : Facteurs de l'espérance de vie

## « User Guide »
Pour déployer et utiliser le dashboard sur une autre machine, suivez les étapes ci-dessous :

1. **Cloner le projet :**   
Dans le terminal, exécutez la commande suivante pour copier le projet sur votre machine :


    $ git clone https://git.esiee.fr/projet-data-science/myproject.git

2. **Configurer les identifiants Kaggle :**  
Placez votre fichier kaggle.json dans le dossier principal du projet. Ce fichier contient vos identifiants d’API Kaggle pour accéder aux données. Le script copy_json_file.py copiera automatiquement ce fichier dans le dossier .kaggle de votre répertoire personnel.

3. **Installer les dépendances :**  
Assurez-vous d'installer toutes les dépendances nécessaires listées dans le fichier requirements.txt. Exécutez :

   $ pip install -r requirements.txt

4. **Lancer le dashboard :**
Une fois les dépendances installées, vous pouvez démarrer le dashboard en lançant la commande suivante dans le répertoire racine du projet :

   $ python main.py

## ***Note importante :***
Après l'exécution de **main.py**, vérifiez l'apparition de la phrase suivante dans le terminal pour confirmer le chargement correct des données :

    Données nettoyées chargées avec succès.

Cependant, juste après ce message, il est possible que vous rencontriez des erreurs de type :


    2024-11-11 21:26:55,269 WARNING Retrying (Retry(total=1, connect=None, read=None, redirect=None, status=None)) after connection broken by 'ReadTimeoutError("HTTPSConnectionPool(host='nominatim.openstreetmap.org', port=443): Read timed out. (read timeout=1)")': /search?q=The+former+Yugoslav+republic+of+Macedonia&format=json&limit=1

**Ceci est normal.** Ces messages d'erreur se produisent parfois en raison de services externes comme geolocator.geocode, qui peuvent être momentanément surchargés. Ils n’affectent pas le fonctionnement général du dashboard.

## « Data » 
### Données

Nos données proviennent de **Kaggle**, une plateforme qui héberge des centaines de milliers de jeux de données. Nous avons sélectionné le domaine de la **santé**, avec un fichier de base nommé **life_expectancy** (espérance de vie en anglais). Ce dataset contient des informations variées sur les facteurs susceptibles d'influencer l'espérance de vie, à la hausse comme à la baisse. Les données couvrent tous les pays du monde entre **2000 et 2015**, avec **16 enregistrements par pays**.

### Structure des Données

Les variables incluses dans notre dataset sont les suivantes :

- **Pays** : `country`
- **Année** : `Year` (de 2000 à 2015)
- **Statut** : `Status` (Développé ou en Développement)
- **Espérance de vie** : `Life expectancy` (en années)
- **Mortalité des adultes** : `Adult Mortality` (probabilité de mourir entre 15 et 60 ans pour 1000 habitants)
- **Mortalité infantile** : `Infant deaths` (nombre de décès d'enfants pour 1000 naissances)
- **Consommation d'alcool** : `Alcohol` (consommation par habitant (15+) en litres d'alcool pur)
- **Dépense de santé (% PIB)** : `Percentage expenditure` (dépenses de santé en pourcentage du PIB par habitant)
- **Hépatite B** : `Hepatitis B` (couverture vaccinale des enfants de 1 an en %)
- **Rougeole** : `Measles` (nombre de cas rapportés pour 1000 habitants)
- **Indice de masse corporelle (IMC)** : `BMI` (moyenne pour la population)
- **Mortalité des enfants de moins de 5 ans** : `Under-five deaths` (pour 1000 habitants)
- **Polio** : `Polio` (couverture vaccinale des enfants de 1 an en %)
- **Dépenses de santé totales** : `Total expenditure` (% des dépenses gouvernementales totales)
- **Diphtérie** : `Diphtheria` (couverture de vaccination DTP3 des enfants de 1 an en %)
- **Taux de SIDA et VIH** : `HIV/AIDS` (décès pour 1000 naissances vivantes chez les 0-4 ans)
- **Produit Intérieur Brut (PIB)** : `GDP` (en USD)
- **Minceur (10-19 ans)** : `Thinness prevalence (10-19 years)` (pourcentage)
- **Minceur (5-9 ans)** : `Thinness prevalence (5-9 years)` (pourcentage)
- **Indice de ressources** : `Income composition of resources` (indice de développement humain de 0 à 1)
- **Années de scolarité** : `Schooling` (nombre d'années de scolarité)

### Préparation et Nettoyage des Données

Nous avons nettoyé le jeu de données pour minimiser, voire éliminer, les valeurs manquantes et les valeurs aberrantes. Le fichier résultant, nommé cleaneddata.csv, est maintenant prêt pour nos analyses.


## « Developer Guide »
### Architecture du Code
Le projet est structuré en modules pour faciliter l'ajout de nouvelles pages et composants. Voici les principaux dossiers et fichiers du projet :

- main.py : Fichier principal qui configure les identifiants Kaggle, télécharge les données, les nettoie, puis lance le dashboard.

- /src : Contient les sous-modules pour des fonctions spécifiques.
    - /utils :
        - clean_data.py : Gère le chargement, le nettoyage, et la sauvegarde des données.
        - copy_json_file.py : Copie le fichier kaggle.json dans le dossier .kaggle de l'utilisateur.
        - get_data.py : Télécharge les données depuis Kaggle et renomme le fichier téléchargé.

    - /pages : Contient les pages de visualisation pour le dashboard, notamment DASH1 où se trouve la fonction create_dashboard() qui génère l'interface.

### Étapes d’Ajout d’une Page
Pour ajouter une nouvelle page dans le tableau de bord, suivez les étapes ci-dessous :

1. **Créer le fichier de la page :**    
Dans le dossier /src/pages, créez un fichier Python pour votre nouvelle page (par exemple, new_page.py). Dans ce fichier, définissez les éléments de la page, comme les titres, paragraphes, graphiques, ou autres composants.

2. **Définir la logique de présentation de la page :**  
Utilisez les modules Dash et Plotly pour créer les graphiques et la disposition de la page. Par exemple, utilisez dcc.Tabs pour ajouter un nouvel onglet et y insérer vos éléments.

3. **Intégrer la page dans DASH1.py :**
    - Importez votre nouvelle page dans DASH1.py et assurez-vous que la fonction de création de la page est disponible.

    - Ajoutez un nouvel onglet dans dcc.Tabs en utilisant dcc.Tab, et spécifiez votre contenu dans la section children. Vous pouvez également utiliser html.Div et dcc.Graph pour structurer le contenu et afficher les graphiques de votre page.

### Étapes d’Ajout d’un Graphique
Pour ajouter un nouveau graphique dans le tableau de bord, suivez les étapes ci-dessous :

1. **Créer une fonction pour le graphique :**   
Dans /src/components, créez une fonction pour générer le graphique. Utilisez Plotly pour créer des visualisations interactives, ou Matplotlib si vous souhaitez des graphiques plus basiques.

2. **Intégrer le graphique dans une page :**    
Importez la fonction graphique dans la page où vous souhaitez afficher le graphique et appelez-la dans un dcc.Graph pour l'afficher.


## « Rapport d’analyse »
### 
À travers divers **graphiques et cartes**, nous identifions des facteurs influençant les variations de l'espérance de vie, qu’elle soit en hausse ou en baisse.

### Comparaison des pays développés et en développement
- Dans les **pays développés**, l'espérance de vie dépasse systématiquement les **70 ans**.
- En revanche, dans les **pays en développement**, elle varie généralement entre **50 et 75 ans**.
- Les histogrammes révèlent qu’une majorité de pays atteignent un niveau d'espérance de vie acceptable. Cependant, plusieurs pays affichent encore des niveaux relativement faibles.

### Évolution de l'espérance de vie au fil du temps
- En **2015**, l'espérance de vie moyenne a augmenté par rapport à **2008**.
- **Cas spécifique de l'Afrique australe** : Grâce aux traitements du VIH, un gain d'environ **10 ans d'espérance de vie** a été observé entre **2000 et 2015**, illustrant l’impact direct des soins VIH sur l'espérance de vie.

### Impact de la vaccination et de la santé infantile
- **Pays développés** : Taux de vaccination proche de **100 %**.
- **Pays en développement** : La vaccination reste un défi majeur, entraînant des espérances de vie plus faibles. Ce constat souligne l’importance cruciale de la vaccination.
- En outre, les pays en développement présentent :
  - Des taux de **mortalité infantile** plus élevés.
  - Une **malnutrition** plus répandue, marquée par une forte minceur. Ces deux facteurs influencent directement l'espérance de vie.

### Conclusion
Notre tableau de bord met en lumière des **actions concrètes** que les pays développés pourraient envisager pour soutenir les pays en développement, comme l’assistance aux campagnes de vaccination.


## « Copyright » 
### Attestation sur l'honneur 
Nous  déclarons sur l’honneur que le code fourni a été produit par moi/nous même. 