import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from plot import *
from plotly.graph_objs import *

external_stylesheets = [dbc.themes.COSMO]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Home", href="/", active=True)),
        dbc.NavItem(dbc.NavLink("Page 1", href="/page-1")),
        dbc.NavItem(dbc.NavLink("Page 2", href="/page-2")),
    ],
    brand="JW Dashboard",
    color="#ffbb00",
    dark=True,
)

sample = get_sample_data()

fig = px.line(sample, y=['ACWI', 'BOND', 'USO', 'GOVT'],
              color_discrete_sequence=['salmon', 'orange', 'gold', 'green', 'blue', 'purple', 'black'])

fig.update_xaxes(title=None)
fig.update_yaxes(title=None)
fig.update_layout(title='<b>ACWI Jul 2019 ~ Jan 2023<b>',
                  title_font=dict(size=15, ),
                  
                  # 출력 화면에 따른 자동 크기조절
                  autosize=True,

                  # 배경색
                  plot_bgcolor = 'rgba(0,0,0,0)',
                  paper_bgcolor = 'rgba(0,0,0,0)',
                  
                  # 사이즈
                  height=500,

                  # 범례 설정 
                  legend_orientation="h",
                  legend_yanchor='bottom',
                  legend_y=-0.15,
                  legend_xanchor='left',
                  legend_x=0.0,

                  # 출처 등 annotations
                  annotations=[
                        dict(
                            text="Data Source: Yahoo Finance",
                            x=0,
                            y=-0.2,
                            xref="paper",
                            yref="paper",
                            showarrow=False
                        )
                  ])



sidebar = html.Div(
    [
        html.H2("Sidebar", className="display-4"),
        html.P("A simple sidebar layout with navigation links", className="lead"),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active=True),
                dbc.NavLink("Page 1", href="/page-1"),
                dbc.NavLink("Page 2", href="/page-2"),
            ],
            vertical="md",
            pills=True,
        ),
    ],
    style={"background-color": "#f8f9fa", "height": "100vh"},
)

data = {
    "Header 1": ["Data 1", "Data 4", "Data 7"],
    "Header 2": ["Data 2", "Data 5", "Data 8"],
    "Header 3": ["Data 3", "Data 6", "Data 9"],
}
df = pd.DataFrame(data)

home_layout = html.Div(
    [
        html.H1("Home"),
        html.P("This is Page 2 with a 3x3 graph and table."),
        dbc.Row(
            [
                dbc.Col(
                    dcc.Graph(
                        figure=fig
                    ),
                    width=6,
                ),
                dbc.Col(
                    dcc.Graph(
                        figure=fig
                    ),
                    width=6,
                ),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    dcc.Graph(
                        figure=fig
                    ),
                    width=6,
                ),
                dbc.Col(
                    dcc.Graph(
                        figure=fig
                    ),
                    width=6,
                ),
            ]
        ),
        dbc.Row([
            dbc.Col(
                #dbc.Table.from_dataframe(get_performance(sample,'ACWI'), striped=True, bordered=True, hover=True),
                ),
            dbc.Col(
                #dbc.Table.from_dataframe(get_performance(sample, 'BOND'), striped=True, bordered=True, hover=True),
                ),
        ])
    ],
    style={"background-color": "#ffffff"},
)

page1_layout = html.Div(
    [
        html.H1("Page 2"),
        html.P("This is Page 2 with a 3x3 graph and table."),
        dbc.Row(
            [
                dbc.Col(
                    dcc.Graph(
                        figure={
                            "data": [
                                {"x": [1, 2, 3, 4], "y": [4, 2, 1, 3], "type": "line", "line": {"color": "rgb(255, 188, 0)"}}
                            ],
                            "layout": {"title": "Graph 1"},
                        }
                    ),
                    width=4,
                ),
                dbc.Col(
                    dcc.Graph(
                        figure={
                            "data": [
                                {"x": [1, 2, 3, 4], "y": [4, 3, 2, 4], "type": "line", "line": {"color": "rgb(255, 188, 0)"}}
                            ],
                            "layout": {"title": "Graph 2"},
                        }
                    ),
                    width=4,
                ),
                dbc.Col(
                    dcc.Graph(
                        figure={
                            "data": [
                                {"x": [1, 2, 3, 4], "y": [2, 4, 3, 1], "type": "line", "line": {"color": "rgb(255, 188, 0)"}}
                            ],
                            "layout": {"title": "Graph 3"},
                        }
                    ),
                    width=4,
                ),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    dcc.Graph(
                        figure={
                            "data": [
                                {"x": [1, 2, 3, 4], "y": [4, 2, 1, 3], "type": "bar", "marker": {"color": "rgb(96, 88, 76)"}}
                            ],
                            "layout": {"title": "Graph 1"},
                        }
                    ),
                    width=4,
                ),
                dbc.Col(
                    dcc.Graph(
                        figure={
                            "data": [
                                {"x": [1, 2, 3, 4], "y": [4, 3, 2, 4], "type": "bar", "marker": {"color": "rgb(96, 88, 76)"}}
                            ],
                            "layout": {"title": "Graph 2"},
                        }
                    ),
                    width=4,
                ),
                dbc.Col(
                    dcc.Graph(
                        figure={
                            "data": [
                                {"x": [1, 2, 3, 4], "y": [2, 4, 3, 1], "type": "bar", "marker": {"color": "rgb(96, 88, 76)"}}
                            ],
                            "layout": {"title": "Graph 3"},
                        }
                    ),
                    width=4,
                ),
            ]
        ),
        dbc.Row([
            dbc.Col(
                dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True),),
            dbc.Col(
                dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True),),
            dbc.Col(
                dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True),),
        ])
    ],
    style={"background-color": "#ffffff"},
)

