import csv

def get_login_data(filepath):
    data = []
    with open(filepath, newline='', mode='r', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append((row['username'],row["password"],row["expected_result"]))
    return data


