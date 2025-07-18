import os
import pandas as pd
from typing import List, Optional
from IPython.display import display


class DataCleaner:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.df = pd.read_csv(file_path)
        print(f"Loaded file: {file_path}")

        self.percent_columns = []

    def preview_raw(self, rows: int = 5):
        print(f"\nRaw Data Preview ({rows} rows):")
        print(self.df.head(rows))

    def standardize_column_names(self):
        self.df.columns = (
            self.df.columns
            .str.lower()
            .str.strip()
            .str.replace(r'[^\w\s]', '', regex=True)
            .str.replace(r'\s+', '_', regex=True)
        )
        print("Standardized column names.")

    def detect_and_clean_percentage_columns(self):
        """Detect columns with '%' and clean them by converting to float"""
        for col in self.df.columns:
            if self.df[col].dtype == 'object':
                if self.df[col].astype(str).str.contains('%').any():
                    self.df[col] = self.df[col].astype(str).str.replace('%', '', regex=False).astype(float)
                    self.percent_columns.append(col)

    def remove_duplicates(self):
        self.df.drop_duplicates(inplace=True)
        print("Removed duplicates.")

    def drop_constant_columns(self):
        constant_cols = [col for col in self.df.columns if self.df[col].nunique(dropna=False) <= 1]
        if constant_cols:
            print(f"Dropping constant columns: {constant_cols}")
            self.df.drop(columns=constant_cols, inplace=True)
        else:
            print("No constant columns found.")

    def drop_unnamed_columns(self):
        unnamed_cols = [col for col in self.df.columns if col.lower().startswith("unnamed")]
        if unnamed_cols:
            print(f"Dropping unnamed columns: {unnamed_cols}")
            self.df.drop(columns=unnamed_cols, inplace=True)
        else:
            print("No unnamed columns found.")

    def save_cleaned_data(self, output_path: str = "data/basic_cleaned_raw_data.csv"):
        try:
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            self.df.to_csv(output_path, index=False)
            print(f"\nBasic cleaning complete and cleaned data saved to: {output_path}")
            print(f"Shape: {self.df.shape}")
            print(f"Total Data Points: {self.df.size}")
        except Exception as e:
            print(f"Error saving file: {e}")

    def show_cleaned_data(self, rows: int = 5):
        print(f"\nCleaned Data Preview ({rows} rows):")
        print(self.df.head(rows))

    def combined_summary(self):
        try:
            dtypes = self.df.dtypes
            null_counts = self.df.isnull().sum()
            null_percents = self.df.isnull().mean() * 100
            unique_counts = self.df.nunique(dropna=False)

            # Sample values handling with fallback
            sample_values = {}
            for col in self.df.columns:
                try:
                    sample = self.df[col].dropna().unique()[:3]
                    sample_values[col] = sample
                except Exception as e:
                    print(f"Could not extract samples from column '{col}': {e}")
                    sample_values[col] = ["<error>"]

            # Create summary frame safely
            summary = pd.DataFrame({
                'dtype': dtypes,
                'null Count': null_counts,
                'null_%': null_percents.round(2),
                'unique': unique_counts,
                'example_values': pd.Series(sample_values)
            })

            summary = summary.sort_values(by='null_%', ascending=False)

            print("\nData Summary:")
            display(summary)

            print(f"\nTotal Entries: {len(self.df)}")

            if summary['null Count'].sum() > 0:
                max_null_col = summary['null Count'].idxmax()
                min_null_col = summary[summary['null Count'] > 0]['null Count'].idxmin()

                print(f"\nHighest Nulls → '{max_null_col}' : {summary.loc[max_null_col, 'null Count']} missing")
                print(f"Lowest Nulls → '{min_null_col}' : {summary.loc[min_null_col, 'null Count']} missing")

        except Exception as e:
            print(f"Error generating summary: {e}")

    def show_description(self):
        print("\nSummary Statistics:")
        print(self.df.describe(include='all'))

    def clean(
        self,
        output_path: str = "data/basic_cleaned_raw_data.csv"
    ):
        print("\nStarting cleaning process...")
        self.standardize_column_names()
        self.detect_and_clean_percentage_columns()
        self.drop_unnamed_columns()
        self.drop_constant_columns()
        self.remove_duplicates()
        self.save_cleaned_data(output_path)
        self.show_cleaned_data()


