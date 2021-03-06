import dash
import dash_bootstrap_components as dbc

# bootstrap theme
# https://bootswatch.com/lux/
external_stylesheets = [dbc.themes.LUX]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

#if __name__ =='__main':
#    app.run_server(port=2020, debug=True)

app.title = 'COVID-19 in Africa'
app.config.suppress_callback_exceptions = True