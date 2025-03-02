import pandas as pd
mrio = pd.read_parquet('.\data\ADB MRIO constant price\mrio-62c.parquet')
mrio.to_csv('.\data\ADB MRIO constant price\ADB MRIO constant price.csv', index=False)