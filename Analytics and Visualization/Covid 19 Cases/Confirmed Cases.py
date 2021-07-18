import plotly
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('Covid 19 Confirmed Cases.csv')# Reading the data
data = [go.Bar(
    x = df['Date'],
    y = df['Confirmed_Cases'],
)]


layout = go.Layout(
        xaxis=dict(
            title='Date',),
        yaxis=dict(
            title='Confirmed Cases',)
    )
fig = go.Figure(data=data, layout=layout)
fig.update_layout(title_text="Covid 19 Confirmed Cases")

#plotly.offline.plot(fig,filename='index.html',config={'displayModeBar': False})

fig.show()
