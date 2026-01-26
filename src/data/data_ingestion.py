# Importing the required libraries
import pandas as pd
from pathlib import Path
from google.cloud import bigquery

# Defining the function to fetch data from BigQuery
def fetch_complaints_data():
    """This function fetches consumer complaints data from the BigQuery public dataset."""

    client = bigquery.Client(
        project="financial-complaints-analytics"
    )

    query = """
SELECT
    date_received,
    product,
    subproduct,
    issue,
    subissue,
    company_name,
    state,
    company_response_to_consumer,
    timely_response,
    consumer_disputed
FROM `bigquery-public-data.cfpb_complaints.complaint_database`
WHERE date_received >= DATE('2019-01-01')
"""


    df = client.query(query).to_dataframe()
    return df

# Defining the function to save raw data
def save_raw_data(df, output_path):
    """
    This function saves raw data to CSV format.
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    # Fetch data
    df = fetch_complaints_data()

    # Define output path
    raw_data_path = Path("data/raw/raw_data.csv")

    # Save raw dataset
    save_raw_data(df, raw_data_path)

    # Basic sanity checks
    print("Raw data saved successfully!")
    print(f"Shape: {df.shape}")
    print(df.head())
