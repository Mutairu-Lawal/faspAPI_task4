import os
import shutil

# File type folders
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png"],
    "Documents": [".pdf", ".docx", ".txt"]
}


def organize_files(folder_path):
    if not os.path.isdir(folder_path):
        print("❌ Invalid folder path.")
        return

    try:
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path):
                ext = os.path.splitext(filename)[1].lower()
                for folder, extensions in FILE_TYPES.items():
                    if ext in extensions:
                        target_folder = os.path.join(folder_path, folder)
                        os.makedirs(target_folder, exist_ok=True)
                        shutil.move(file_path, os.path.join(
                            target_folder, filename))
                        print(f"Moved {filename} to {folder}/")
                        break
    except Exception as e:
        print(f"⚠️ Error organizing files: {e}")


def main():
    folder_path = input("Enter the folder path to organize: ").strip()
    organize_files(folder_path)


if __name__ == "__main__":
    main()
