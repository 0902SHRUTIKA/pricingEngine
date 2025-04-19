Pricing Engine

This Python script reads product and sales data from two CSV files, applies pricing rules based on stock and demand, and generates an updated price list.

* Files Used

- `products.csv` – Contains product details like `sku`, `name`, `current_price`, `cost_price`, and `stock`.
- `sales.csv` – Contains sales info with `sku` and `quantity_sold`.
- `updated_prices.csv` – The output file containing updated prices.

* Pricing Rules

1. Rule 1: Low Stock, High Demand 
   `stock < 20` AND `quantity_sold > 30` → **Increase price by 15%

2. Rule 2: Dead Stock
   `stock > 200` AND `quantity_sold == 0` → **Decrease price by 30%

3. Rule 3: Overstocked Inventory
   `stock > 100` AND `quantity_sold < 20` → **Decrease price by 10%

4. Rule 4: Minimum Profit Constraint
   Final price must be at least 20% above `cost_price`.

5. Final Rounding
   All prices are rounded to "2 decimal places" and prefixed with the currency symbol `₹`.

*  Example Output

| sku  | old_price | new_price |
|------|-----------|-----------|
| A123 | ₹649.99   | ₹600.00   |
| B456 | ₹699.00   | ₹803.85   |
| C789 | ₹999.00   | ₹699.30   |

* Output

The updated prices are saved in the file `updated_price.csv`.

