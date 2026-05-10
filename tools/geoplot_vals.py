import pandas as pd
import plotly.express as px


def geoplot_vals(dataset: pd.DataFrame, loc_col: str, val_col: str):
    fig = px.choropleth(
        dataset,
        locations=loc_col,
        locationmode='ISO-3',
        color=val_col,
        color_continuous_scale='RdYlBu',
        range_color=(-1, 1),
        projection='natural earth',
    )

    fig.update_geos(
        showcoastlines=True, coastlinecolor='black', coastlinewidth=0.5,
        showland=True, landcolor='lightgray',
        showocean=True, oceancolor='aliceblue',
        showcountries=True, countrycolor='black', countrywidth=0.3,
        showlakes=True, lakecolor='aliceblue',
        showrivers=False,
    )

    fig.update_layout(
        width=1200, height=700,
        margin=dict(l=0, r=0, t=30, b=0),
    )

    fig.show()
