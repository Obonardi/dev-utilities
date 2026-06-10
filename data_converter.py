import csv
import json

def json_to_csv(json_data, output_file):
    # Parse the data if it is a string
    data = json.loads(json_data) if isinstance(json_data, str) else json_data
    
    # Open CSV file for writing
    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        
        # Write the header
        if data:
            writer.writerow(data.keys())
            
            # Write the rows
            for entry in data:
                writer.writerow(entry.values())
    print(f"Success: Data converted to {output_file}")

if __name__ == "__main__":
    # Example data to convert
    sample_data = [
        {"id": 1, "task": "Market Research", "priority": "high"},
        {"id": 2, "task": "Documentation", "priority": "medium"}
    ]
    json_to_csv(sample_data, "output.csv")