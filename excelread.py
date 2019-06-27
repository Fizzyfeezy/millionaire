import xlrd
file_location = "C:/Users/Fizzyfeezy/PycharmProjects/tutorial/millionaire.xlsx"
workbook = xlrd.open_workbook(file_location)
sheet = workbook.sheet_by_index(0)
cell = sheet.cell_value(0, 0)
print(cell)