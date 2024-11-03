import pandas as pd

# Sample earthquake data
data = {
    "Date": ["2024-01-15", "2024-02-03", "2024-03-21", "2024-05-14", "2024-07-30"],
    "Latitude": [54.2, 55.3, 53.8, 54.9, 52.7],
    "Longitude": [-1.5, -2.4, -3.6, -0.8, -1.2],
    "Depth_km": [10.2, 15.5, 5.8, 12.3, 7.5],
    "Magnitude": [2.5, 3.2, 1.8, 2.9, 3.4],
    "Location": ["North Sea", "Central UK", "Southern UK", "East UK", "North Sea"],
}

# Create DataFrame
df = pd.DataFrame(data)

# Convert 'Date' column to datetime format
df["Date"] = pd.to_datetime(df["Date"])

# Display the DataFrame
print("Earthquake DataFrame:")
print(df)

# Calculate the average magnitude of earthquakes
average_magnitude = df["Magnitude"].mean()
print("\nAverage Magnitude of Earthquakes:", average_magnitude)

# Filter earthquakes with magnitude greater than 2.0
significant_quakes = df[df["Magnitude"] > 2.0]
print("\nEarthquakes with Magnitude > 2.0:")
print(significant_quakes)

# Calculate the number of earthquakes by month
df["Month"] = df["Date"].dt.month
earthquakes_per_month = df["Month"].value_counts().sort_index()
print("\nNumber of Earthquakes per Month:")
print(earthquakes_per_month)

# Optional: Plotting the number of earthquakes per month (requires matplotlib)
try:
    import matplotlib.pyplot as plt

    earthquakes_per_month.plot(
        kind="bar",
        title="Earthquakes per Month",
        xlabel="Month",
        ylabel="Number of Earthquakes",
    )
    plt.show()
except ImportError:
    print(
        "\nMatplotlib is not installed. Install it to visualize earthquake trends per month."
    )

# Print a name at the end
print("\nScript completed. Name: John Doe")
