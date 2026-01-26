# CONSUMER FINANCIAL COMPLAINTS AND RESPONSE ANALYTICS

## Project Overview
This project analyzes consumer complaints filed with the Consumer Financial Protection Bureau (CFPB) to monitor operational performance, product risk, and company responsiveness in the U.S. financial services industry.

The goal is to transform raw complaint data into actionable KPIs and executive dashboards that support compliance, risk monitoring, and decision-making.

## Business Problem

Financial institutions face regulatory and reputational risk if consumer complaints:
Increase rapidly,
Concentrate around specific products,
Are not addressed in a timely manner.

This project answers:
1. Which products generate the most complaints?
2. Are complaints increasing or decreasing over time?
3. How effectively do companies respond?
4. Which companies pose potential operational risk?

## Why This Matters

Regulators monitor complaint trends closely.
High complaint volumes may trigger audits or penalties.
Timely response is a key compliance metric.
Executives need high-level visibility, not raw data.

## Data Source

CFPB Consumer Complaints Database.
Source: Google BigQuery (public dataset).
Time period analyzed: 2019–2023.
Records analyzed: 1.4M+ complaints.

## Key KPIs

Total number of complaints.
Complaints trend by year.
Complaints by product.
Most common consumer issues.
Timely response rate.
Complaint resolution outcomes.
Company-level response performance.

## Dashboards

The analysis is visualized using Power BI, with three interactive pages:

1. Executive Overview:
   Overall complaint volume and trends
   Top consumer issues
   Company response outcomes
   ![Executive Overview](dashboards/executive_overview.png)

2. Product Risk Analytics
   Complaint distribution by product
   Timely response rate by product
   High-risk products
   ![Product Risk Analytics](dashboards/product_risk_analytics.png)

3. Company Performance
   Top companies by complaint volume
   Response quality benchmarking
   ![Company Performance](dashboards/company_performance.png)

## Key Takeaways
- Complaint volumes peaked in 2022 and declined in 2023, which may be due to the partial-year data in    2023.
- Credit reporting-related products generate the highest complaints.
- Majority of complaints are closed with explanation rather than monetary relief.
- Timely response rates are generally high, but performance varies by company and product.

## Tech Stack

Python (Pandas, NumPy, Matplotlib),
Google BigQuery,
Power BI,
VS Code,
Jupyter Notebook