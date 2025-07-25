
"""main.py - Orchestrator."""

import argparse
from extract import load_inventory_data
from process import clean_and_process
from update import write_cleaned_data
from alert import generate_alerts

def main(input_path, output_path):
    print("🚚 Loading data...")
    df = load_inventory_data(input_path)

    print("🛠️ Processing data...")
    df = clean_and_process(df)

    print("📦 Writing cleaned data...")
    write_cleaned_data(df, output_path)

    print("📣 Generating restock alerts...")
    generate_alerts(df)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to input CSV")
    parser.add_argument("--output", required=True, help="Path to output cleaned CSV")
    args = parser.parse_args()
    main(args.input, args.output)
