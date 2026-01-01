# Import the csv module to read/write CSV files
import csv


def get_login_data(filepath):
    """
    Reads login data from a CSV file and returns it as a list of tuples.

    :param filepath: Path to the CSV file containing login data
                     The CSV should have columns: username, password, expected_result
    :return: List of tuples in the format (username, password, expected_result)
    """

    data = []  # Initialize an empty list to store login data

    # Open the CSV file in read mode with UTF-8 encoding (removes BOM if present)
    with open(filepath, newline='', mode='r', encoding='utf-8-sig') as csvfile:
        # Create a DictReader to read the CSV rows as dictionaries (column_name: value)
        reader = csv.DictReader(csvfile)

        # Iterate over each row in the CSV
        for row in reader:
            # Extract username, password, and expected_result and store as a tuple
            data.append((row['username'], row['password'], row['expected_result']))

    # Return the list of login data tuples
    return data


