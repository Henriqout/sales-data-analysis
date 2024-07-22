import pandas as pd
import numpy as np
import plotly.express as px

def generate_sales_data():
    np.random.seed(42)
    
    dates = pd.date_range(start='2024-01-01', end='2024-07-30', freq='D')
    
    data = {
        'date': np.random.choice(dates, size=1000),
        'store_id': np.random.choice(['A', 'B', 'C', 'D'], size=1000),
        'product_id': np.random.choice(['P1', 'P2', 'P3', 'P4', 'P5'], size=1000),
        'sales_amount': (np.random.normal(500, 200, size=1000) * np.random.uniform(0.8, 1.2, size=1000)).round(2),
        'quantity_sold': np.random.poisson(20, size=1000) + np.random.randint(0, 5, size=1000)
    }
    
    return pd.DataFrame(data)

def clean_transform_data(df):
    print("Checking for missing data")
    print(df.isnull().sum())

    print("Removing duplicate data")
    df.drop_duplicates(inplace=True)

    print("Correcting data types")
    df['date'] = pd.to_datetime(df['date'])
    return df

def aggregate_data(df):
    grouped_df = df.groupby(['store_id', 'date']).agg({
        'sales_amount': ['sum', 'mean', 'std'],
        'quantity_sold': ['sum', 'mean', 'std']
    }).reset_index()
    
    grouped_df.columns = [
        'store_id', 'date', 'total_sales', 'avg_sales', 'std_sales', 
        'total_quantity', 'avg_quantity', 'std_quantity'
    ]
    
    return grouped_df

def create_visualizations(grouped_df):

    fig1 = px.bar(
        grouped_df.groupby('store_id')['total_sales'].sum().reset_index(),
        x='store_id',
        y='total_sales',
        title='Total Sales by Store',
        labels={'store_id': 'Store', 'total_sales': 'Total Sales'}
    )
    fig1.show()

    fig2 = px.line(
        grouped_df,
        x='date',
        y='total_sales',
        color='store_id',
        title='Total Sales Over Time',
        labels={'date': 'Date', 'total_sales': 'Total Sales', 'store_id': 'Store'}
    )
    fig2.show()

def main():
    df = generate_sales_data()
    print("Dataset successfully generated!")

    df = clean_transform_data(df)
    print("Data cleaned and transformed successfully!")

    grouped_df = aggregate_data(df)
    print("Data aggregated and statistics calculated successfully!")
    
    create_visualizations(grouped_df)
    print("Visualizations created successfully!")

if __name__ == "__main__":
    main()
