import polars as pl
from pathlib import Path


DATA_PATH = 'data/StudentPerformanceFactors.csv'

file_path = Path(DATA_PATH)
if not file_path.exists():
    dtf = None
else:
    dtf = pl.read_csv(file_path)