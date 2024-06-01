import json

# Define the path to your JSON file
json_file_path = "Electronics_5.json"

# Open the JSON file for reading
with open(json_file_path, 'r') as file:
    # Read and process the file line by line
    for line in file:
        # Decode the JSON object from the current line
        obj = json.loads(line)

        # Check if the "vote" key exists in the JSON object
        if "vote" in obj:
            # Convert the value of the "vote" key to an integer
            if obj["vote"].isdigit():
                obj["vote"] = int(obj["vote"])
                # Print the new data type of the "vote" column
                print("New Data Type of 'vote' column:", type(obj["vote"]).__name__)
            else:
                print("Vote value is not a valid integer:", obj["vote"])

        # Process the decoded JSON object
        # Here you can perform any operations you need on the object
        print(obj)

        # Break the loop after processing the desired number of lines
        # You can remove this if you want to process the entire file
        break
