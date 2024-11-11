import os
import shutil

def setup_kaggle_credentials():
    """
    Copies kaggle.json from the main project folder to the user's .kaggle folder.
    Creates the .kaggle folder if it does not exist and verifies the file placement.
    """
    # Step 1: Define the universal path to the user's home directory
    home_dir = os.path.expanduser("~")

    # Step 2: Define the path to the .kaggle folder within the user's home directory
    kaggle_dir = os.path.join(home_dir, ".kaggle")

    # Step 3: Check if the .kaggle folder exists, if not, create it
    if not os.path.exists(kaggle_dir):
        os.makedirs(kaggle_dir)
        print(f"Created directory: {kaggle_dir}")
    else:
        print(f"Directory already exists: {kaggle_dir}")

    # Step 4: Locate the project folder containing kaggle.json
    # Traverse up directories to find the main project folder where kaggle.json is located
    current_dir = os.path.abspath(".")
    while current_dir != os.path.dirname(current_dir):  # Traverse up until root
        kaggle_json_path = os.path.join(current_dir, "kaggle.json")
        if os.path.isfile(kaggle_json_path):
            break  # Found the kaggle.json file
        current_dir = os.path.dirname(current_dir)

    if not os.path.isfile(kaggle_json_path):
        print("kaggle.json not found in the project folder. Make sure it's there before running this function.")
        return False

    # Step 5: Copy kaggle.json to the .kaggle folder in the user's home directory
    destination_path = os.path.join(kaggle_dir, "kaggle.json")
    try:
        shutil.copy(kaggle_json_path, destination_path)
        print(f"Copied kaggle.json to {destination_path}")

        # Verification step: Check if kaggle.json is in the .kaggle folder
        if os.path.isfile(destination_path):
            print("✅ Kaggle credentials setup completed successfully. kaggle.json is now in .kaggle folder.")
            return True
        else:
            print("❌ kaggle.json was not copied to the .kaggle folder.")
            return False

    except Exception as e:
        print(f"Failed to copy kaggle.json: {e}")
        return False
    
if __name__ == "__main__":
    setup_kaggle_credentials()
    