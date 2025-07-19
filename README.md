# Optimizing Facebook Ads: Unveiling the Top 10 Performing Ad Creatives with Performance EDA

## Features
- Smart data loader (CSV, Excel, JSON, TSV, Parquet, Pickle)
- Auto cleaner (columns, duplicates, missing, dates)
- `main.py` for full pipeline execution (Set your file path there)
	

## Structure
```
data_analysis_project/
├── data/                                           # Raw or cleaned datasets
├── images/
├── notebooks/                                      # All Jupyter/Colab notebooks
│   ├── 01_load_preview.ipynb
│   ├── 02_manual_clening.ipynb
│   └── 03_explore_cleaned_data.ipynb
├── outputs/                                        # Processed files, reports, charts
│   ├──report_and_insights.md                        
├── scripts/                                        # Core logic (reusable Python modules)
│   ├── cleaner.py                                  # AutoCleaner class
│   ├── data_validator.py                           # DataValidator 
│   ├── loader.py                                   # SmartDataLoader class
│   └── utils.py                                    # Helper functions (save/load/export)
├── main.py                                         # Entry point: run everything from one place
├── requirements.txt                                # Used pip dependencies
├── README.md                                       # Project overview & instructions
├── .gitignore                                      # Ignore virtual env, cache, etc.
└── LICENSE

```

## Usage
```
python main.py
```

## Execution Order
```
Following the sequence — Load → Clean → Explore. 
— 01_load_preview.ipynb,
— 02_manual_cleaning.ipynb,
— 03_explore_cleaned_data.ipynb

```
