import pandas as pd
import matplotlib.pyplot as plt

def plot_data(file_path, label, color):
    # Load the Excel file
    df = pd.read_excel(file_path)
    
    # Filter the data for Z=50
    df_Z50 = df[df['Z'] == 40]
    
    # Convert columns to numpy arrays before plotting
    N_values = df_Z50['N'].values
    prediction_values = df_Z50['prediction'].values
    
    # Plot the prediction as a function of neutron number
#    plt.plot(N_values, prediction_values, marker='o', linestyle='-', color=color, label=label)
     # Plot the prediction as a function of neutron number with black borders around the dots
    plt.plot(N_values, prediction_values, marker='o', linestyle='-', color=color, label=label, markerfacecolor=color, markeredgewidth=1, markeredgecolor='black')

# File paths for each dataset

# File paths for each dataset
file_paths = [
    'extrapolation_with_std.xlsx',  # Update this with the actual path to your first file
    'WS4.xlsx',            # Update this with the actual path to your second file
    'FRDM2012.xlsx'         # Update this with the actual path to your third file
]

# Labels and colors for each dataset
labels = ['GPR', 'WS4', 'FRDM2012']
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'orange', 'purple', 'lime', 'pink', 'olive', 'brown', 'navy', 'teal', 'maroon']

# Plot each dataset
plt.figure(figsize=(10, 6))
for file_path, label, color in zip(file_paths, labels, colors):
    plot_data(file_path, label, color)

# Adding titles and labels
plt.title('Mass excess predictions for Z=50 Isotopic Chain as a Function of Neutron Number', fontsize=12)
plt.xlabel('Neutron Number (N)', fontsize=16)
plt.ylabel('Mass excess [MeV]', fontsize=16)
plt.legend()

# Remove background grid lines
plt.grid(which='both', color='gray', linestyle='-', linewidth=0.5)


# Display the plot
plt.grid(True)
plt.show()

