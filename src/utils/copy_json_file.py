import os
import shutil

def setup_kaggle_credentials():
    """
    Copie le fichier kaggle.json du dossier principal du projet vers le dossier .kaggle de l'utilisateur.
    Crée le dossier .kaggle s'il n'existe pas et vérifie le placement du fichier.
    """
    #Définissez le chemin universel vers le répertoire personnel de l'utilisateur
    home_dir = os.path.expanduser("~")

    #Définissez le chemin vers le dossier .kaggle dans le répertoire personnel de l'utilisateur
    kaggle_dir = os.path.join(home_dir, ".kaggle")

    #Vérifiez si le dossier .kaggle existe, sinon, créez-le
    if not os.path.exists(kaggle_dir):
        os.makedirs(kaggle_dir)
        print(f"Dossier créé: {kaggle_dir}")
    else:
        print(f"Le dossier existe déjà: {kaggle_dir}")

    #Localisez le dossier du projet contenant le fichier kaggle.json
    #Remontez les répertoires pour trouver le dossier principal du projet où se trouve kaggle.json
    current_dir = os.path.abspath(".")
    while current_dir != os.path.dirname(current_dir):
        kaggle_json_path = os.path.join(current_dir, "kaggle.json")
        if os.path.isfile(kaggle_json_path):
            break
        current_dir = os.path.dirname(current_dir)

    if not os.path.isfile(kaggle_json_path):
        print("kaggle.json introuvable dans le dossier du projet. Assurez-vous qu'il s'y trouve avant d'exécuter cette fonction.")
        return False

    #Copiez le fichier kaggle.json vers le dossier .kaggle dans le répertoire personnel de l'utilisateur
    destination_path = os.path.join(kaggle_dir, "kaggle.json")
    try:
        shutil.copy(kaggle_json_path, destination_path)
        print(f"Fichier kaggle.json copié vers {destination_path}")

        #Vérifiez si le fichier kaggle.json se trouve dans le dossier .kaggle
        if os.path.isfile(destination_path):
            print("✅ Configuration des identifiants Kaggle terminée avec succès. Le fichier kaggle.json est maintenant dans le dossier .kaggle.")
            return True
        else:
            print("❌ Le fichier kaggle.json n'a pas été copié dans le dossier .kaggle.")
            return False

    except Exception as e:
        print(f"Échec de la copie du fichier kaggle.json: {e}")
        return False
    
if __name__ == "__main__":
    setup_kaggle_credentials()
