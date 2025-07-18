# Helper functions will go here
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from IPython.core.display_functions import display


# Date Correction
def convert_columns_to_datetime(df, columns=None):
    """
    Converts specified columns to datetime.
    If no columns are provided, automatically detects columns containing 'date' in their name.

    Parameters:
        df (pd.DataFrame): The input DataFrame.
        columns (list, optional): Specific columns to convert. If None, it auto-detects.

    Returns:
        pd.DataFrame: DataFrame with converted datetime columns.
    """
    try:
        # Auto-detect if no columns are provided
        if columns is None:
            columns = [col for col in df.columns if 'date' in col.lower()]
            if not columns:
                print("No column containing 'date' found.")
                return df

        converted = []
        for col in columns:
            try:
                df[col] = pd.to_datetime(df[col], errors='coerce')
                if df[col].notnull().sum() > 0:
                    converted.append(col)
            except Exception as e:
                print(f"Failed to convert '{col}' to datetime: {e}")

        if converted:
            print("\nDatetime conversion completed for:")
            for col in converted:
                print(f"- {col}: {df[col].dtype}")
        else:
            print("No columns were successfully converted to datetime.")

        return df

    except Exception as e:
        print(f"Error during datetime conversion: {e}")
        return df


# Fill non critical missing values
def fill_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()  # Keep raw data unchanged

    for col in df.columns:
        if df[col].dtype == 'O':  # Object/String type
            df[col] = df[col].replace("Unknown", pd.NA)
            mode_val = df[col].mode().dropna()
            df[col] = df[col].fillna(mode_val.iloc[0] if not mode_val.empty else "Unknown")
        else:  # Numeric type
            df[col] = df[col].fillna(df[col].median())

    return df


# Value Counts summary
def print_column_value_summary(df: pd.DataFrame):
    # Prints unique value count and value frequencies for each column in a DataFrame.
    for col in df.columns:
        print(f"\nColumn: {col}")
        print(f"Unique values: {df[col].nunique(dropna=False)}")
        print(f"Value Counts:\n{df[col].value_counts(dropna=False)}")


# Frequency Summary Table
def generate_frequency_summary(df: pd.DataFrame) -> pd.DataFrame:
    summary = []

    for col in df.columns:
        top_val = df[col].mode(dropna=False)[0] if not df[col].mode(dropna=False).empty else None
        top_count = df[col].value_counts(dropna=False).iloc[0] if not df[col].value_counts(dropna=False).empty else 0

        summary.append({
            'Column': col,
            'Dtype': df[col].dtype,
            'Unique Values': df[col].nunique(dropna=False),
            'Most Frequent (Top Value)': top_val,
            'Frequency': top_count
        })

    return pd.DataFrame(summary)


def check_duplicates(df: pd.DataFrame):
    dup_count = df.duplicated().sum()
    print(f"\nDuplicate rows: {dup_count}")
    return dup_count


def check_column_distribution(df: pd.DataFrame, column: str):
    if column in df.columns:
        print(f"\nValue counts for column: {column}")
        print(df[column].value_counts(dropna=False))
    else:
        print(f"⚠️ Column '{column}' not found in DataFrame.")


def summary_statistics(df: pd.DataFrame):
    print("\nSummary Statistics:")
    display(df.describe(include='all').transpose())
