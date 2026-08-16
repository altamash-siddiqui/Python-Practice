import os


FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"],
    "Documents": [".doc", ".docx", ".txt", ".rtf"],
    "PDFs": [".pdf"],
    "Spreadsheets": [".xls", ".xlsx", ".csv"],
    "Presentations": [".ppt", ".pptx"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".py", ".js", ".html", ".css", ".java", ".cpp", ".c"]
}


def get_file_category(filename):
    extension = os.path.splitext(filename)[1].lower()

    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return category

    return "Others"


def scan_folder(folder_path):
    if not os.path.exists(folder_path):
        print("❌ Folder does not exist.")
        return

    files = []

    for item in os.listdir(folder_path):
        full_path = os.path.join(folder_path, item)

        if os.path.isfile(full_path):
            files.append(item)

    print(f"\n📂 Total files found: {len(files)}")

    for file in files:
        category = get_file_category(file)
        print(f"{file:<35} → {category}")


def main():
    print("=" * 65)
    print("          SMART FILE ORGANIZER")
    print("=" * 65)

    folder = input("\nEnter folder path: ").strip()

    scan_folder(folder)


if __name__ == "__main__":
    main()