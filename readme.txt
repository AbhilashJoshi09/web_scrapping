Web Scraping Script for Booking.com

# Description:-
This script scrapes hotel details from Booking.com based on the provided URL and stores the extracted data in a CSV file. The script collects hotel names, locations, prices, ratings, scores, reviews, and booking links.

# Requirements:-
To run this script, you need to have Python installed along with the following dependencies:
- `requests`
- `beautifulsoup4`

Install them using:
```
pip install requests beautifulsoup4
```

# How to Use
1. Run the script using:
```
python script_name.py
```
2. Enter the Booking.com search results page URL when prompted.
3. Provide a filename (without extension) to save the extracted data.

# Features:-
- Fetches data from Booking.com
- Extracts hotel name, location, price, rating, score, review, and link
- Saves data into a CSV file
- Includes random delays to mimic human browsing

# Output:-
A CSV file containing:
- Hotel Name
- Location
- Price
- Rating
- Score
- Review
- Booking Link

# Notes:-
- Ensure the provided URL contains hotel listings.
- The script may stop working if Booking.com updates its HTML structure.
- Modify class names in the script if required to match Booking.com’s current website layout.
- Scraping should be done responsibly and in compliance with the website’s terms of service.

# Disclaimer:-
This script is for educational purposes only. Web scraping may violate the terms of service of some websites. Use responsibly.

