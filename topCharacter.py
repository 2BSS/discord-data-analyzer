import os
import json
from collections import Counter

def get_top_50_characters(directory):
    character_counter = Counter()

    # Traverse through the directory structure
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Check if the file is messages.json
            if file == "messages.json":
                # Get the full path of the messages.json file
                file_path = os.path.join(root, file)
                # Read the contents of the messages.json file
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                # Concatenate "Contents" of all messages
                all_contents = ''.join([message.get("Contents", "") for message in data])
                # Update character counts
                character_counter.update(all_contents)
    
    # Get the top 50 most used characters
    top_50_characters = character_counter.most_common(500)  # Top 50 characters
    
    return top_50_characters

# Path to the directory containing the messages folder
directory_path = "data/messages"

# Get the top 50 most used characters from all "Contents"
top_50_characters = get_top_50_characters(directory_path)

# Print the top 50 most used characters
print("Top 50 Most Used Characters:")
for char, count in top_50_characters:
    print(f"'{char}': {count}")

input("Press any key to exit")
