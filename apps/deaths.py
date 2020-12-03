import os
import pandas as pd 
import plotly.graph_objs as go 
import cufflinks as cf 
import dash_core_components as dcc 
import dash_html_components as html 
import dash_bootstrap_components as dbc 
from dash.dependencies import Input, Output
import plotly.express as px

px.set_mapbox_access_token(os.environ.get('TOKEN'))

af = pd.read_csv('data/africa.csv')
df = pd.read_csv('data/latest.csv')

df.rename(columns={
    'Country_Region':'Country', 'Long_':'Long', 'Case_Fatality_Ratio':'C.F.R'
}, inplace=True)

df.drop([
    'FIPS','Admin2','Combined_Key','Province_State'
], axis=1, inplace=True)

y = list(af['Country'])
df = df[df['Country'].isin(y)]

small = df.nsmallest(10, columns = 'Deaths')
large = df.nlargest(10, columns = 'C.F.R')

colors = [
    '#d73027', '#f46d43', '#fdae61', '#fee090', '#ffffbf', '#e0f3f8', '#abd9e9', '#74add1', '#4575b4'
]

fig = px.scatter_mapbox(df,lat='Lat',lon='Long',color='Deaths', center=None,
                        hover_name='Country',size = 'Deaths', zoom=2,
                        hover_data={'Lat':False, 'Long':False}, width=1900,
                        labels={'Country':'Deaths'}, color_continuous_scale='pinkyl',
                        template='plotly_dark', height=700, mapbox_style='dark',
                        title='COVID-19 Death Cases in Africa')

fig1 = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=df.Deaths.sum(axis=0),
        domain={'x': [0, 1], 'y': [0, 1]},
        title={
            'text': "Total Death Cases", 'font': {
                'size': 32,'family': 'Overpass'
            }},
        gauge={
            'axis': {
                'range': [None, df.Deaths.sum()], 'tickwidth': 1, 'tickcolor':"darkblue"
            },
            'bar': {'color': "dodgerblue"},
            'bgcolor': "#1a1a1a",
            'borderwidth': 2,
            'bordercolor': "#1a1a1a"}))
fig1.update_layout(paper_bgcolor="#1a1a1a", font={
    'color': "tomato", 'family': "Overpass"
})
fig2 = large.iplot(asFigure=True, kind='pie', labels='Country',sort=True,
                   values='Incident_Rate', textinfo='label', linecolor='white',
                   textposition='outside', textcolor='white', hole=.2, pull=.03,
                   gridcolor='#1a1a1a', dimensions=(950,500), legend=True,
                   colorscale='rdylgn', theme='solar',
                   title = 'Countries with the Highest Incidence Rate in Africa')

fig3 = small.iplot(asFigure=True, kind='barh', x='Country', y='Deaths',
                   xTitle='Death Cases', yTitle='Region', theme = 'solar',
                   colors=colors, dimensions=(950,500), gridcolor='#1a1a1a',
                   title = 'African Countries with Lowest Death Cases')

fig4 = df.iplot(asFigure=True, kind='scatter', mode='lines', x='Country',
                y='C.F.R', yTitle='C.F.R', xTitle='Countries', theme='solar',
                colorscale='prgn', dimensions=(950,450), gridcolor='#1a1a1a',
                interpolation='spline', title='Case Fatality Ratio per Country')

layout = html.Div([
dbc.Row([html.Div([
            dbc.Col(html.Div([
                        dcc.Graph(id='Chart5',
                                figure=fig1,
                                animate=True,
                                config={
                                    'showTips': True,
                                    'responsive': True,
                                    'displaylogo':False
                                })], style={
                                    'color':'#ffffff','font-variant':'small-caps','font-weight':'bold'
                                }), width=6),
            dbc.Col(html.Div([
                        dcc.Graph(id='Chart6',
                                figure=fig4,
                                animate=True,
                                config={
                                    'showTips': True,
                                    'responsive': True,
                                    'displaylogo':False
                                })], style={
                                    'color':'#ffffff','font-variant':'small-caps','font-weight':'bold'
                                }), width=6),
            ], className='row'),
        ], style={
            'color':'#ffffff','font-variant':'small-caps','font-weight':'bold'
        }),
dbc.Row(dbc.Col(html.Div([
                    html.Div([
                        dcc.Graph(id='Chart7',
                            figure=fig,
                            animate=True,
                            config={
                                'showTips': True,
                                'responsive': True,
                                'displaylogo':False,
                                'scrollZoom' : False
                            })], className='auto', style={
                                'color':'#ffffff','font-variant':'small-caps','font-weight':'bold'
                            }),
                    ], className='row'),
), style={'color':'#ffffff','font-variant':'small-caps'}),
dbc.Row([html.Div([
            dbc.Col(html.Div([
                        dcc.Graph(id='Chart8',
                                figure=fig3,
                                animate=True,
                                config={
                                    'showTips': True,
                                    'responsive': True,
                                    'displaylogo':False
                                })], style={
                                    'color':'#ffffff','font-variant':'small-caps','font-weight':'bold'
                                }), width=6),
            dbc.Col(html.Div([
                        dcc.Graph(id='Chart9',
                                figure=fig2,
                                animate=True,
                                config={
                                    'showTips': True,
                                    'responsive': True,
                                    'displaylogo':False
                                })], style={
                                    'color':'#ffffff','font-variant':'small-caps','font-weight':'bold'
                                }), width=6),
        
            ], className='row'),
        ]),
]),

