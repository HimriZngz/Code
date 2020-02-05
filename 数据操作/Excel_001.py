import xlwt


# 用途：用来重新构建一个excel，从建表开始，然后往里面写入数据。

wb = xlwt.Workbook()
sheet = wb.add_sheet('sheet 001')

sheet.write(0, 0, 'data')
wb.save('Excel_001.xlsx')
