import requests
import pandas as pd
import openpyxl
import xlsxwriter
import fuuuuunc

url = "https://pskgu-api.onrender.com/groups?name=0481-06"
params = {
    'param1': 'значение1',
    'param2': 'значение2'
}

response = requests.get(url, params=params)

excel_file_path = 'C:\\Users\\dom\\Desktop\\окей мы просто играем в жизнь.xlsx'

workbook = openpyxl.load_workbook(excel_file_path)
worksheet = workbook.active


if response.status_code == 200:
    data = response.json()["days"]
else:
    print(f"Ошибка запроса: {response.status_code}")

def wriiite(lol, s):
    st = fuuuuunc.summator228(s)-2
    current_column=0
    for k, v in lol.items():
        current_column = int(k) + 66
        worksheet[f"{chr(current_column)}{st}"] = v

for k in data:
    wriiite(fuuuuunc.filtr(data.get(k)), k)


workbook.save(excel_file_path)