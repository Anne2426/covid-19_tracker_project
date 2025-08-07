
# covid19_tracker.py

import requests
import pandas as pd
import matplotlib.pyplot as plt

# Fetch COVID-19 summary from an open API
url = "https://api.covid19api.com/summary"
response = requests.get(url)

# Check if data was received
if response.status_code == 200:
    data = response.json()
    global_data = data['Global']
    countries_data = data['Countries']

    print("🌍 Global COVID-19 Summary:")
    print(f"New Confirmed: {global_data['NewConfirmed']}")
    print(f"Total Confirmed: {global_data['TotalConfirmed']}")
    print(f"New Deaths: {global_data['NewDeaths']}")
    print(f"Total Deaths: {global_data['TotalDeaths']}")
    print(f"New Recovered: {global_data['NewRecovered']}")
    print(f"Total Recovered: {global_data['TotalRecovered']}")

    # Convert country data to DataFrame
    df = pd.DataFrame(countries_data)
    top10 = df.sort_values(by='TotalConfirmed', ascending=False).head(10)

    # Plot top 10 countries by total confirmed cases
    plt.figure(figsize=(12, 6))
    plt.bar(top10['Country'], top10['TotalConfirmed'], color='orange')
    plt.title("Top 10 Countries by Total COVID-19 Confirmed Cases")
    plt.xlabel("Country")
    plt.ylabel("Total Confirmed Cases")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("top10_covid_countries.png")
    plt.show()

else:
    print("❌ Failed to fetch data from the API.")
