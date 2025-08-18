import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from prophet import Prophet


# Load dataset
df = pd.read_excel("sales_data.xlsx")

print("First 5 rows:")
print(df.head())

print("\nData Info:")
print(df.info())

# Plot sales trend
sns.lineplot(data=df, x="date", y="units_sold")
plt.title("Daily Sales Over Time")
plt.xlabel("Date")
plt.ylabel("Units Sold")
plt.show()

# its showes the Reads the Excel file,Prints first few rows,Visualizes sales over time.

 # Prepare data for Prophet
df_prophet = df.rename(columns={"date": "ds", "units_sold": "y"})[["ds", "y"]]

print(df_prophet.head()) 

# Initialize model
model = Prophet(yearly_seasonality=True, daily_seasonality=False)

# Fit model
model.fit(df_prophet)

# Make future dataframe (next 90 days)
future = model.make_future_dataframe(periods=90)

# Forecast
forecast = model.predict(future)

# Plot forecast
fig1 = model.plot(forecast)
plt.show()

# Plot forecast components (trend + seasonality)
fig2 = model.plot_components(forecast)
plt.show()


model = Prophet()
model.fit(df_prophet)