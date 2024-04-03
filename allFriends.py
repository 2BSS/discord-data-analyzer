import json
from datetime import datetime

def get_relationships_sorted_by_date(users_json_path):
    with open(users_json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    relationships = data.get("relationships", [])
    
    # Parse and format the "since" field into a readable date format
    formatted_relationships = []
    for relationship in relationships:
        since = relationship.get("since", "")
        global_name = relationship.get("user", {}).get("global_name", "")
        if since:  # Check if the "since" field is not empty
            since_date = datetime.strptime(since, "%Y-%m-%dT%H:%M:%S.%f%z")
            formatted_since = since_date.strftime("%Y-%m-%d %H:%M:%S")
            formatted_relationships.append((formatted_since, global_name))
    
    # Sort relationships by date in descending order
    sorted_relationships = sorted(formatted_relationships, key=lambda x: x[0], reverse=True)
    
    return sorted_relationships

# Path to the users.json file
users_json_path = "data/account/user.json"

# Get relationships sorted by date descending
sorted_relationships = get_relationships_sorted_by_date(users_json_path)

# Print relationships by date descending
print("Relationships sorted by date (descending):")
for formatted_since, global_name in sorted_relationships:
    print(f"Since: {formatted_since}, Global Name: {global_name}")

input("Press any key to exit...")