page2_layout = html.Div(
    [
        html.H1("Page 2"),
        html.P("This is Page 2 with a 3x3 graph and table."),
        dbc.Row(
            [
                dbc.Col(
                    dcc.Graph(
                        figure={
                            "data": [
                                {"x": [1, 2, 3, 4], "y": [4, 2, 1, 3], "type": "line", "line": {"color": "rgb(255, 188, 0)"}}
                            ],
                            "layout": {"title": "Graph 1"},
                        }
                    ),
                    width=3,
                ),
                dbc.Col(
                    dcc.Graph(
                        figure={
                            "data": [
                                {"x": [1, 2, 3, 4], "y": [4, 3, 2, 4], "type": "line", "line": {"color": "rgb(255, 188, 0)"}}
                            ],
                            "layout": {"title": "Graph 2"},
                        }
                    ),
                    width=3,
                ),
                dbc.Col(
                    dcc.Graph(
                        figure={
                            "data": [
                                {"x": [1, 2, 3, 4], "y": [2, 4, 3, 1], "type": "line", "line": {"color": "rgb(255, 188, 0)"}}
                            ],
                            "layout": {"title": "Graph 3"},
                        }
                    ),
                    width=3,
                ),
                dbc.Col(
                    dcc.Graph(
                        figure={
                            "data": [
                                {"x": [1, 2, 3, 4], "y": [2, 4, 3, 1], "type": "line", "line": {"color": "rgb(255, 188, 0)"}}
                            ],
                            "layout": {"title": "Graph 4"},
                        }
                    ),
                    width=3,
                ),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    dcc.Graph(
                        figure={
                            "data": [
                                {"x": [1, 2, 3, 4], "y": [4, 2, 1, 3], "type": "bar", "marker": {"color": "rgb(96, 88, 76)"}}
                            ],
                            "layout": {"title": "Graph 1"},
                        }
                    ),
                    width=3,
                ),
                dbc.Col(
                    dcc.Graph(
                        figure={
                            "data": [
                                {"x": [1, 2, 3, 4], "y": [4, 3, 2, 4], "type": "bar", "marker": {"color": "rgb(96, 88, 76)"}}
                            ],
                            "layout": {"title": "Graph 2"},
                        }
                    ),
                    width=3,
                ),
                dbc.Col(
                    dcc.Graph(
                        figure={
                            "data": [
                                {"x": [1, 2, 3, 4], "y": [2, 4, 3, 1], "type": "bar", "marker": {"color": "rgb(96, 88, 76)"}}
                            ],
                            "layout": {"title": "Graph 3"},
                        }
                    ),
                    width=3,
                ),
                dbc.Col(
                    dcc.Graph(
                        figure={
                            "data": [
                                {"x": [1, 2, 3, 4], "y": [2, 4, 3, 1], "type": "bar", "marker": {"color": "rgb(96, 88, 76)"}}
                            ],
                            "layout": {"title": "Graph 4"},
                        }
                    ),
                    width=3,
                ),
            ]
        ),
        dbc.Row([
            dbc.Col(
                dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True),),
            dbc.Col(
                dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True),),
            dbc.Col(
                dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True),),
            dbc.Col(
                dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True),),
        ])
    ],
    style={"background-color": "#ffffff"},
)

app.layout = html.Div(
    [
        dcc.Location(id="url", refresh=False),
        navbar,
        dbc.Row(
            [   
                dbc.Col(
                    html.Div(id="page-content"),
                    #width=10,
                    style={"padding-left": 15, "padding-top": 15},
                ),
            ],
            style={"margin": 0, "display": "flex"},
            className="flex-nowrap",
        ),
    ],
    style={"display": "grid", "background-color": "#ffffff"},
)



@app.callback(
    dash.dependencies.Output("page-content", "children"),
    [dash.dependencies.Input("url", "pathname")],
)
def render_page_content(pathname):
    if pathname == "/":
        return home_layout
    elif pathname == "/page-1":
        return page1_layout
    elif pathname == "/page-2":
        return page2_layout
    else:
        return "404: Page not found"


if __name__ == "__main__":
    app.run_server(port=8888, debug=True)
