import time
from openpyxl import load_workbook
from openpyxl import Workbook

load_wb = load_workbook("./2022mento.xlsx",data_only=True)

load_ws = load_wb['Sheet1']

write_wb = Workbook()
write_ws = write_wb.create_sheet('생성시트')
write_ws = write_wb.active

write_ws['J1'] = "입력"
i=1
while True:
    print(load_ws.cell(i,4).value)
    print(load_ws.cell(i,5).value)
    if(load_ws.cell(i,4).value==None):
        break
    # time.sleep(0.1)
    for cell in load_ws.rows[i]:
        write_ws.append(cell.value)
    i+=1

write_wb.save("./backup.xlsx")