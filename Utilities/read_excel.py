from openpyxl import load_workbook


# for DDT testdata
def get_login_data(filepath, sheetname):
    workbook = load_workbook(filepath)
    sheet = workbook[sheetname]
    data = []

    for row in sheet.iter_rows(min_row=2, values_only=True):
        username, password, expected_result = row
        data.append((username,password, expected_result))
    return  data

# for Admin testdata
def get_admin_user_data(filepath,sheetName):
    workbook = load_workbook(filepath)
    sheet = workbook[sheetName]
    data = []

    for row in sheet.iter_rows(min_row=2,values_only=True):
        data.append(row[:7])
    return data

