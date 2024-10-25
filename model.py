import pandas as pd
import matplotlib.pyplot as plt
import os
from config import PARENT_DIRECTORY

# Set the working directory
os.chdir(PARENT_DIRECTORY)

# Adjust the file path accordingly
df = pd.read_csv(r'Data\HenryHub_NatGas_SpotPrices_EIA.csv')

# Convert 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Set 'Date' as the index
df.set_index('Date', inplace=True)

# Display the first few rows of the DataFrame
print(df.head())
df.info()

# Plotting the data
plt.figure(figsize=(10, 6))
plt.plot(df.index, df['Price'], color='blue', linewidth=2)

# Labeling the plot
plt.xlabel('Date')
plt.ylabel('Price ($/MMBTU)')
plt.title('Henry Hub Natural Gas Spot Price Over Time')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Show the plot with better layout
plt.tight_layout()
plt.show()


