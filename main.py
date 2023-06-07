import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import json
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

external_stylesheets = ["https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap"]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv("Areal-Kakao.csv")
df = df.drop(columns=["No"])

df_reshaped = df.melt(
    id_vars=["Provinsi"],
    var_name="Year",
    value_name="Luas Areal Kakao (Ha)"
)

with open("indonesia.geojson") as f:
    geojson = json.load(f)

colorscale = ["#E6DFDB", "#B09F93", "#58412F", "#38220F", "#38220F", "#290C19"]

app.layout = html.Div(
    style={
        "fontFamily": "Roboto, sans-serif"
    },
    children=[
        html.H1(
            children='Visualisasi Data Luas Areal Kakao di Indonesia',
            style={
                'textAlign': 'center',
                'color': '#38220F'
            }
        ),
        html.Div(
            style={
                "textAlign": "center",
                "color": "#290C19"
            },
            children=[
                html.H2(children='Choropleth Map'),
                dcc.Graph(
                    id="choropleth-map",
                    figure=px.choropleth(
                        df_reshaped,
                        geojson=geojson,
                        locations="Provinsi",
                        featureidkey="properties.state",
                        animation_frame="Year",
                        color="Luas Areal Kakao (Ha)",
                        color_continuous_scale=colorscale,
                        labels={"Luas Areal Kakao (Ha)": "Luas Areal Kakao (Ha)"},
                    ).update_geos(fitbounds="locations", visible=False).update_traces(
                        hovertemplate="<b>%{location}</b><br>Luas Areal Kakao: %{z} Ha"
                    ),
                    style={'width': '100%', 'height': '710px'}
                )
            ]
        ),
        html.Div(
            style={'margin-top': '20px', 'margin-bottom': '20px','textAlign': 'center'},
            children=[
                html.H2(
                    children='Time Series Chart',
                    style={
                        'color': '#290C19'
                    }
                ),
                dcc.Graph(id="time-series-chart"),
                html.P("Select province(s):"),
                dcc.Dropdown(
                    id="province-dropdown",
                    options=[{"label": x, "value": x}
                             for x in df_reshaped["Provinsi"].unique()],
                    value=[df_reshaped["Provinsi"].unique()[0]],
                    multi=True,
                    clearable=False
                )
            ]
        ),
        html.Div(
            style={'margin-top': '20px', 'margin-bottom': '20px', 'text-align': 'center'},
            children=[
                html.H2(children='Pie Chart', style={'color': '#290C19'}),
                dcc.Graph(
                    id="pie-chart",
                    style={'width': '100%', 'height': '710px', 'margin-left': 'auto', 'margin-right': 'auto',
                           'display': 'block'}
                ),
                html.P("Select a year:"),
                dcc.Dropdown(
                    id="year-dropdown",
                    options=[{"label": year, "value": year} for year in df_reshaped["Year"].unique()],
                    value=df_reshaped["Year"].unique()[0],
                    clearable=False
                ),
            ]
        )
    ]
)


@app.callback(
    Output("time-series-chart", "figure"),
    Input("province-dropdown", "value")
)
def display_time_series(selected_provinces):
    filtered_df = df_reshaped[df_reshaped["Provinsi"].isin(selected_provinces)]

    fig = px.line(
        filtered_df,
        x="Year",
        y="Luas Areal Kakao (Ha)",
        color="Provinsi",
        labels={"Luas Areal Kakao (Ha)": "Luas Areal Kakao (Ha)"},
    )
    fig.update_layout(transition_duration=500)

    return fig


@app.callback(
    Output("pie-chart", "figure"),
    Input("year-dropdown", "value")
)
def display_pie_chart(selected_year):
    filtered_df = df_reshaped[df_reshaped["Year"] == selected_year]
    total_by_province = filtered_df.groupby("Provinsi")["Luas Areal Kakao (Ha)"].sum()

    hover_text = [
        f"Provinsi: {province}<br>Luas Tanah: {area} Ha"
        for province, area in zip(total_by_province.index, total_by_province.values)
    ]

    fig = go.Figure(data=go.Pie(
        labels=total_by_province.index,
        values=total_by_province.values,
        hoverinfo="text",
        text=hover_text,
        textinfo="percent",
        textposition="inside"
    ))

    fig.update_layout(transition_duration=500)

    return fig



if __name__ == "__main__":
    app.run_server(debug=True)
