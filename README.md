# Scrapy data-analysis project

This project uses Scrapy to scrape car listings from the Auto.RIA website, gathering detailed information on car models, prices, mileage, engine specifications, color, fuel type, and gearbox type. Data cleaning and transformations were applied to standardize formats and prepare the data for analysis.

#### The data collected was then visualized using graphs available at the following link:
```http
https://lookerstudio.google.com/s/kZvB9Bo3pBY
```

-------------------------------------------------------------------------------------
## Key Features:
- **Data Scraping**: Extracts car information, including model, year, price (in USD), mileage (in km), engine volume, horsepower, color, fuel type, and gearbox type.
- **Data Transformation**: Converts prices to USD, normalizes color names, and extracts structured data from unformatted text.
- **Visualization**: The data insights are visualized in a Looker Studio report, displaying key metrics and trends in car listings on Auto.RIA.
-------------------------------------------------------------------------------------
## Graph Highlights:
- **Engine Type Distribution**: Shows which engine types are most common in listings, revealing preferences for fuel types among sellers.
- **Average Price by Engine Type**: Visualizes the average car price for each engine type, helping to identify pricing trends for different fuel types.
- **Top 10 Most Expensive Cars**: Lists the ten highest-priced cars on Auto.RIA, showcasing premium listings.
- **Top 10 Cars with Highest Mileage**: Displays the ten cars with the highest mileage in listings, providing insights into long-lasting car models.