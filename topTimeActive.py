import os
import json
from collections import Counter
from datetime import datetime

def get_top_data(directory):
    top_data = {}

    # Get top minutes
    top_data["Minutes"] = get_top_minutes(directory)

    # Get top hours
    top_data["Hours"] = get_top_hours(directory)

    
    # Get top weekdays
    top_data["Weekdays"] = get_top_weekdays(directory)

    # Get top months
    top_data["Months"] = get_top_months(directory)

    # Get top years
    top_data["Years"] = get_top_years(directory)

    return top_data

def get_top_hours(directory):
    hours_counter = Counter()

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
                # Extract timestamp from each message and aggregate counts per hour
                for message in data:
                    timestamp = message.get("Timestamp", "")
                    if timestamp:
                        # Parse timestamp to determine the hour
                        hour = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S").hour
                        hours_counter[hour] += 1
    
    # Get the top active hours
    top_hours = hours_counter.most_common(24)
    
    return top_hours

def get_top_minutes(directory):
    minutes_counter = Counter()

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
                # Extract timestamp from each message and aggregate counts per minute
                for message in data:
                    timestamp = message.get("Timestamp", "")
                    if timestamp:
                        # Parse timestamp to determine the minute
                        minute = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S").minute
                        minutes_counter[minute] += 1
    
    # Get the top active minutes
    top_minutes = minutes_counter.most_common(60)
    
    return top_minutes

def get_top_months(directory):
    months_counter = Counter()

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
                # Extract timestamp from each message and aggregate counts per month
                for message in data:
                    timestamp = message.get("Timestamp", "")
                    if timestamp:
                        # Parse timestamp to determine the month
                        month = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S").strftime('%B')
                        months_counter[month] += 1
    
    # Get the top active months
    top_months = months_counter.most_common(12)
    
    return top_months
def get_top_weekdays(directory):
    weekdays_counter = Counter()

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
                # Extract timestamp from each message and aggregate counts per weekday
                for message in data:
                    timestamp = message.get("Timestamp", "")
                    if timestamp:
                        # Parse timestamp to determine the weekday (0 = Monday, 6 = Sunday)
                        weekday = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S").weekday()
                        weekdays_counter[weekday] += 1
    
    # Get the top active weekdays
    top_weekdays = weekdays_counter.most_common(7)
    
    return [(get_weekday_name(day), count) for day, count in top_weekdays]

def get_weekday_name(day):
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return weekdays[day]

def get_top_years(directory):
    years_counter = Counter()

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
                # Extract timestamp from each message and aggregate counts per year
                for message in data:
                    timestamp = message.get("Timestamp", "")
                    if timestamp:
                        # Parse timestamp to determine the year
                        year = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S").year
                        years_counter[year] += 1
    
    # Get the top active years
    top_years = years_counter.most_common(20)
    
    return top_years

# Path to the directory containing the messages folder
directory_path = "data/messages"

# Get top data
top_data = get_top_data(directory_path)

# Print top data
for category, data in top_data.items():
    print("Most active " + category + ":")
    print("Rank".ljust(6) + category.ljust(10) + "Messages")
    for i, (item, count) in enumerate(data, 1):
        print(f"{str(i).ljust(6)}{str(item).ljust(10)}{count}")
    print()

input("Press any key to exit...")