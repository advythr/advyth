# Compute Celcius temperatures
sea_temp_df['temperature_c'] = (sea_temp_df['temperature_f'] - 32) * 5 / 9
sea_temp_df