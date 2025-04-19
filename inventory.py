import pandas as pd
from pandas import DataFrame

# load csv files of product data
print('Products')
products_df = pd.read_csv('products.csv')
print(products_df.head())

# load csv files of sales data
print('Sales')
sales_df = pd.read_csv('sales.csv')
print(sales_df.head())
# print(products_df.columns)#list of product columns
# print(sales_df.columns)#list of sales columns

# Merge both dataframes by using sku
merge_df: DataFrame = pd.merge(sales_df, products_df, on='sku')

# fill missing sales data with 0
merge_df['quantity_sold'] = merge_df['quantity_sold'].fillna(0)
print(merge_df)


# def function to calculate new prices
def apply_pricing(row):
    old_price = row['current_price']
    cost_price = row['cost_price']
    stock = row['stock']
    quantity_sold = row['quantity_sold']
    new_price = old_price

    # Rule 1 – Low Stock, High Demand (Highest Priority)
    if stock < 20 and quantity_sold > 30:
        new_price = old_price * 1.15
    # Rule 2 – Dead Stock (Second Priority)
    elif stock > 200 and quantity_sold == 0:
        new_price = old_price * 0.7
    # Rule 3 – Overstocked Inventory (Third Priority)
    elif stock > 100 and quantity_sold < 20:
        new_price = old_price * 0.9
    # Rule 4 – Minimum Profit Constraint (Always Applied Last)
    min_price = cost_price * 1.2
    if new_price < min_price:
        new_price = min_price

    # Final Rounding
    new_price = round(new_price, 2)

    return new_price

    # Apply pricing rules for each row
    merge_df['new_price'] = merge_df.apply(apply_pricing_rules, axis=1)
    # Prepare for output csv files
    output_df = merge_df[['sku', 'current_price', 'new_price']]
    output_df.rename(columns={'current_price': 'old_price'}, inplace=True)

    # Add ₹ for unit
    output_df['old_price'] = output_df['old_price'].apply(lambda x: f"₹{x:.2f}")
    output_df['new_price'] = output_df['new_price'].apply(lambda x: f"₹{x:.2f}")

    # Save updated_price.
    merge_df.to_csv("Updated_price.csv", index=False)
    output_df.to_csv("updated_price.csv", index=False)  # updated_df.to_csv("updated_prices.csv",index = false)
    print("Pricing updated successfully. File saved as 'updated_prices.csv'.")

