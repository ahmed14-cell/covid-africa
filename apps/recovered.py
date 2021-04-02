import os
import pandas as pd 
import plotly.graph_objs as go 
import cufflinks
import dash_core_components as dcc 
import dash_html_components as html 
import dash_bootstrap_components as dbc 
from dash.dependencies import Input, Output
import plotly.express as px
import colorcet as cl

px.set_mapbox_access_token(os.environ.get('TOKEN'))

af = pd.read_csv('data/africa.csv')
df = pd.read_csv('data/latest.csv')

df.rename(columns={
    'Country_Region':'Country',
    'Long_': 'Long',
    'Case_Fatality_Ratio': 'C.F.R'
}, inplace=True)

df.drop([
    'FIPS','Admin2','Combined_Key','Province_State'
], axis=1, inplace=True)

y = list(af['Country'])
df = df[df['Country'].isin(y)]


small = df.nsmallest(10, columns='Recovered')
large = df.nlargest(10, columns='Active')

colors = [
    '#d73027', '#f46d43', '#fdae61', '#fee090', '#ffffbf', '#e0f3f8', '#abd9e9', '#74add1', '#4575b4'
]

fig = px.scatter_mapbox(df,lat='Lat',lon='Long',color='Recovered', zoom=2,
                        hover_name='Country',size = 'Recovered',center=None,
                        hover_data={'Lat':False, 'Long':False}, width=1900,
                        labels={'Country':' Recovered'}, height=700,
                        color_continuous_scale='brwnyl', mapbox_style='dark',
                        template='plotly_dark',
                        title='COVID-19 Recovered Cases in Africa')

fig1 = large.iplot(asFigure=True, kind='pie', labels='Country', sort=True,
                   values='Active', textinfo='label', textposition='outside',
                   textcolor='white', gridcolor='#1a1a1a', dimensions=(950,500),
                   linecolor='white', hole=.2, pull=.03, legend=True, 
                   colorscale='rdylgn', theme='solar',
                   title='Countries with the Most Active Cases in Africa' )

fig2 = small.iplot(asFigure=True, kind='barh', x='Country', y='Recovered', 
                   xTitle='Recovery Cases', yTitle='Country', theme='solar',
                   title='African Countries with Lowest Recovery Cases', 
                   colors=colors, dimensions=(950,500), gridcolor='#1a1a1a')

fig3 = go.Figure(go.Indicator(
    mode="number+delta",
    value=df.Active.sum(axis=0),
    domain={'x': [0, 1], 'y': [0, 1]},
    title={
        'text': "Latest Active Cases", 'font': {
            'size': 30,'family': 'Overpass'
        }
    }))
fig3.update_layout(paper_bgcolor="#121212", font={
    'color': "tomato", 'size':26, 'family': "Overpass"
})

fig4 = px.bar_polar(df, r='C.F.R', color="C.F.R", theta=af.Region, width=950,
                    template="plotly_dark", color_continuous_scale=cl.coolwarm,
                    title='Case Fatality Ratio in African Regions', height=500)

layout = html.Div([
dbc.Row([html.Div([
            dbc.Col(html.Div([
                        dcc.Graph(id='Chart10',
                                figure=fig3,
                                animate=True,
                                config={
                                    'showTips': True,
                                    'responsive': True,
                                    'displaylogo':False
                                })], style={
                                    'color': '#ffffff',
                                    'font-variant': 'small-caps',
                                    'font-weight':'bold'
                                }), width=6),
            dbc.Col(html.Div([
                        dcc.Graph(id='Chart11',
                                figure=fig4,
                                animate=True,
                                config={
                                    'showTips': True,
                                    'responsive': True,
                                    'displaylogo':False
                                })], style={
                                    'color': '#ffffff',
                                    'font-variant': 'small-caps',
                                    'font-weight': 'bold'
                                }), width=6),
        
            ], className='row'),
        ]),
dbc.Row(dbc.Col(html.Div([
                    html.Div([
                        dcc.Graph(id='Chart12',
                            figure=fig,
                            animate=True,
                            config={
                                'showTips': True,
                                'responsive': True,
                                'displaylogo':False,
                                'scrollZoom': False
                            })], className='auto', style={
                                'color':'#ffffff','font-variant':'small-caps','font-weight':'bold'
                            }),
                    ], className='row'), width=12,
), style={'color':'#ffffff','font-variant':'small-caps'}),

dbc.Row([html.Div([
            dbc.Col(html.Div([
                        dcc.Graph(id='Chart13',
                                figure=fig1,
                                animate=True,
                                config={
                                    'showTips': True,
                                    'responsive': True,
                                    'displaylogo':False
                                })], style={
                                    'color':'#ffffff',
                                    'font-variant': 'small-caps',
                                    'font-weight': 'bold'
                                }), width=6),
            dbc.Col(html.Div([
                        dcc.Graph(id='Chart14',
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

