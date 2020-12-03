import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from app import server
from app import app
# import all pages in the app
from apps import confirmed, deaths, recovered, home

##

##
# building the navigation bar
nav_item = dbc.NavItem(dbc.NavLink("Home", href='/home'))
# make a dropdown for the different pages
dropdown = dbc.DropdownMenu(
    children=[
        dbc.DropdownMenuItem("World Health Organization",
                             href='https://www.afro.who.int/about-us/contact-us'),
        dbc.DropdownMenuItem("Africa Centre for Disesase Control and Prevention", href='https://africacdc.org/contact-us/'),
    ],
    nav=True,
    in_navbar=True,
    label="Emergency Links",
)
drop_down = dbc.DropdownMenu(
    children=[
        dbc.DropdownMenuItem("Confirmed Cases", href="/confirmed"),
        dbc.DropdownMenuItem("Death Cases", href="/deaths"),
        dbc.DropdownMenuItem("Recovered Cases", href="/recovered"),
    ],
    nav = True,
    in_navbar = True,
    label = "Explore",
)
# Navbar Layout
navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src='/assets/log.png', height="50px",), width=4),
                        dbc.Col(dbc.NavbarBrand("Tracking COVID-19 in Africa", className="ml-2"), width=8),
                    ],
                    align="center",
                    no_gutters=True,
                ),
            ),
            dbc.NavbarToggler(id="navbar-toggler2"),
            dbc.Collapse(
                dbc.Nav(
                    [nav_item,navitem,drop_down,dropdown], className="ml-auto", navbar=True
                ),
                id="navbar-collapse2",
                navbar=True,
            ),
        ]
    ),
    color="primary",
    dark=True,
    className="mb-5",
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

for i in [2]:
    app.callback(
        Output(f"navbar-collapse{i}", "is_open"),
        [Input(f"navbar-toggler{i}", "n_clicks")],
        [State(f"navbar-collapse{i}", "is_open")],
    )(toggle_navbar_collapse)
# embedding the navigation bar
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    html.Div(id='page-content')
])
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/confirmed':
        return confirmed.layout
    elif pathname == '/deaths':
        return deaths.layout
    elif pathname == '/recovered':
        return recovered.layout
    else:
        return home.layout

if __name__ == '__main__':
    app.run_server(port=2010,debug=True)
