import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import warnings

warnings.filterwarnings('ignore')
discrete_sequence = ['salmon', 'orange', 'gold', 'green', 'blue', 'purple', 'black']

def fig_update(fig, title, data_source):
    fig.update_xaxes(title=None)
    fig.update_yaxes(title=None)
    fig.update_layout(title=title,
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
                                text=data_source,
                                x=0,
                                y=-0.2,
                                xref="paper",
                                yref="paper",
                                showarrow=False
                            )
                    ])
    return fig

def line_plot(df, x, y, title=None, data_source=None):
    fig = px.line(df, x=x, y=y,
              color_discrete_sequence=discrete_sequence)

    fig = fig_update(fig, title, data_source)
    return fig

def facet_area_plot(df, facet_col, facet_col_wrap=2, title=None, data_source=None):
    fig = px.area(df, facet_col=facet_col, facet_col_wrap=facet_col_wrap,
              color_discrete_sequence=discrete_sequence)
    
    fig = fig_update(fig, title, data_source)
    return fig

def scatter_plot(df, x, y, title=None, data_source=None):
    fig = px.scatter(df, x=x, y=y,
              color_discrete_sequence=discrete_sequence)
    fig = fig_update(fig, title, data_source)
    return fig

def bar_plot(df, x, y, title=None, data_source=None):
    fig = px.bar(df, x=x, y=y,
              color_discrete_sequence=discrete_sequence)
    fig = fig_update(fig, title, data_source)
    return fig

def group_bar_plot(df, x, y, color_column, title=None, data_source=None):
    fig = px.histogram(df, x=x, y=y, barmode='group', color=color_column,
              color_discrete_sequence=discrete_sequence)
    fig = fig_update(fig, title, data_source)
    return fig

def pie_plot(df, values, names, title=None, data_source=None, hole=0.0):
    fig = px.pie(df, values=values, names=names, hole=hole,
              color_discrete_sequence=discrete_sequence)

    fig = fig_update(fig, title, data_source)

    return fig

def box_plot(df, x, y, color = None, title=None, data_source=None):
    fig = px.box(df, x=x, y=y, color=color,
              color_discrete_sequence=discrete_sequence)

    fig = fig_update(fig, title, data_source)

    return fig

def bubble_plot(df, x, y, size, color, log_x=False, title=None, data_source=None):
    fig = px.scatter(df, x=x, y=y, size=size, color=color, log_x=log_x,
              color_discrete_sequence=discrete_sequence)

    fig = fig_update(fig, title, data_source)

    return fig

def tree_map(df, path, value, color, color_continuous_scale='Edge', title=None, data_source=None):
    # 예시 path = [px.Constant("world"), 'continent', 'country']
    fig = px.treemap(df,  path=path, values=value,
                color=color, color_continuous_scale=color_continuous_scale,
                color_continuous_midpoint=np.average(df[color], weights=df[value]))
    
    fig = fig_update(fig, title, data_source)

    return fig

def radar_plot(category, score_value, title=None, data_source=None):
    df = pd.DataFrame({
        'r':category,
        'theta':score_value})
    
    fig = px.line_polar(df, r='r', theta='theta', line_close=True,
                    color_discrete_sequence=discrete_sequence)
    
    fig = fig_update(fig, title, data_source)

    return fig

def heat_map(array, title=None, data_source=None):
    fig = go.Figure(data=go.Heatmap(
                    z=array))
    fig = fig_update(fig, title, data_source)

    return fig

def heat_map_v2(array, color_continuous_scale='Edge', title=None, data_source=None):
    fig = px.imshow(array, color_continuous_scale=color_continuous_scale)

    fig = fig_update(fig, title, data_source)

    return fig