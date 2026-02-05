import pandas as pd
import numpy as np
import random

# Read the existing CSV file
df = pd.read_csv('delivery_time.csv')

# Analyze the current data to understand the distribution
delivery_times = df['Delivery Time'].values
sorting_times = df['Sorting Time'].values

# Calculate statistics for the existing data
delivery_mean = np.mean(delivery_times)
delivery_std = np.std(delivery_times)
sorting_min = min(sorting_times)
sorting_max = max(sorting_times)

print(f"Current data stats:")
print(f"Delivery Time - Mean: {delivery_mean:.2f}, Std: {delivery_std:.2f}")
print(f"Sorting Time - Min: {sorting_min}, Max: {sorting_max}")
print(f"Current row count: {len(df)}")

# Generate additional data points to reach over 200 rows
current_count = len(df)
rows_needed = 200 - current_count + 10  # Adding extra to ensure over 200

additional_data = []
for i in range(rows_needed):
    # Randomly select a sorting time between 2 and 10
    sorting_time = random.randint(2, 10)
    
    # Generate a delivery time that generally increases with sorting time
    # Using a base value plus a factor related to sorting time plus some random variation
    base_delivery = 8 + (sorting_time * 1.5)  # Base delivery time correlated with sorting time
    variation = random.uniform(-2, 3)  # Add some variation
    delivery_time = max(5, base_delivery + variation)  # Ensure minimum delivery time
    
    additional_data.append([round(delivery_time, 2), sorting_time])

# Create a DataFrame for the new data
new_df = pd.DataFrame(additional_data, columns=['Delivery Time', 'Sorting Time'])

# Append the new data to the original dataframe
combined_df = pd.concat([df, new_df], ignore_index=True)

# Save the combined data back to the CSV file
combined_df.to_csv('delivery_time.csv', index=False)

print(f"New row count: {len(combined_df)}")
print("Additional data has been generated and appended to the CSV file.")