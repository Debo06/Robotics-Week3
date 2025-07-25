
"""extract.py module."""

import pandas as pd

def load_inventory_data(filepath):
    try:
        df = pd.read_csv(filepath)
        return df
    except Exception as e:
        raise RuntimeError(f"Error loading inventory data: {e}")
