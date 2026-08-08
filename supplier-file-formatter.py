from pathlib import Path
import pandas as pd

# Mapping supplier column names to the standard client schema.
# Updating a supplier format only requires editing this dictionary.
COLUMN_MAP: dict[str, str] = {
    "Item": "Product",
    "Dept": "Category",
    "Qty": "Quantity",
    "UnitPrice": "Price",
}


def create_supplier_csv(filepath: str) -> None:
    """Generates the raw supplier inventory CSV file."""
    path = Path(filepath)
    path.parent.mkdir(parents=True, exist_ok=True)

    csv_data = """Item,Dept,Qty,UnitPrice
Milk,Dairy,20,65
Bread,Bakery,,80
Sugar,Grocery,40,180
Rice,,25,210
Eggs,Poultry,60,15
Milk,Dairy,20,65"""

    with open(filepath, "w") as file:
        file.write(csv_data)


def load_data(filepath: str) -> pd.DataFrame:
    """Reads a CSV file and loads it into a Pandas DataFrame."""
    return pd.read_csv(filepath)


def standardize_columns(
    df: pd.DataFrame, column_mapping: dict[str, str]
) -> pd.DataFrame:
    """Renames columns to match the standard target schema using a mapping dictionary."""
    return df.rename(columns=column_mapping)


def clean_inventory_data(df: pd.DataFrame) -> pd.DataFrame:
    """Cleans the dataset by handling missing values, casting types, and removing duplicates."""
    cleaned_df = df.copy()

    # Replace missing values
    cleaned_df["Category"] = cleaned_df["Category"].fillna("Unknown")
    cleaned_df["Quantity"] = cleaned_df["Quantity"].fillna(0)

    # Convert numeric columns explicitly
    cleaned_df["Quantity"] = pd.to_numeric(cleaned_df["Quantity"]).astype(int)
    cleaned_df["Price"] = pd.to_numeric(cleaned_df["Price"])

    # Remove duplicates and reset index
    cleaned_df = cleaned_df.drop_duplicates().reset_index(drop=True)

    return cleaned_df


def add_calculated_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Adds derived business metrics to the DataFrame."""
    calculated_df = df.copy()
    calculated_df["Total Value"] = (
        calculated_df["Quantity"] * calculated_df["Price"]
    )
    return calculated_df


def sort_inventory(df: pd.DataFrame, column_name: str) -> pd.DataFrame:
    """Sorts the DataFrame alphabetically by the specified column."""
    return df.sort_values(by=column_name).reset_index(drop=True)


def print_summary_statistics(df: pd.DataFrame) -> None:
    """Calculates and prints dataset insights and business metrics."""
    dataset_shape = df.shape
    total_inventory_value = df["Total Value"].sum()
    avg_quantity = df["Quantity"].mean()

    # Locate the row with the maximum Total Value
    highest_value_row = df.loc[df["Total Value"].idxmax()]
    top_product = highest_value_row["Product"]
    top_product_value = highest_value_row["Total Value"]

    print("\n" + "=" * 40)
    print("        INVENTORY SUMMARY METRICS        ")
    print("=" * 40)
    print(f"Dataset Shape:             {dataset_shape}")
    print(f"Total Inventory Value:     {total_inventory_value:,}")
    print(
        f"Top Product by Value:      {top_product} ({top_product_value:,})"
    )
    print(f"Average Item Quantity:    {avg_quantity:.2f}")
    print("=" * 40)


def save_cleaned_csv(df: pd.DataFrame, output_filepath: str) -> None:
    """Saves the processed DataFrame to a CSV file."""
    path = Path(output_filepath)
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_filepath, index=False)


def main() -> None:
    input_file = "sample_data/supplier_inventory.csv"
    output_file = "output/formatted_supplier_inventory.csv"

    # Step 1: Create raw input data
    create_supplier_csv(input_file)

    # Step 2: Load data
    original_df = load_data(input_file)

    # Step 3: Standardize, clean, calculate, and sort
    df_renamed = standardize_columns(original_df, COLUMN_MAP)
    df_cleaned = clean_inventory_data(df_renamed)
    df_calculated = add_calculated_columns(df_cleaned)
    final_df = sort_inventory(df_calculated, column_name="Product")

    # Step 4: Display DataFrames
    print("--- ORIGINAL DATAFRAME ---")
    print(original_df)

    print("\n--- STANDARDIZED & CLEANED DATAFRAME ---")
    print(final_df)

    # Step 5: Display statistics
    print_summary_statistics(final_df)

    # Step 6: Export results
    save_cleaned_csv(final_df, output_file)
    print(f"\nSuccessfully exported formatted data to: '{output_file}'")


if __name__ == "__main__":
    main()