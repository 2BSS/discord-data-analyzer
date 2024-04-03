import os

def get_message_json_folders(directory):
    message_json_folders = {}

    # Traverse through the directory structure
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Check if the file is messages.json
            if file == "messages.json":
                # Get the folder name containing the messages.json file
                folder_name = os.path.basename(root)
                # Get the size of the file
                file_path = os.path.join(root, file)
                file_size = os.path.getsize(file_path)
                # Store the folder name and file size in a dictionary
                message_json_folders[folder_name] = file_size
    
    # Sort the dictionary by file size in descending order
    sorted_folders = sorted(message_json_folders.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_folders

# Path to the directory containing the messages folder
directory_path = "data/messages"

# Get the sorted folder names and file sizes of messages.json files
sorted_folders = get_message_json_folders(directory_path)

# Print the sorted folder names and file sizes
for folder, size in sorted_folders:
    print(f"Folder: {folder}, Size: {size} bytes")

input("Press any key to exit")