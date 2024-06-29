"""
Description: Creating data visualizations for analyzing attack patterns and trends using honeypot data.

"""
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import warnings
import time

def load_and_prepare_data(file_path):
    """
    This function is to load and prepare the dataset by handling missing values and converting types.

    Parameters:
    file_path (str): The path to the CSV file.

    Returns:
    pd.DataFrame: The cleaned and prepared dataset.
    """
    time.time()
    data = pd.read_csv(file_path)

    # Filling the missing 'type' values with 'Unknown' after converting the column to a string type
    data['type'] = data['type'].astype(str)
    data['type'].fillna('Unknown', inplace=True)

    # Droping the  unnecessary column
    data.drop(columns=['Unnamed: 15'], inplace=True)

    # Droping the rows with missing latitude or longitude as they are important for geographical analysis
    data.dropna(subset=['latitude', 'longitude'], inplace=True)

    # Converting datetime column to datetime type
    data['datetime'] = pd.to_datetime(data['datetime'])
    
    # Mapping attack types to their respective attack names
    attack_type_mapping = {
        '0.0': 'Echo Reply (ICMP)',
        '3.0': 'Destination Unreachable (ICMP)',
        '5.0': 'Redirect (ICMP)',
        '8.0': 'Echo Request (ICMP)',
        '11.0': 'Time Exceeded (ICMP)',
        '12.0': 'Timestamp Request (ICMP)',
        '13.0': 'Timestamp Reply (ICMP)',
        'Unknown': 'Unknown'
    }
    data['type'] = data['type'].map(attack_type_mapping)
    return data

def print_statistics(data):
    """
    This function is to print basic statistics of the dataset.

    Parameters:
    data (pd.DataFrame): The dataset.
    """
    print("=========================")
    print("Dataset Statistics")
    print("=========================")
    print(f"Total number of entries: {len(data):,}")
    print(f"Number of unique hosts: {data['host'].nunique()}")
    print(f"Date range: {data['datetime'].min()} to {data['datetime'].max()}")
    print("\nMost common attack types:")
    print(data['type'].value_counts().head())
    print("\nBasic statistics for numerical columns:")
    print(data[['latitude', 'longitude']].describe().to_string())
    print("=========================")

def analyze_geographical_distribution_scatter(data):
    """
    This function is to plot a geographical scatter plot showing attack origins based on geographical locations.

    Parameters:
    data (pd.DataFrame): The dataset.
    """
    plt.figure(figsize=(15, 10))
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    world.plot(figsize=(15, 10), color='white', edgecolor='black')
    plt.scatter(data['longitude'], data['latitude'], alpha=0.5, s=10, c='red')
    plt.title('Geographical Scatter Plot of Attack Origins')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.xlim(-180, 180)
    plt.ylim(-90, 90)
    plt.show()

def analyze_time_series(data):
    """
    This function plot the time series analysis of attack frequency.

    Parameters:
    data (pd.DataFrame): The dataset.
    """
    data.set_index('datetime', inplace=True)
    time_series = data['src'].resample('D').count()
    time_series.plot(kind='line', figsize=(12, 6))
    plt.xlabel('Date')
    plt.ylabel('Number of Attacks')
    plt.title('Time Series Analysis of Attack Frequency')
    plt.show()

def analyze_attack_vectors(data):
    """
    This function is to analyze and plot the attack vectors in the dataset.

    Parameters:
    data (pd.DataFrame): The dataset.
    """
    attack_vectors = data['proto'].value_counts()
    attack_vectors.plot(kind='pie', autopct='%1.1f%%', figsize=(8, 8))
    plt.ylabel('')
    plt.title('Attack Vectors Distribution')
    plt.show()

def analyze_grouped_bar_chart(data):
    """
    This function i sto plot a grouped/stacked bar chart to show the number of attacks per host per type.

    Parameters:
    data (pd.DataFrame): The dataset.
    """
    attack_type_host = data.groupby(['host', 'type']).size().unstack().fillna(0)
    attack_type_host.plot(kind='bar', stacked=True, figsize=(14, 8))
    plt.xlabel('Host')
    plt.ylabel('Number of Attacks')
    plt.title('Number of Attacks per Host per Type')
    plt.legend(title='Attack Type', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.show()

def analyze_and_plot_data(file_path):
    """
    This function is to load, prepare, analyze, and plot the dataset.

    Parameters:
    file_path (str): The path to the CSV file.
    """
    data = load_and_prepare_data(file_path)
    print_statistics(data)
    analyze_geographical_distribution_scatter(data)
    analyze_time_series(data)
    analyze_attack_vectors(data)
    analyze_grouped_bar_chart(data)

def main():
    
    # To ignore have future warnings
    warnings.simplefilter(action='ignore', category=FutureWarning)
    
    file_path = 'marx-geo.csv'
    analyze_and_plot_data(file_path)

main()
