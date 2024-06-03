import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file
file_path = 'extrapolation_with_std.xlsx'  # Update this with the actual path to your file
df = pd.read_excel(file_path)

# Check the column names to ensure they are correct
print("Column names:", df.columns)

# Filter the data for Z=50
df_Z50 = df[df['Z'] == 50]

# Check the filtered data
print("Filtered data (Z=50):")
print(df_Z50)

# Convert columns to numpy arrays before plotting
N_values = df_Z50['N'].values
prediction_values = df_Z50['prediction'].values

# Plot the prediction as a function of neutron number
plt.figure(figsize=(10, 6))
plt.plot(N_values, prediction_values, marker='o', linestyle='-', color='b', label='Prediction')

# Adding titles and labels
plt.title('Prediction for Z=50 Isotopic Chain as a Function of Neutron Number')
plt.xlabel('Neutron Number (N)')
plt.ylabel('Prediction')
plt.legend()

# Display the plot
plt.grid(True)
plt.show()

