import dash_html_components as html
import dash_bootstrap_components as dbc
# needed only if running this as a single page app
#external_stylesheets = [dbc.themes.LUX]

#app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# change to app.layout if running as single page app instead
layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(html.H1("Welcome to the Africa COVID-19 Tracking app ", style={'color':'white','font-variant':'small-caps'}, className="text-center")
                    , className="mb-5 mt-5")
        ]),
        html.Hr(),
        dbc.Row([
            dbc.Col(html.H5(children='This application is created by the data science team at The BluExpress Technologies for COVID-19 Tracing in Africa.'
                                     , style={'color':'white','font-variant':'small-caps'})
                    , className="mb-4")
            ]),
        dbc.Row([
            dbc.Col(html.H5(children='The data used in the development of this application was collected from the public repository for the Center of Systems Science and Engineering at the Johns Hopkins University.',
            style={'color':'white','font-variant':'small-caps'})
                    ,className="mb-5")
        ]),
        html.Hr(),
        html.Div([dbc.Row(dbc.Col(html.H2("Global numbers at a glance:\n", style={'color':'white','font-variant':'small-caps'})))]),
        html.Hr(),
        dbc.Row([
            dbc.Col(dbc.Card(children=[html.H3(children='Confirmed Cases',
                                               className="text-center"),
                                        html.P('64,508,175:\n Confirmed Cases', className = 'text-center'),
                                        html.Hr(),
                                        html.P('Last Updated:\n December 3, 2020', className = 'text-right'),
                                       ],
                             body=True, color="dark", outline=True)
                    , width=4, className="mb-4"),
            dbc.Col(dbc.Card(children=[html.H3(children='Death Cases',
                                               className="text-center"),
                                       html.P('1,492,998:\n Death Cases', className = 'text-center'),
                                       html.Hr(),
                                       html.P('Last Updated:\n December 3, 2020', className = 'text-right'),
                                       ],
                             body=True, color="dark", outline=True)
                    , width=4, className="mb-4"),
            dbc.Col(dbc.Card(children=[html.H3(children='Recovered Cases',
                                               className="text-center"),
                                       html.P('41,492,849:\n Recovered Cases', className = 'text-center'),
                                       html.Hr(),
                                       html.P('Last Updated:\n December 3, 2020', className = 'text-right'),

                                       ],
                             body=True, color="dark", outline=True)
                    , width=4, className="mb-4"),
                    ])
    ])
])

#if __name__ == '__main__':
#    app.run_server(port = 2020, debug=True)