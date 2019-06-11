import pandas as pd

import plotly
import plotly.offline as py
import plotly.graph_objs as go
import plotly.figure_factory as ff
import cufflinks as cf

from collections import Counter

py.init_notebook_mode(connected=True)
cf.go_offline()

dataframe = pd.read_csv("/home/muhammad/Envs/tweet/code/CCA_for_Tweets/CCA_for_Dates_of_Tweets/created_datas/datetime_data.csv")

# print(dataframe.head())

trace0 = go.Scatter(
	x = list(Counter(sorted(dataframe["hours"])).keys()),
	y = list(Counter(sorted(dataframe["hours"])).values()),
	mode = 'lines + markers',
)

data = [trace0]

# py.plot(data, filename='basic-line.html')

monday = dataframe[dataframe["day_of_week"] == 1]
tuesday = dataframe[dataframe["day_of_week"] == 2]
wednesday = dataframe[dataframe["day_of_week"] == 3]
thursday = dataframe[dataframe["day_of_week"] == 4]
friday = dataframe[dataframe["day_of_week"] == 5]
saturday = dataframe[dataframe["day_of_week"] == 6]
sunday = dataframe[dataframe["day_of_week"] == 7]

Monday = go.Scatter(
	x = list(Counter(sorted(monday["hours"])).keys()),
	y = list(Counter(sorted(monday["hours"])).values()),
	mode = 'lines + markers',
	name= 'Monday'
)
Tuesday = go.Scatter(
	x = list(Counter(sorted(tuesday["hours"])).keys()),
	y = list(Counter(sorted(tuesday["hours"])).values()),
	mode = 'lines + markers',
	name = 'Tuesday'
)
Wednesday = go.Scatter(
	x = list(Counter(sorted(wednesday["hours"])).keys()),
	y = list(Counter(sorted(wednesday["hours"])).values()),
	mode = 'lines + markers',
	name = 'Wednesday'
)
Thursday = go.Scatter(
	x = list(Counter(sorted(thursday["hours"])).keys()),
	y = list(Counter(sorted(thursday["hours"])).values()),
	mode = 'lines + markers',
	name = 'Thursday'
)
Friday = go.Scatter(
	x = list(Counter(sorted(friday["hours"])).keys()),
	y = list(Counter(sorted(friday["hours"])).values()),
	mode = 'lines + markers',
	name = 'Friday'
)
Saturday = go.Scatter(
	x = list(Counter(sorted(saturday["hours"])).keys()),
	y = list(Counter(sorted(saturday["hours"])).values()),
	mode = 'lines + markers',
	name = 'Saturday'
)
Sunday = go.Scatter(
	x = list(Counter(sorted(sunday["hours"])).keys()),
	y = list(Counter(sorted(sunday["hours"])).values()),
	mode = 'lines + markers',
	name = 'Sunday'
)

data = [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]

# py.plot(data, filename='basic-line.html')
