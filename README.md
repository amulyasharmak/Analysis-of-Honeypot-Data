# Analysis-of-Honeypot-Data
The objective of this project is to analyze honeypot data to identify attack patterns, trends, and geographical distributions of cyber-attacks. Honeypots are tools in cybersecurity, that are made to analyze potential cyber threats by mimicking vulnerable systems.


# Methods
Data Cleaning and Preprocessing:
Handling Missing Values: Missing values in columns like 'spt', 'dpt', 'type', and 'country' were filled with appropriate values or removed to ensure data integrity.
Converting Datetime Column: The 'datetime' column was converted to datetime format using Pandas to facilitate time series analysis. (data['datetime'] = pd.to_datetime(data['datetime']))
Mapping Attack Types: Numerical codes in the 'type' column were mapped to meaningful descriptions for better interpretability.

# Visualization Methods:
Geographical Distribution Analysis: Geopandas was used to plot a scatter plot of attack origins on a world map to identify regions with higher attack activity.
Time Series Analysis: Pandas was used to resample data by day and create a line plot to visualize the trend of attack frequency over time.
Attack Vectors Distribution: A pie chart was created to show the proportion of different attack vectors (TCP, UDP, ICMP).
Attack Frequency by Host and Type: A grouped bar chart was used to analyze the number of attacks per host categorized by attack type.

# Data Source:
The data was obtained from Secrepo (https://www.secrepo.com/), a reliable source of honeypot data. The dataset is available in CSV format and includes various fields such as DateTime, host, source IP, protocol, attack type, source port, destination port, country, latitude, and longitude. This comprehensive dataset allows for a detailed analysis of attack patterns and trends.

# Conclusions:
The analysis provided important information about how and when attacks happen. It helped us find high-risk areas and times when attacks are more frequent. By understanding which types of attacks are most common and which hosts are most vulnerable, we can create better cybersecurity strategies.
