import csv
import json


def json_to_csv(json_data, output_file):
    """Convert a JSON array of objects to CSV, preserving all field names."""
    data = json.loads(json_data) if isinstance(json_data, str) else json_data
    if not isinstance(data, list) or not all(isinstance(row, dict) for row in data):
        raise ValueError("Expected a JSON array of objects")
    fields = list(dict.fromkeys(key for row in data for key in row))
    with open(output_file, "w", newline="", encoding="utf-8") as file:
        if fields:
            writer = csv.DictWriter(file, fieldnames=fields)
            writer.writeheader()
            writer.writerows(data)
    print(f"Success: Data converted to {output_file}")


if __name__ == "__main__":
    sample_data = [
        {"id": 1, "task": "Market Research", "priority": "high"},
        {"id": 2, "task": "Documentation", "priority": "medium"},
    ]
    json_to_csv(sample_data, "output.csv")
