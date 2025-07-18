# Data Analysis Report



## 1\. Project Title \& Overview

Ad Performance Analysis Using Creative Metrics This project focuses on analyzing ad performance data to identify which creative metrics contribute most to successful outcomes. The goal is to clean and explore the dataset, extract insights, and build a regression model to guide future ad strategy.



## 2\. Business Question or Objective

What creative factors (e.g., scroll stop rate, hook rate, hold rate) most influence ad performance, and how can we identify top-performing ads across multiple metrics?



## 3\. Dataset Summary

* Source of the dataset: Internal ad performance file (ad\_data.csv)
* Timeline: 2 years +
* Description of key variables:
* amount\_spent: Total spend per ad
* max\_roas: Maximum return on ad spend
* result\_rate\_(%): Conversion rate
* scroll\_stop\_(%), hook\_rate\_(%), hold\_rate\_(%): Creative engagement metrics
* ctr, cpr, cpc: Performance indicators
* ad\_name, date: Identifiers and timestamps



## 4\. Data Cleaning Summary

* Standardized column names
* Converted percentage strings to numeric values
* Removed unnamed and constant columns
* Removed duplicates
* Converted date columns to datetime format
* Dropped rows with missing or zero values in critical columns
* Filled missing values in non-critical columns
* Saved cleaned data to advance\_cleaned\_raw\_data.csv



## 5\. Exploratory Data Analysis (EDA)

* Figure out top 10 performing ads
* Descriptive statistics of all columns
* Distribution plots for engagement and performance metrics
* Correlation heatmap to identify relationships



## 6\. Key Insights

* scroll\_stop\_(%) has strong positive correlation with result rate
* High hook\_rate\_(%) and low cpr indicate winning ads
* Few ads perform well across all metrics — ideal for replication
* Scroll-stop rate helps ROAS visually but not statistically strong alone
* Higher CPC gave better results — suggests quality audience targeting
* result\_rate\_(%) is the most reliable and statistically strong KPI
* hook\_rate\_ctr is statistically strong but may reduce conversion if overdone
* cpc shows strong negative impact but better performance came from quality clicks
* scroll\_stop\_(%), amount\_spent, hold\_rate\_cpr looked important in visuals but regression says otherwise



## 7\. Visualizations

* Bar chart showing feature importance from linear regression



## 8\. Statistical Testing Observations

* Linear regression reveals that max\_roas is the most influential driver of result rate, with the highest positive coefficient (10.42) — ads with stronger returns clearly outperform.
* cpc and ctr both show strong positive coefficients, indicating that costlier clicks are acceptable when paired with better targeting and higher click-through performance.
* scroll\_stop\_(%) and hook\_rate\_(%) positively contribute but rank behind CTR and ROAS, suggesting they enhance conversions but aren’t dominant.
* hold\_rate\_(%) and cpr have strong negative coefficients, reinforcing the idea that lingering engagement or high cost per result can dilute performance.
* amount\_spent shows a slightly negative coefficient, emphasizing that spending more doesn’t guarantee results without the right creative metrics in place.



## 9\. Recommendations

* Prioritize creatives with high scroll stop and hook rates
* Avoid ads with high cost per result and low ROAS
* Use winning ads as templates for future campaigns
* Monitor result rate as a key performance metric



## 10\. Limitations \& Assumptions

* Regression assumes linear relationships
* External factors (e.g., audience targeting) not included

## 

