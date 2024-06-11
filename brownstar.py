from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd
import requests

# WIKIPEDIA Bright STARS DATA URL
START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

page = requests.get("https://en.wikipedia.org/wiki/List_of_brown_dwarfs")
soup = bs4(page.text,"html.parser")

temp_list = []

start_table = soup.find_all("table", {"class:"wikitable sortable"})
print(len(start_table))
table_rows =start_table[1].find_all("tr")
for tr in table_rows:
    td = tr.find_all("td")
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

Star_names = []
Distance =[]
Mass = []
Radius =[]

print(temp_list)

for i in range(1,len(temp_list)):
    
    Star_names.append(temp_list[i][0])
    Distance.append(temp_list[i][5])
    Mass.append(temp_list[i][7])
    Radius.append(temp_list[i][8])

# Convert to CSV
headers = ['Star_name','Distance','Mass','Radius']  
df2 = pd.DataFrame(list(zip(Star_names,Distance,Mass,Radius,)),columns=['Star_name','Distance','Mass','Radius'])
print(df2)

df2.to_csv('dwarf_stars.csv', index=True, index_label="id")
# Define Data Scrapping Method
def scrape():
               
        # BeautifulSoup Object     
        soup = BeautifulSoup(browser.page_source, "html.parser")

        # VERY IMP: The class "wikitable" and <tr> data is at the time of creation of this code. 
        # This may be updated in future as page is maintained by Wikipedia. 
        # Understand the page structure as discussed in the class & perform Web Scraping from scratch.

        # Find <table>
        bright_star_table = soup.find("table", attrs={"class", "wikitable"})
        
        # Find <tbody>
        table_body = bright_star_table.find('tbody')

        # Find <tr>
        table_rows = table_body.find_all('tr')

        # Get data from <td>
        for row in table_rows:
            table_cols = row.find_all('td')
            # print(table_cols)
            
            temp_list = []

            for col_data in table_cols:
                # Print Only colums textual data using ".text" property
                # print(col_data.text)

                # Remove Extra white spaces using strip() method
                data = col_data.text.strip()
                # print(data)

                temp_list.append(data)

            # Append data to star_data list
            scarped_data.append(temp_list)


       
# Calling Method    
scrape()

################################################################

# IMPORT DATA to CSV

stars_data = []


for i in range(0,len(scarped_data)):
    
    Star_names = scarped_data[i][1]
    Distance = scarped_data[i][3]
    Mass = scarped_data[i][5]
    Radius = scarped_data[i][6]
    Lum = scarped_data[i][7]

    required_data = [Star_names, Distance, Mass, Radius, Lum]
    stars_data.append(required_data)

print(stars_data)


# Define Header
headers = ['Star_name','Distance','Mass','Radius','Luminosity']  

# Define pandas DataFrame   
star_df_1 = pd.DataFrame(stars_data, columns=headers)

#Convert to CSV
star_df_1.to_csv('scraped_data.csv',index=True, index_label="id")




