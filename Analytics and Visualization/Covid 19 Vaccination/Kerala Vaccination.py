import plotly
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('Covid 19 Kerala Vaccination.csv')# Reading the data
data = [go.Bar(
    x = df['Date'],
    y = df['Vaccination'],
)]


layout = go.Layout(
        xaxis=dict(
            title='Date',),
        yaxis=dict(
            title='Vaccinated',)
    )
fig = go.Figure(data=data, layout=layout)
fig.update_layout(title_text="Covid 19 Vaccination in Kerala")

#plotly.offline.plot(fig,filename='index.html',config={'displayModeBar': False})

fig.show()

