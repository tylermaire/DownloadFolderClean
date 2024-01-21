import os
import shutil

def organize_downloads(download_folder_path):
    # Define a mapping of file extensions to folder names
    file_type_to_folder = {
        '.jpg': 'Images',
        '.jpeg': 'Images',
        '.png': 'Images',
        '.gif': 'Images',
        '.pdf': 'PDFs',
        '.docx': 'Documents',
        '.xlsx': 'Spreadsheets',
        '.pptx': 'Presentations',
        '.txt': 'TextFiles',
        '.mp3': 'Music',
        '.mp4': 'Videos',
        '.zip': 'Archives',
        '.rar': 'Archives'
        # Add more file types and folders as needed
    }

    # Create all folders upfront
    for folder in set(file_type_to_folder.values()):
        folder_path = os.path.join(download_folder_path, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # Move files to corresponding folders
    for filename in os.listdir(download_folder_path):
        file_path = os.path.join(download_folder_path, filename)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1].lower()
            folder_name = file_type_to_folder.get(file_extension)
            if folder_name:
                shutil.move(file_path, os.path.join(download_folder_path, folder_name, filename))

# Replace '[YourUsername]' with your actual username on your Mac
download_folder_path = '/Users/[YourUsername]/Downloads'
organize_downloads(download_folder_path)

