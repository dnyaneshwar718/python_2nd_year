import csv
import json

input_file = "data.csv"
output_file = "data.json"

try:
    with open(input_file, "r", newline="", encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data = list(csv_reader)

    with open(output_file, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, indent=4)

    print("CSV file successfully converted to JSON!")
    print("Input :", input_file)
    print("Output:", output_file)

except FileNotFoundError:
    print("Error: The file data.csv was not found.")
    print("Make sure data.csv is in the same folder as this Python file.")
except Exception as e:
    print("Error:", e)