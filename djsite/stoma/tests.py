import csv
from datetime import datetime, timedelta
import requests
import dateutil.parser






with open('data.csv', 'r', encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        # print(row)
        headers = {'Content-Type': 'application/json'}  # Указываем, что отправляем JSON
        print(row)
        start_time = row[3][:4] + "20" + row[3][4:] if len(row[3]) == 12 else row[3][:5] + "20" + row[3][5:]
        end_time = row[4][:4] + "20" + row[4][4:] if len(row[3]) == 12 else row[4][:5] + "20" + row[4][5:]

        data = {
            "add_time": row[2],
            "start_time": start_time,
            "end_time": end_time,
            "cancel_time": row[12],
            "card_comment": row[13],
            "reception_comment": row[14],
            "clinic": row[1],
            "doctor": row[6],
            "patient": row[8],

        }

        add_time = dateutil.parser.parse(data["add_time"])
        print(add_time)

        # print(data)
        # add_time = datetime.strptime(data["add_time"], "%d/%m/%Y %H:%M:%S")
        # print(add_time, type(add_time))
        response = requests.post(url="http://localhost:8000/api/v1/index/", headers=headers, json=data)

# time_now = datetime.strptime("05.06.2024 13:34:23", "%d.%m.%Y %H:%M:%S")
#
# given_time = datetime.strptime("06.06.2024 13:34:23", "%d.%m.%Y %H:%M:%S")
#
# print((time_now - given_time).days)