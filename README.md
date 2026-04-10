# spark-elt-pipeline

ELT pipeline using Apache Spark and Databricks for transforming raw transactional data.

## Overview
This project demonstrates a simple ELT (Extract, Load, Transform) workflow using Apache Spark in Databricks. The pipeline shows how raw data can be loaded into Spark, cleaned, transformed, and analyzed to produce meaningful insights.

## Objectives
- Extract raw transactional data
- Load the data into Spark DataFrames
- Transform the data after loading
- Generate aggregated results for analysis

## Tools and Technologies
- Apache Spark
- PySpark
- Databricks
- SQL

## Project Structure
- `week 1` – Initial notebook/file for the first week’s Spark or Databricks work
- `week2` – Notebook/file containing ELT pipeline code and transformations
- `README.md` – Project documentation

## Workflow
1. **Extract**  
   Raw transactional data is created or collected.

2. **Load**  
   The raw data is loaded into a Spark DataFrame.

3. **Transform**  
   Data is cleaned and transformed using PySpark functions.

4. **Analyze**  
   SQL queries and Spark transformations are used to generate summaries such as total sales by state.

## Example Processing
The pipeline includes:
- Creating a Spark DataFrame from raw data
- Displaying the data using `show()`
- Checking schema with `printSchema()`
- Casting columns into correct data types
- Grouping data by state
- Calculating total sales
- Running SQL queries on temporary views

## Sample Output
Example result from the transformation:

| State | Total Sales |
|-------|-------------|
| NV    | 385.0       |
| CA    | 350.5       |
| AZ    | 50.0        |

## How to Run
1. Open Databricks
2. Import or upload the notebook files
3. Attach the notebook to a Spark cluster
4. Run the cells step by step
5. View the transformed output and SQL results

## Learning Outcomes
Through this project, I learned:
- How ELT differs from ETL
- How to use Spark DataFrames for data processing
- How to apply transformations after loading data
- How to combine PySpark and SQL in Databricks
- How to summarize and analyze transactional data efficiently

## Author
Sumanth Nandipati
