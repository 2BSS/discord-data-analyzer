import os
import json
from datetime import datetime

def get_first_message(directory):
    first_message = None
    earliest_timestamp = None

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
                # Iterate through messages to find the earliest timestamp
                for message in data:
                    timestamp = message.get("Timestamp", "")
                    # Convert timestamp to datetime object
                    message_time = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
                    # Check if this is the earliest message
                    if earliest_timestamp is None or message_time < earliest_timestamp:
                        earliest_timestamp = message_time
                        first_message = message
    
    return first_message

# Path to the directory containing the messages folder
directory_path = "data/messages"

# Get the first message ever sent
first_message = get_first_message(directory_path)

# Print the first message
if first_message:
    print("First Message Ever Sent:")
    print(first_message)
else:
    print("No messages found.")

input("Press any key to exit")
