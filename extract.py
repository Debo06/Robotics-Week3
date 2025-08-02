
"""extract.py module."""

import pandas as pd

def load_inventory_data("data/inventory_raw.csv):
    try:
        df = pd.read_csv("data/inventory_raw.csv)
        return df
    except Exception as e:
        raise RuntimeError(f"Error loading inventory data: {e}")
