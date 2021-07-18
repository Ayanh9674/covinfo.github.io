import plotly
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('Covid 19 Goa Vaccination.csv')# Reading the data
data = [go.Bar(
    x = df['Date'],
    y = df['Vaccination'],
)]



#data= go.data.gapminder()
#df = pd.read_csv('Covid 19 Goa Vaccination.csv')

#data = [go.data.gapminder(
 #   x= df['Date'],
  #  y= df['Vaccination']
  #  )]
#fig = go.bar(data, x='year', y='pop')

#data_canada = data[data.country == 'Canada']
#fig = go.bar(Covid 19 Goa Vaccination.csv , x='Date', y='Vaccination',
 #            hover_data=['lifeExp', 'gdpPercap'], color='lifeExp',
  #           labels={'Vaccination'}, height=400)

layout = go.Layout(
        xaxis=dict(
            title='Date',),
        yaxis=dict(
            title='Vaccinated',)
    )
fig = go.Figure(data=data, layout=layout)
fig.update_layout(title_text="Covid 19 Vaccination in Goa")
#plotly.offline.plot(fig,filename='index.html',config={'displayModeBar': False})

fig.show()

#df = pd.read_csv('Covid 19 Goa Vaccination.csv')
#fig = px.histogram(df, x="Date", y="Vaccination")
#fig.update_layout(bargap=0.2)
#fig.update_layout(bargap=0.2)

#import plotly.express as px
#data = px.data.gapminder()

#data_canada = data[data.country == 'Canada']
#fig = px.bar(data_canada, x='year', y='pop',
 #            hover_data=['lifeExp', 'gdpPercap'], color='lifeExp',
  #           labels={'pop':'population of Canada'}, height=400)
#fig.show()




#import plotly.express as px
#data_canada = px.data.gapminder().query("country == 'Canada'")
#fig = px.bar(data_canada, x='year', y='pop')
#fig.show()
