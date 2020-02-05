import openpyxl
# 这个模块只能用于 .xlsx 文件

# 用途：复制一个excel然后修改另存为一下


# 读取一个文件
excel = openpyxl.load_workbook(r'Excel_002.xlsx')

# 读出第一个表
sheet = excel.worksheets[0]

for i, row in enumerate(sheet.rows):
    # 把每一行的第三列更改为999
    row[2].value = 999

excel.save('Excel_003.xlsx')
