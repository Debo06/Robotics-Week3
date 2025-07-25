
"""alert.py module."""

def generate_alerts(df):
    alerts = df[df['NeedsRestock']]
    print(f"🔔 {len(alerts)} items need restocking.")
    return alerts
