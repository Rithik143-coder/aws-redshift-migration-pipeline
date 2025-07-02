# AWS Redshift Migration Pipeline

This project simulates a legacy data warehouse migration to Amazon Redshift using AWS Glue, Apache NiFi, and Lambda functions for orchestration and automation.

## Features
- AWS Glue jobs to transform and load data
- Apache NiFi for ingestion from multiple sources
- AWS Lambda + Step Functions for automation
- Data validation & cleansing
- Sample schema and connection config

## Technologies
- AWS Glue
- Apache NiFi
- Amazon Redshift
- AWS Lambda
- Python, SQL, Terraform

## Folder Structure
- `etl/` – Glue scripts and Lambda orchestration
- `config/` – JSON-based connection configuration
- `terraform/` – Redshift infrastructure as code
- `data/` – Sample data files

## How to Run
- Deploy infrastructure with Terraform
- Trigger NiFi ingestion
- Run Glue jobs via Lambda
