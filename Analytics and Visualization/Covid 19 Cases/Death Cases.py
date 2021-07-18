import plotly
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('Covid 19 Death Cases.csv')# Reading the data
data = [go.Bar(
    x = df['Date'],
    y = df['Death'],
)]


layout = go.Layout(
        xaxis=dict(
            title='Date',),
        yaxis=dict(
            title='Death Cases',)
    )
fig = go.Figure(data=data, layout=layout)
fig.update_layout(title_text="Covid 19 Death Cases")

#plotly.offline.plot(fig,filename='index.html',config={'displayModeBar': False})

fig.show()

