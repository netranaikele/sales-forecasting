# Sales Forecasting with Prophet

A time series forecasting project that analyzes historical sales data and predicts future sales trends using Facebook's Prophet library.

## Overview

This project reads sales data from an Excel file, performs exploratory data analysis, and uses Prophet to forecast sales for the next 90 days. The analysis includes trend visualization, seasonality detection, and comprehensive forecasting with confidence intervals.

## Features

- **Data Loading & Exploration**: Reads Excel sales data and displays basic statistics
- **Data Visualization**: Creates line plots to visualize sales trends over time
- **Time Series Forecasting**: Uses Prophet for accurate sales predictions
- **Seasonality Analysis**: Detects and visualizes yearly seasonal patterns
- **Future Predictions**: Generates 90-day sales forecasts
- **Component Analysis**: Breaks down forecast into trend and seasonal components

## Requirements

```python
pandas
matplotlib
seaborn
prophet
openpyxl  # For Excel file reading
```

## Installation

```bash
pip install pandas matplotlib seaborn prophet openpyxl
```

## Data Format

The Excel file (`sales_data.xlsx`) should contain the following columns:
- `date`: Date column (datetime format)
- `units_sold`: Number of units sold (numeric)

Example data structure:
```
date        | units_sold
2023-01-01  | 150
2023-01-02  | 165
2023-01-03  | 142
...
```

## Usage

1. Place your sales data in an Excel file named `sales_data.xlsx` in the same directory
2. Run the script:
   ```bash
   python sales_forecast.py
   ```

## Code Structure

### Data Loading and Exploration
```python
# Loads Excel data and displays first 5 rows
df = pd.read_excel("sales_data.xlsx")
print(df.head())
print(df.info())
```

### Data Visualization
```python
# Creates a line plot showing sales trend over time
sns.lineplot(data=df, x="date", y="units_sold")
```

### Prophet Model Setup
```python
# Renames columns to Prophet's required format (ds, y)
df_prophet = df.rename(columns={"date": "ds", "units_sold": "y"})[["ds", "y"]]

# Initializes Prophet model with yearly seasonality
model = Prophet(yearly_seasonality=True, daily_seasonality=False)
```

### Forecasting
```python
# Fits model and creates 90-day forecast
model.fit(df_prophet)
future = model.make_future_dataframe(periods=90)
forecast = model.predict(future)
```

### Visualization
- **Forecast Plot**: Shows historical data with future predictions and confidence intervals
- **Components Plot**: Displays trend and seasonal components separately

## Model Configuration

- **Yearly Seasonality**: Enabled to capture annual patterns
- **Daily Seasonality**: Disabled (suitable for aggregated daily data)
- **Forecast Period**: 90 days into the future
- **Confidence Intervals**: Automatically calculated by Prophet

## Output

The script generates:
1. Console output with data summary and first few rows
2. Line plot showing historical sales trends
3. Forecast visualization with predictions and confidence bands
4. Component analysis showing trend and seasonality patterns

## Key Insights

The Prophet model provides:
- **Trend Analysis**: Long-term growth or decline patterns
- **Seasonality Detection**: Recurring patterns throughout the year
- **Uncertainty Quantification**: Confidence intervals for predictions
- **Anomaly Detection**: Identification of unusual data points

## Customization

### Adjusting Forecast Period
```python
# Change periods parameter for different forecast horizons
future = model.make_future_dataframe(periods=30)  # 30 days instead of 90
```

### Adding Holidays
```python
# Include holiday effects
from prophet import Prophet
model = Prophet(holidays=your_holiday_dataframe)
```

### Tuning Seasonality
```python
# Adjust seasonality parameters
model = Prophet(
    yearly_seasonality=True,
    weekly_seasonality=True,
    daily_seasonality=False,
    seasonality_mode='multiplicative'
)
```

## Troubleshooting

- **File Not Found**: Ensure `sales_data.xlsx` exists in the correct directory
- **Date Format Issues**: Verify date column is in proper datetime format
- **Missing Values**: Clean data before feeding to Prophet
- **Insufficient Data**: Prophet requires at least several months of data for reliable forecasts

## Next Steps

- Add cross-validation for model performance evaluation
- Include external regressors (promotions, weather, etc.)
- Implement automated model selection
- Create interactive dashboards for forecast visualization
- Add model performance metrics (MAPE, MAE, RMSE)

## License

This project is open source and available under the MIT License.
