import pandas as pd 
import plotly.graph_objs as go 
import cufflinks as cf 
import dash_core_components as dcc 
import dash_html_components as html 
import dash_bootstrap_components as dbc 
from dash.dependencies import Input, Output
import plotly.express as px
import os
af = pd.read_csv('data/africa.csv')
df = pd.read_csv('data/latest.csv')

df.rename(columns={
    'Country_Region':'Country', 'Long_':'Long', 'Case_Fatality_Ratio':'C.F.R'
    }, inplace=True)
df.drop(['FIPS','Admin2','Combined_Key','Province_State'], axis=1, inplace=True)

y = list(af['Country'])
df = df[df['Country'].isin(y)]

small = df.nsmallest(10, columns='Confirmed')
large = df.nlargest(10, columns='C.F.R')

color = [
    '#d73027', '#f46d43','#fdae61', '#fee090', '#ffffbf', '#e0f3f8', '#abd9e9', '#74add1', '#4575b4'
]

px.set_mapbox_access_token(os.environ.get('TOKEN'))

colors = [
    '#d73027', '#f46d43', '#fdae61', '#fee08b', '#ffffbf', '#d9ef8b', '#a6d96a', '#66bd63', '#1a9850'
]

fig = px.scatter_mapbox(df,lat='Lat',lon='Long',color='Confirmed',
                        hover_name='Country',size = 'Confirmed',
                        hover_data={'Lat':False, 'Long':False},
                        labels = {'Country':'Confirmed'},zoom=2.3, height=700,
                        color_continuous_scale=color, width=1900, center=None,
                        template='plotly_dark', mapbox_style='dark',
                        title='COVID-19 Confirmed Cases in Africa')

fig1 = df.iplot(asFigure=True, kind='bar', barmode='overlay', x='Country',
                y='Incident_Rate', xTitle='Regions', yTitle='Incidence Rate',
                colorscale='piyg', theme='solar', dimensions=(950,500),
                gridcolor = '#1a1a1a',
                title='COVID-19 Incidence Rate in Africa', orientation='v')

fig2 = large.iplot(asFigure=True, kind='pie', labels='Country', values='C.F.R',
                   textinfo='label', textposition='outside', textcolor='white',
                   gridcolor='#1a1a1a', dimensions=(950,500), sort=True,
                   linecolor='white', hole=.2, pull=.03, legend=True,
                   colors=colors,theme = 'solar',
                   title = 'Countries with the Highest Case-Fatality Ratio')

fig3 = small.iplot(asFigure=True, kind='barh', x='Country', y='Confirmed',
                   xTitle='Confirmed Cases', yTitle='Region',theme='solar',
                   title='African Countries with Low Confirmed Cases',
                   colorscale='rdylgn', dimensions=(950,500), gridcolor='#1a1a1a')

fig4 = df.iplot(asFigure=True, kind='scatter', mode='lines', x='Country',
                y='Active', yTitle='Active Cases', xTitle='Countries',
                colors=color, theme='solar', dimensions=(950,500),
                gridcolor='#1a1a1a', interpolation='spline',
                title='Latest Active Cases per country')
#external_stylesheets = [
#    dbc.themes.LUX,
#    'assets/style.css']

#app = dash.Dash('__name__', external_stylesheets = external_stylesheets, assets_external_path = 'https://gacaldata.000webhostapp.com/assets')
layout = html.Div([
dbc.Row([html.Div([
            dbc.Col(html.Div([
                        dcc.Graph(id='Chart',
                                figure=fig1,
                                animate=True,
                                config={
                                    'showTips': True,
                                    'responsive': True,
                                    'displaylogo':False
                                })], style={'color':'#ffffff','font-variant':'small-caps','font-weight':'bold'}), width=6),
            dbc.Col(html.Div([
                        dcc.Graph(id='Chart1',
                                figure=fig2,
                                animate=True,
                                config={
                                    'showTips': True,
                                    'responsive': True,
                                    'displaylogo':False
                                })], style={'color':'#ffffff','font-variant':'small-caps','font-weight':'bold'}), width=6),
        
            ], className='row'),
        ], style={'color':'#ffffff','font-variant':'small-caps','font-weight':'bold'}),
dbc.Row(dbc.Col(html.Div([
                    html.Div([
                        dcc.Graph(id='Chart2',
                            figure=fig,
                            animate=True,
                            config={
                                'showTips': True,
                                'responsive': True,
                                'displaylogo':False,
                                'scrollZoom': False
                            })], className='auto', style={'color':'#ffffff','font-variant':'small-caps','font-weight':'bold'}),
                    ], className='row'),
), style={'color':'#ffffff','font-variant':'small-caps'}),
dbc.Row([html.Div([
            dbc.Col(html.Div([
                        dcc.Graph(id='Chart3',
                                figure=fig3,
                                animate=True,
                                config={
                                    'showTips': True,
                                    'responsive': True,
                                    'displaylogo':False
                                })], style={'color':'#ffffff','font-variant':'small-caps','font-weight':'bold'}), width=6),
            dbc.Col(html.Div([
                        dcc.Graph(id='Chart4',
                                figure=fig4,
                                animate=True,
                                config={
                                    'showTips': True,
                                    'responsive': True,
                                    'displaylogo':False
                                })], style={'color':'#ffffff','font-variant':'small-caps','font-weight':'bold'}), width=6),
        
            ], className='row'),
        ]),
]),

