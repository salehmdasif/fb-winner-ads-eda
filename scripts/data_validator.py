import pandas as pd
import numpy as np


class DataValidator:
    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def check_raw(self, rows: int = 5):
        print(f"\nRaw Data Check ({rows} rows):")
        print(self.df.head(rows), "\n")

    def check_duplicates(self):
        return self.df.duplicated().sum()

    def check_unnamed_columns(self):
        return [col for col in self.df.columns if col.lower().startswith("unnamed")]

    def check_constant_columns(self):
        return [col for col in self.df.columns if self.df[col].nunique() <= 1]

    def run_all_checks(self):
        self.check_raw()
        return {
            'Duplicates': self.check_duplicates(),
            'Unnamed Columns': self.check_unnamed_columns(),
            'Constant Columns': self.check_constant_columns()
        }
