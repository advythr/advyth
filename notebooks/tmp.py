# Get the area outside the city boundary
out_gdf = gpd.GeoDataFrame(geometry=sanjose_gdf.envelope).overlay(
    sanjose_gdf, how="difference"
)
out_gdf