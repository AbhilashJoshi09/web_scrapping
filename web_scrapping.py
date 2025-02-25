from bs4 import BeautifulSoup
import requests
import sys
sys.stdout.reconfigure(encoding='utf-8')
import csv
import time
import random


source_url = 'https://www.booking.com/searchresults.html?ss=Goa%2C+India&efdco=1&label=gen173nr-1FCAEoggI46AdIM1gEaGyIAQGYATG4ARfIAQzYAQHoAQH4AQKIAgGoAgO4AsTx8L0GwAIB0gIkODgxNmQzMDEtNjdjZS00YjljLTgxMjgtZTkzN2Y4NTUzZGQ22AIF4AIB&aid=304142&lang=en-us&sb=1&src_elem=sb&src=index&dest_id=4127&dest_type=region&checkin=2025-03-03&checkout=2025-03-04&group_adults=2&no_rooms=1&group_children=0'

def web_scrapping(source_url, file_name):

    #greeting
    print("Thank you sharing the source_url and file name!\n...\nFatching data...")
    num = random.randint(2,6)
    time.sleep(num)

    ## header for given user is authentation for web site security policies.  It's a short, technical description of the web browser, operating system, (and maybe mobile device) that you're using as you access the internet. 
    header = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0'}

    response = requests.get(source_url, headers = header)

    if response.status_code == 200:
        print("successfully connected to ebookinf.com")
        html_content = response.text

        # creating soup
        soup = BeautifulSoup(html_content,'html.parser')
        print(soup.prettify())

        #main containers
        hotel_divs = soup.find_all('div', role = "listitem")

        with open(f'{file_name}.csv', 'w',encoding = 'utf-8') as csv_file:
            writer = csv.writer(csv_file)

            # adding header
            writer.writerow(['Hotel Name','Location','Price','Rating','Score','Review','Link'])

            for hotel in hotel_divs:
                hotel_name = hotel.find('div', class_="f6431b446c a15b38c233")
                hotel_name = hotel_name.text.strip() if hotel_name else "N/A"

                location = hotel.find('span', class_="aee5343fdb def9bc142a")
                location = location.text.strip() if location else "N/A"

                price = hotel.find('span', class_="f6431b446c fbfd7c1165 e84eb96b1f")
                price = price.text.replace('₹ ', '').strip() if price else "N/A"

                rating = hotel.find('div', class_="a3b8729ab1 e6208ee469 cb2cbb3ccb")
                rating = rating.text.strip() if rating else "N/A"

                score = hotel.find('div', class_="a3b8729ab1 d86cee9b25")
                score = score.text.strip().split(' ')[-1] if score else "N/A"

                review = hotel.find('div', class_="abf093bdfe f45d8e4c32 d935416c47")
                review = review.text.strip() if review else "N/A"

                link = hotel.find('a', href=True)
                link = "https://www.booking.com" + link['href'] if link else "N/A"

            #saving the file into csv
            writer.writerow([hotel_name,location,price,rating,score,review,link])

        #print(f"Hotel Name: {hotel_name}")
        # print(f"Location: {location}")
        # print(f"Price: {price}")
        # print(f"Rating: {rating}")
        #print(f"Score: {score}")
        #print(f"Review: {review}")

        print("Data saved successfully")

    else:
        print("connection failed")    

#if using this script directly than below task will be executed
if __name__ == '__main__':
    source_url = input("Enter the source url: ")
    file_name = input("Enter the file name: ")
    web_scrapping(source_url, file_name)
