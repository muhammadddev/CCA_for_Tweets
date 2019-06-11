import datetime

import pandas as pd

data = open("/home/muhammad/Envs/tweet/code/CCA_for_Tweets/CCA_for_Dates_of_Twee/created_datas/dates.txt", "r", encoding="utf-8")
data = data.read()
# print(data)

datas = []
for date in data.splitlines():
	datas.append(date)
	# print(date)

dataframe = pd.DataFrame(datas, columns=['actual_dates'])

dates_and_times = []
for row in dataframe["actual_dates"]:
	for date_and_time in row.split(" "):
		dates_and_times.append(date_and_time)

# print(dates_and_times)

times = []
dates = []
for i in range(int(len(dates_and_times)/2)):
	times.append(dates_and_times[2*i + 1])
	dates.append(dates_and_times[2*i])


dataframe["dates"] = dates
dataframe["times"] = times

hours = []
minutes = []
secconds = []
for row in dataframe["times"]:
	splited_time = row.split(":")
	hours.append(splited_time[0])
	minutes.append(splited_time[1])
	secconds.append(splited_time[2])

dataframe["hours"] = hours
dataframe["minutes"] = minutes
dataframe["seconds"] = secconds

years = []
months = []
days = []
for row in dataframe["dates"]:
	splited_date = row.split("-")
	years.append(splited_date[0])
	months.append(splited_date[1])
	days.append(splited_date[2])

dataframe["years"] = years
dataframe["months"] = months
dataframe["days"] = days

days_of_week = []
for date in dataframe["dates"]:
	day_of_week = datetime.datetime.strptime(date, '%Y-%m-%d').strftime('%u')
	days_of_week.append(day_of_week)

dataframe["day_of_week"] = days_of_week

dataframe.to_csv('/home/muhammad/Envs/tweet/code/CCA_for_Tweets/CCA_for_Dates_of_Tweets/created_datas/datetime_data.csv', encoding='utf-8')
