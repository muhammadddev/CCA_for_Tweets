import pandas as pd

import plotly
import plotly.offline as py
import plotly.graph_objs as go
import plotly.figure_factory as ff
import cufflinks as cf

from collections import Counter

py.init_notebook_mode(connected=True)
cf.go_offline()

dataframe = pd.read_csv("/home/muhammad/Envs/tweet/code/datetime_data.csv")

trace0 = go.Scatter(
	x = list(Counter(sorted(dataframe["day_of_week"])).keys()),
	y = list(Counter(sorted(dataframe["day_of_week"])).values()),
	mode = 'lines + markers',
)

data = [trace0]

py.plot(data, filename='basic-line.html')

x = list(Counter(sorted(dataframe["hours"])).values())
hist_data = [x]
group_labels = ['distplot']

fig = ff.create_distplot(hist_data, group_labels)
# py.plot(fig, filename='Basic_Distplot.html')
