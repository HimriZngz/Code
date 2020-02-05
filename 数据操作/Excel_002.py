import xlrd


# 用途：用来读取已经存在的excel里的数据

rb = xlrd.open_workbook(r'Excel_002.xlsx')

# 读取第一个表
sheet_1 = rb.sheet_by_index(0)  # 或者根据表名 sheet2 = workbook.sheet_by_name(sheet_name)

# 读取第4行的内容
row = sheet_1.row_values(3)
# 读取第2列的内容
col = sheet_1.col_values(1)

print(row)
print(col)
