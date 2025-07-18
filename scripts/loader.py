import pandas as pd
import os
from csv import QUOTE_NONE


class DataLoader:
    def __init__(self, file_path: str, delimiter: str = ',', encoding: str = 'utf-8'):
        self.file_path = file_path
        self.delimiter = delimiter
        self.encoding = encoding
        self.extension = os.path.splitext(file_path)[1].lower()
        self.df = None

    def load(self):
        try:
            print(f"\nLoading: {self.file_path} ...")
            if self.extension == ".csv":
                self.df = pd.read_csv(
                    self.file_path,
                    on_bad_lines='skip',
                    encoding=self.encoding,
                    delimiter=self.delimiter,
                    quoting=QUOTE_NONE
                )
            elif self.extension == ".xlsx":
                self.df = pd.read_excel(self.file_path)
            elif self.extension == ".json":
                self.df = pd.read_json(self.file_path)
            elif self.extension in [".tsv", ".txt"]:
                self.df = pd.read_csv(
                    self.file_path,
                    sep='\t',
                    on_bad_lines='skip',
                    encoding=self.encoding,
                    quoting=QUOTE_NONE
                )
            elif self.extension == ".parquet":
                self.df = pd.read_parquet(self.file_path)
            elif self.extension == ".pkl":
                self.df = pd.read_pickle(self.file_path)
            else:
                raise ValueError(f"Unsupported file type: {self.extension}")

            print(f"Loaded successfully! Saved as raw_data.csv. \nShape: {self.df.shape}")
        except Exception as e:
            print(f"Error loading file: {e}")

    def get_dataframe(self):
        return self.df
