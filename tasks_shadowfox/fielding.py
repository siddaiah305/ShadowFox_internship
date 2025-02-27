import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
file_path = r"C:\Users\kasan\OneDrive\Documents\IPL_1.xlsx"
df = pd.read_excel(file_path)

# Display basic information about the dataset
print("Dataset Info:")
print(df.info())
print("\nFirst 5 rows:")
print(df.head())

# Define a research question: Analyzing top fielders' performance
# Assuming we have columns like 'Player', 'Catches', 'Runouts'
if 'Player' in df.columns and 'Catches' in df.columns and 'Runouts' in df.columns:
    df['Total_Fielding'] = df['Catches'] + df['Runouts']
    top_fielders = df.sort_values(by='Total_Fielding', ascending=False).head(10)
    
    # Visualization
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Total_Fielding', y='Player', data=top_fielders, palette='viridis')
    plt.xlabel("Total Fielding Contributions")
    plt.ylabel("Player")
    plt.title("Top 10 Fielders in IPL")
    plt.show()
else:
    print("Required columns not found in dataset. Please check the data structure.")
