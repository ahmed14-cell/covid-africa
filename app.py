import pandas as pd 
import numpy as np 
import plotly.graph_objs as go 
import cufflinks as cf 
import dash 
import dash_core_components as dcc 
import dash_html_components as html 
import dash_bootstrap_components as dbc 
from dash.dependencies import Input, Output
import plotly.express as px


df = pd.read_csv('data/global.csv')
df.head()

df1 = df.drop(['Province/State','Country/Region','Lat','Long'], axis = 1)

df1 = df1.sum(axis = 1)

df1 = df1.to_frame(name = 'Total')

df = pd.merge(df, df1, left_index = True, right_index = True)
df

px.set_mapbox_access_token('pk.eyJ1IjoiYWhtZWRpdG8xNCIsImEiOiJja2NubTNmNmgwY216MnFsdnc3ZThyMzJ4In0.3mYybVWSnj-Lv0MG40bWZQ')

death = pd.read_csv('data/death.csv')
death.head()

death1 = death.drop(['Province/State','Country/Region','Lat','Long'], axis = 1)

death1 = death1.sum(axis = 1)

death1 = death1.to_frame(name = 'Total Deaths')

death = pd.merge(death, death1, left_index = True, right_index = True)
death

val = death.columns

fig = px.scatter_mapbox(data_frame=df, lat='Lat', lon='Long', color='Total', hover_name='Country/Region',size = 'Total', hover_data={'Lat':False, 'Long':False}, labels = {'Country/Region':'Total'}, color_continuous_scale=px.colors.sequential.Plotly3, zoom=2, center=None, mapbox_style='light', title='Global Confirmed COVID-19 Cases')
fig

fig_1 = px.scatter_mapbox(data_frame=death, lat='Lat', lon='Long', color='Total Deaths', hover_name='Country/Region',size = 'Total Deaths', hover_data={'Lat':False, 'Long':False}, labels = {'Country/Region':'Total Deaths'}, color_continuous_scale=px.colors.sequential.Plotly3, zoom=1.5, center=None, width=1900, height=700, mapbox_style='light', title='Global COVID-19 Death Cases')
fig_1

fig_1_bar = death.iplot(asFigure = True, kind = 'bar', orientation = 'h', barmode = 'overlay', legend = True, x = 'Continent', y = 'Total Deaths', xTitle = 'Total COVID-19 Deaths', yTitle = 'Continents', title = 'Global COVID_19 Deaths', colorscale = 'piyg', theme = 'pearl', dimensions = (1200,338))
fig_1_bar

pie = death.iplot(asFigure = True, kind = 'pie', labels = 'Continent', values = 'Total Deaths', theme = 'pearl', colorscale = 'ylorbr', hole = .1, pull = .02, textinfo = 'label+percent', textposition = 'inside', textcolor = 'black', legend = True, title = 'Comparison of Death Cases in all Continents', dimensions = (950,400))
pie

fig2 = death.iplot(asFigure = True, kind = 'bar', x = 'Country/Region', y = val.all(), theme = 'pearl', colorscale = 'rdylbu', yTitle = 'COVID-19 Death Cases', title = 'Global COVID-19 Mortality Rates', dimensions = (950,400))
fig2


external_stylesheets = [
    dbc.themes.LUX]

app = dash.Dash('__name__', external_stylesheets = external_stylesheets, assets_external_path = 'https://gacaldata.000webhostapp.com/assets')

server = app.server

app.title = 'BluExpress Technologies'
colors = {
    'text':'#6072D4',
    'plot_color':'#4C3960',
    'paper_color':'#F5F6F7',
    'background':'#ffffff'
}


nav_item = dbc.NavItem(dbc.NavLink("BluExpress Technologies"))

# make a reuseable dropdown for the different examples
dropdown = dbc.DropdownMenu(
    children=[
        dbc.DropdownMenuItem("World Health Organization",
                             href='https://www.who.int/emergencies/contact'),
        dbc.DropdownMenuItem("Centre for Disesase Control and Prevention", href='https://wwwn.cdc.gov/dcs/contactus/form'),
    ],
    nav=True,
    in_navbar=True,
    label="Emergency Links",
)

# Navbar Layout
navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src='https://gacaldata.000webhostapp.com/assets/logo1.jpg', height="40px")),
                        dbc.Col(dbc.NavbarBrand("Covid-19 Dashboard", className="ml-2")),
                    ],
                    align="center",
                    no_gutters=True,
                ),
            ),
            dbc.NavbarToggler(id="navbar-toggler2"),
            dbc.Collapse(
                dbc.Nav(
                    [nav_item,
                     dropdown,
                     ], className="ml-auto", navbar=True
                ),
                id="navbar-collapse2",
                navbar=True,
            ),
        ]
    ),
    color="light",
    dark=False,
    className="mb-5",
)

app.layout = html.Div(
    html.Div([navbar,
html.Div([
        html.Div([
            dcc.Graph(id='chart1',
                      figure = fig_1_bar,
                      animate = True,
                      config = {
                          'showTips': True,
                          'responsive': True,
                          'displaylogo':False
                      })], className = 'six columns'),
        html.Div([
            dbc.Jumbotron(
    [
        dbc.Container(
            [
            html.H1("Death Cases", className="display-1"),
            html.P(
            "774,053 COVID-19 Death Cases Globally",
            className="lead",
            ),
            html.Hr(className="my-2"),
            html.P(
            "Last Update:\n A few seconds ago"
            ),
            ], fluid = True,
        ),
    ], fluid = True,
)
        ], className = 'six columns')
], className = 'row'),

dbc.Row(dbc.Col(html.Div([
                    html.Div([
                        dcc.Graph(id='chart',
                            figure = fig_1,
                            animate = True,
                            config = {
                                'showTips': True,
                                'responsive': True,
                                'displaylogo':False
                            })], className = 'auto'),
                    ], className = 'row'),
)),

dbc.Row([html.Div([
            dbc.Col(html.Div([
                        dcc.Graph(id='chart3',
                                figure = fig2,
                                animate = True,
                                config = {
                                    'showTips': True,
                                    'responsive': True,
                                    'displaylogo':False
                                })]), width = 6),
            dbc.Col(html.Div([
                        dcc.Graph(id='chart2',
                                figure = pie,
                                animate = True,
                                config = {
                                    'showTips': True,
                                    'responsive': True,
                                    'displaylogo':False
                                })]), width = 6),
        
            ], className = 'row'),
        ]),




])
)

if __name__ == '__main__':
    app.run_server(debug = True, port = 2050)
