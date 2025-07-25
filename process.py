
"""process.py module."""

import pandas as pd
import numpy as np

def clean_and_process(df):
    df = df.drop_duplicates(subset=['SKU', 'Location'])
    df['OnHandQty'] = df['OnHandQty'].apply(lambda x: max(x, 0))
    df['ReorderQty'] = np.maximum(0, df['ReorderPoint'] - df['OnHandQty'])
    df['NeedsRestock'] = df['ReorderQty'] > 0
    return df
