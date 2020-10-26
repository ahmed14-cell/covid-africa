import pandas as pd 
import plotly.graph_objs as go 
import cufflinks as cf 
import dash_core_components as dcc 
import dash_html_components as html 
import dash_bootstrap_components as dbc 
from dash.dependencies import Input, Output
import plotly.express as px
import os
import colorcet as cl
px.set_mapbox_access_token(os.environ.get('TOKEN'))
af = pd.read_csv('data/africa.csv')
df = pd.read_csv('data/latest.csv')
df = df.rename(columns = {'Country_Region':'Country', 'Long_':'Long','Case-Fatality_Ratio':'C.F.R'})
df = df.drop(['FIPS','Admin2','Combined_Key','Province_State'], axis = 1)
y = list(af['Country'])
df = df[df['Country'].isin(y)]
small = df.nsmallest(10, columns = 'Deaths')
large = df.nlargest(10, columns = 'C.F.R')
colors = ['#d73027','#f46d43','#fdae61','#fee090','#ffffbf','#e0f3f8','#abd9e9','#74add1','#4575b4']
fig = px.scatter_mapbox(df,lat='Lat',lon='Long',color='Deaths',hover_name='Country',size = 'Deaths',
                        hover_data={'Lat':False, 'Long':False}, labels = {'Country':'Deaths'}, color_continuous_scale='pinkyl',
                        zoom=2, template='plotly_dark',center=None, width=1900, height=700, mapbox_style='dark',title='COVID-19 Death Cases in Africa')
fig1 = go.Figure(go.Indicator(
        mode = "gauge+number+delta",
        value = df.Deaths.sum(axis = 0),
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "Total Death Cases", 'font': {'size': 32,'family': 'Overpass'}},
        gauge = {
            'axis': {'range': [None, 30000], 'tickwidth': 1, 'tickcolor': "darkblue"},
            'bar': {'color': "dodgerblue"},
            'bgcolor': "#1a1a1a",
            'borderwidth': 2,
            'bordercolor': "#1a1a1a"}))
fig1.update_layout(paper_bgcolor = "#1a1a1a", font = {'color': "tomato", 'family': "Overpass"})
fig2 = large.iplot(asFigure = True, kind = 'pie', labels = 'Country', values = 'Incidence_Rate', textinfo = 'label', textposition = 'outside', textcolor = 'white',
                    gridcolor = '#1a1a1a', dimensions = (950,500), sort = True, linecolor = 'white', hole = .2, pull = .03, legend = True,colorscale = 'rdylgn',
                    theme = 'solar',title = 'Countries with the Highest Incidence Rate in Africa')
fig3 = small.iplot(asFigure = True, kind = 'barh',  x = 'Country', y = 'Deaths', xTitle = 'Death Cases', yTitle = 'Region',
                    title = 'African Countries with Lowest Death Cases', theme = 'solar', colors =colors, dimensions = (950,500), gridcolor = '#1a1a1a')
fig4 = df.iplot(asFigure = True, kind = 'scatter', mode = 'lines' , x = 'Country', y = 'C.F.R', yTitle = 'C.F.R', xTitle = 'Countries', colorscale = 'prgn',
                theme = 'solar', title = 'Case Fatality Ratio per Country', dimensions = (950,450), gridcolor = '#1a1a1a', interpolation = 'spline')
#external_stylesheets = [
#    dbc.themes.LUX,
#    'assets/style.css']

#app = dash.Dash('__name__', external_stylesheets = external_stylesheets, assets_external_path = 'https://gacaldata.000webhostapp.com/assets')
layout = html.Div([
dbc.Row([html.Div([
            dbc.Col(html.Div([
                        dcc.Graph(id='Chart5',
                                figure = fig1,
                                animate = True,
                                config = {
                                    'showTips': True,
                                    'responsive': True,
                                    'displaylogo':False
                                })], style = {'color':'#ffffff','font-variant':'small-caps','font-weight':'bold'}), width = 6),
            dbc.Col(html.Div([
                        dcc.Graph(id='Chart6',
                                figure = fig4,
                                animate = True,
                                config = {
                                    'showTips': True,
                                    'responsive': True,
                                    'displaylogo':False
                                })], style = {'color':'#ffffff','font-variant':'small-caps','font-weight':'bold'}), width = 6),
            ], className = 'row'),
        ], style = {'color':'#ffffff','font-variant':'small-caps','font-weight':'bold'}),
dbc.Row(dbc.Col(html.Div([
                    html.Div([
                        dcc.Graph(id='Chart7',
                            figure = fig,
                            animate = True,
                            config = {
                                'showTips': True,
                                'responsive': True,
                                'displaylogo':False,
                                'scrollZoom' : False
                            })], className = 'auto', style = {'color':'#ffffff','font-variant':'small-caps','font-weight':'bold'}),
                    ], className = 'row'),
), style={'color':'#ffffff','font-variant':'small-caps'}),
dbc.Row([html.Div([
            dbc.Col(html.Div([
                        dcc.Graph(id='Chart8',
                                figure = fig3,
                                animate = True,
                                config = {
                                    'showTips': True,
                                    'responsive': True,
                                    'displaylogo':False
                                })], style = {'color':'#ffffff','font-variant':'small-caps','font-weight':'bold'}), width = 6),
            dbc.Col(html.Div([
                        dcc.Graph(id='Chart9',
                                figure = fig2,
                                animate = True,
                                config = {
                                    'showTips': True,
                                    'responsive': True,
                                    'displaylogo':False
                                })], style = {'color':'#ffffff','font-variant':'small-caps','font-weight':'bold'}), width = 6),
        
            ], className = 'row'),
        ]),
]),

