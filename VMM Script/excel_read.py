def main():
 import json
 from openpyxl import load_workbook
 workbook = load_workbook(filename="VMM.xlsx")
 sheet =workbook.active
 i=1
 while (i <=309):
  EPG1=sheet["A"+str(i)].value
  Tenant1=sheet["B"+str(i)].value
  APP1=sheet["C"+str(i)].value
  Domain1=sheet["E"+str(i)].value
  Data=("'Tenant' : '{}'".format(Tenant1), "'APP' : '{}'".format(APP1),"'EPG' : '{}'".format(EPG1),"'Domain' : '{}'".format(Domain1))
  Data1 = list(Data)
  print(Data1)
  print(" ")
  i=i+1
if __name__ == '__main__':
 main()
