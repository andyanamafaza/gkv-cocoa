from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import json

app = Dash(__name__)

df = pd.read_csv("Area-kakao.csv")
df = df.drop(columns=["No"])

df_reshaped = df.melt(
    id_vars=["Provinsi"],
    var_name="Year",
    value_name="Luas Areal Kakao (Ha)"
)

with open("indonesia.geojson") as f:
    geojson = json.load(f)

colorscale = ["#E6DFDB", "#B09F93", "#58412F", "#38220F", "#38220F", "#290C19"]

app.layout = html.Div([
    html.H1(
        children='Visualisasi Data Luas Areal Kakao di Indonesia',
        style={
            'textAlign': 'center',
            'color': '#38220F'
        }
    ),
    html.Div([
        html.H2(
            children='Choropleth Map',
            style={
                'textAlign': 'center',
                'color': '#290C19'
            }
        ),
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
    ]),
    html.Div([
        html.H2(
            children='Time Series Chart',
            style={
                'textAlign': 'center',
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
    ],
        style={'margin-top': '20px', 'margin-bottom': '20px'}
    )
])


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


if __name__ == "__main__":
    app.run_server(debug=True)
