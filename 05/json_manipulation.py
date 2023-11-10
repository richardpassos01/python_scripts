import json
from datetime import datetime
import os

def process_json(input_data):
    # Print the Payee ID value
    payee_id = input_data["payee"]["id"]
    print(f"Payee ID: {payee_id}")

    # Find and print invoices containing the text "583"
    invoices_with_583 = [invoice for invoice in input_data["invoiceIds"] if "583" in invoice]
    print("Invoices containing '583':", invoices_with_583)

    # Change date/time fields to text in the format ‘%Y-%m-%dT%H:%M:%S’
    input_data["claimDateTime"] = datetime.fromtimestamp(input_data["claimDateTime"] / 1e3).strftime('%Y-%m-%dT%H:%M:%S')
    input_data["fileDateTime"] = datetime.fromtimestamp(input_data["fileDateTime"] / 1e3).strftime('%Y-%m-%dT%H:%M:%S')
    input_data["receivedDateTime"] = datetime.fromtimestamp(input_data["receivedDateTime"] / 1e3).strftime('%Y-%m-%dT%H:%M:%S')

    return input_data

def main():
    script_directory = os.path.dirname(os.path.abspath(__file__))
    json_file_path = os.path.join(script_directory, "json_manipulation.json")

    with open(json_file_path, "r") as file:
        json_data = json.load(file)

    modified_data = process_json(json_data)

    output_file_path = os.path.join(script_directory, "output.json")

    with open(output_file_path, "w") as output_file:
        json.dump(modified_data, output_file, indent=2)

    print("JSON document has been modified and written to output.json")

if __name__ == "__main__":
    main()