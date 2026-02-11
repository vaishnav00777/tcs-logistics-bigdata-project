import pandas as pd

shipment = pd.read_csv('../data/shipment_data.csv')
vehicle = pd.read_csv('../data/vehicle_tracking.csv')

# Cleaning
shipment.dropna(inplace=True)
vehicle.drop_duplicates(inplace=True)

# Merge datasets
merged = shipment.merge(vehicle, on='vehicle_id')

# Feature Engineering
merged['delivery_deviation'] = (
    merged['actual_delivery_time'] -
    merged['expected_delivery_time']
)

merged.to_csv('../data/processed_logistics.csv', index=False)
print("ETL Completed")
