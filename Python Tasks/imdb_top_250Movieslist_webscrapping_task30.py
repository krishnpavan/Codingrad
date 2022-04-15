'''
Web Scrapping extracts the data from websites in the
unstructured format. 
It helps to collect these unstructured data and 
convert it in a structured form.
'''

'''
pip:
pip is the standard package manager for Python. 
It allows you to install and manage additional 
packages.
'''
#installations
# pip install pandas
# pip install requests
# pip install beautifulsoup4


# IMDb movies Website scrapping program illustration
# urllib module we want to use response method
# for palcing permission request from website
from urllib import response
# for requesting permission from websites
import requests
# To store data as table format, we import pandas
import pandas as pd
# BeautifulSoup is used to keep data in proper format
# bs4 is total module and from it i want to use only BeautiulSoup
from bs4 import BeautifulSoup

# To ask request from IMDb movies website
response = requests.get('https://www.imdb.com/chart/top/?sort=nv,desc&mode=simple&page=1')  # for permission we use get()
# if we get 200 then its success and got permission from IMDb website
#print(response)


# To bring the data from IMDb movies website
# storing data from IMDb website in soup
# parser is conversion. html tag number is converted to data
# information in html tags is converted into readable data using parser
soup = BeautifulSoup(response.content,'html.parser')
# we get data but its not structured
#print(soup) 


# To get data in structured format little bit we 
# use prettify()
#print(soup.prettify())


# To convert data into structured format
# find_all() function in beautiful soup is used to access
# data in particular tag

# To extract name of the movies
# names of top 250 movies in IMDb website
# class_ is used to identify that particular tag
# movie names are avialable in td tag in titleColumn
names = soup.find_all('td',class_='titleColumn')
print(names)


# To filter out only movie names data
# To extract data using list
# unstructured data to structured data
# To find names data
# creating empty list 'name'
name = []
# to get all names of tags
# len(names) is given to iterate over all the names 
# of the realme products
print(len(names)) # len(names) = 250  
for i in range(0,len(names)):
    # get_text() function is used to get only text data  
    name.append(names[i].a.get_text()) # append function adds names in lists 
print(name)


# To find year data of the movie
# class_ is used to identify that particular tag
# Here class_='titleColumn' 'span' tag consists of year data
years = soup.find_all('td',class_='titleColumn')

# Creating empty list 'year'
year = []

print(len(years)) # len(years) = 250
for i in range(0,len(years)):
    # get_text() function is used to get only text data  
    year.append(years[i].span.get_text()) # append function adds years in lists 
print(year)


# To find IMDb Rating of the product
# class_ is used to identify that particular tag
# available in 'td' tag
# Here class_='ratingColumn imdbRating' class consists of rating data
ratings = soup.find_all('td',class_='ratingColumn imdbRating')

# Creating empty list 'rating'
rating = []

print(len(ratings)) # len(ratings) = 250 
for i in range(0,len(ratings)):
    # get_text() function is used to get only text data  
    rating.append(ratings[i].strong.get_text()) # append function adds names in lists 
print(rating)


# To scrap links with in IMDb website
# links are present in 'td' tag       
links = soup.find_all('td',class_='posterColumn')
link = []
for i in range(0,len(links)):
    # 'https://www.imdb.com/' adding this to get http protocol and open link
    # all links are in 'href' with in anchor 'a' tag
    d = 'https://www.imdb.com/' + links[i].a['href']
    link.append(d)
print(link)


# To find image of the movie
# image link will be found in source (src) tag
# In websites links for images are provided
# rather than directly uploading images, by providing
# links of images website loading will not slow down
# Generally all these images are stored in S3 bucket 
# then will be reconnected to html source (src) tag
images = soup.find_all('td',class_='posterColumn')
image = []
# To add data to empty list
for i in range(0,len(images)):
    # ['src'] is attribute of image where source tag with imge link is avialable  
    image.append(images[i].img['src']) # append function adds image links in lists 
print(image)


# All scrapped data is in list format
# To store all the above scrapped data in a structured format
# in rows and columns as csv file
# DataFrame() is two dimensional and has rows,columns
df = pd.DataFrame()
# Creating required columns and rows
df['Movie Name'] = name 
df['Movie Release Year'] = year
df['Movie Ratings'] = rating
df['Movie Image'] = image
df['Movie Links'] = link

# Printing the datafram
print(df)


# to convert data into csv file
df.to_csv('C:/Users/HOME/Desktop/VS code Files/Tasks/Webscrapping/IMDb_Top250_movies_data.csv')

# so we can scrap all the data from website
# and save in csv excel file