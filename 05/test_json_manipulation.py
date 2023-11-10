import unittest
import json
import os
from datetime import datetime
from json_manipulation import main

class TestProcessJson(unittest.TestCase):
    def setUp(self):
        script_directory = os.path.dirname(os.path.abspath(__file__))
        self.json_output_file_path = os.path.join(script_directory, "output.json")
        main()

    def tearDown(self):
        try:
            os.remove(self.json_output_file_path)
        except FileNotFoundError:
            pass

    def test_process_json(self):
        # Read in the document from a file
        with open(self.json_output_file_path, "r") as file:
            modified_data_from_file = json.load(file)

        # Verify if the modifications were done correctly
        self.assertEqual(modified_data_from_file["payee"]["id"], 9999)

        # Check if all expected invoices are present in the modified data
        expected_invoices = ["XXA15839", "XXA25829"]
        for invoice in expected_invoices:
            self.assertIn(invoice, modified_data_from_file["invoiceIds"])

        # Check if any invoices containing "583" are present
        for invoice in modified_data_from_file["invoiceIds"]:
            if "583" in invoice:
                self.assertTrue(True)
                break
        else:
            self.assertTrue(False, "Nenhuma fatura contendo '583' encontrada.")

        # Change any date/time fields to text in the format ‘%Y-%m-%dT%H:%M:%S’
        self.assertEqual(
            modified_data_from_file["claimDateTime"],
            datetime.fromtimestamp(1634860244000 / 1e3).strftime('%Y-%m-%dT%H:%M:%S')
        )
        self.assertEqual(
            modified_data_from_file["fileDateTime"],
            datetime.fromtimestamp(1634860244000 / 1e3).strftime('%Y-%m-%dT%H:%M:%S')
        )
        self.assertEqual(
            modified_data_from_file["receivedDateTime"],
            datetime.fromtimestamp(1634922275533 / 1e3).strftime('%Y-%m-%dT%H:%M:%S')
        )

if __name__ == '__main__':
    unittest.main()
