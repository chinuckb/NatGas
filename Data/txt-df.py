import pandas as pd
import matplotlib.pyplot as plt
import json

def load_data(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            try:
                data_dict = json.loads(line.strip())
                if data_dict.get('series_id') == "NG.RNGWHHD.D":
                    data.extend(data_dict.get('data', []))
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")

    # Convert to DataFrame
    df = pd.DataFrame(data, columns=['Date', 'Price'])

    # Convert the 'Date' column to datetime format
    df['Date'] = pd.to_datetime(df['Date'], format='%Y%m%d')

    # Set the 'Date' column as the index
    df.set_index('Date', inplace=True)

    return df

# Adjust the file path accordingly
file_path = r'E:\Python Projects\A33 Hedge Fund\Natural Gas Model\Henry Hub Natural Gas Spot Price DeepL Model\NatGas\Data\NatGas_BulkData_EIA.txt'
df = load_data(file_path)

# Display the first few rows of the DataFrame
print(df.head())
df.to_csv(r'E:\Python Projects\A33 Hedge Fund\Natural Gas Model\Henry Hub Natural Gas Spot Price DeepL Model\NatGas\Data\HenryHub_NatGas_SpotPrices_EIA.csv', index=True)


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
