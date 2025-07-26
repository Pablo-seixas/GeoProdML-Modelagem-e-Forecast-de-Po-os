import folium
from folium.plugins import MarkerCluster

def gerar_mapa(df, lat_col='lat', lon_col='lon', tooltip_col='litologia', popup_col='produtividade_inicial_bpd'):
    mapa = folium.Map(location=[-15.5, -47.5], zoom_start=5)
    cluster = MarkerCluster().add_to(mapa)

    for _, row in df.iterrows():
        folium.Marker(
            location=[row[lat_col], row[lon_col]],
            tooltip=f"{row[tooltip_col]}",
            popup=f"Produtividade: {row[popup_col]:.1f} bpd"
        ).add_to(cluster)

    return mapa
