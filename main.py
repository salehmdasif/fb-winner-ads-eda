from scripts.loader import DataLoader
from scripts.cleaner import DataCleaner
from scripts.data_validator import DataValidator
import pandas as pd
import warnings
warnings.simplefilter(action='ignore', category=RuntimeWarning)

# Show all columns in full width
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 1000)  # Wider console width

# Set your file path here
file_path = "data/ad_data.csv"

# Step 1: Load data using SmartDataLoader
loader = DataLoader(file_path)
loader.load()

# Step 2: Get DataFrame from loader
df_loaded = loader.get_dataframe()

# Step 3: Save it temporarily to pass to DataCleaner (or skip if already loaded)
temp_path = "data/raw_data.csv"
df_loaded.to_csv(temp_path, index=False)

# Step 3: Run validator using df_loaded
validator = DataValidator(df_loaded)
report = validator.run_all_checks()

# Step 4: Print results
for key, value in report.items():
    print(f"{key}: {value}")

confirm = input("\nDo you want to start basic data cleaning? (y/n): ").strip().lower()
if confirm == 'y':
    print("Proceeding with cleaning...\n")

    # Step 5: Clean using DataCleaner
    cleaner = DataCleaner(temp_path)
    cleaner.clean()

    # Step 6: Optional summaries
    cleaner.combined_summary()
    cleaner.show_description()
else:
    print("Cleaning cancelled by user.")






