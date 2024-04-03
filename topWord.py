import os
import json
import re
from collections import Counter

def get_most_used_words(directory):
    words_counter = Counter()

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
                # Extract words from the "Contents" field of each message
                for message in data:
                    contents = message.get("Contents", "")
                    # Split contents into words using regular expression
                    words = re.findall(r'\b\w+\b', contents.lower())
                    # Update word counts
                    words_counter.update(words)
    
    # Get the most common words
    most_common_words = words_counter.most_common(5000)  # Change 50 to the desired number of most common words
    
    return most_common_words

# Path to the directory containing the messages folder
directory_path = "C:/Users/Adrian/Desktop/DiscordData/data/messages"

# Get the most used words across all messages.json files
most_used_words = get_most_used_words(directory_path)

# Print the table header
print("{:<6} {:<20} {:<10}".format("Rank", "Word", "Amount"))

# Print the most used words in a table format
for i, (word, count) in enumerate(most_used_words, 1):
    print("{:<6} {:<20} {:<10}".format(i, word, count))

input("Press any key to exit")