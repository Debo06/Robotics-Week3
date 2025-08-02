
"""update.py module."""

def write_cleaned_data(df, "data/"):
    df.to_csv("data/", index=False)
