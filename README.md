# Programing For Cultural Heritage: Unforgotten Restaurants

This project aims to commemorate and honor our beloved restaurants which have been temporarily or permanently closed due to the Covid-19 pandemic. The goal of this project is to extract data that can visualize the status and gravity of closed restaurants. I referenced Google Maps’ API, which presents the current status of recently closed restaurants. 

This project was completed in three steps. I fetched the data through the API as a python file and extracted the necessary information through the .json file. And in order to visualize that information on personalized Google Maps, I converted it into a .csv file that Google Maps can read and perform. 

Limitations for this project are as follows:
First, The Places Api returned only 60 results, which means a Python file in the Github repository is a script that displays only restaurant data within a specific district of Midtown, New York. Therefore, the user has to enter various latitude and longitude directly in the script to find the desired data. 

Second, the permanently closed restaurant information is not returned by the Google MAP API. Searching through the data will display "Permanently_closed" = True, but that is also marked with "business_status": "CLOSED_TEMPORARILY". That is, Place Search currently supports a field called permanently_closed, but it doesn’t distinguish between a business or location that is closed permanently or closed temporarily. According to the Google MAP API instruction page,  “the Places field permanently_closed is deprecated as of May 26, 2020, and will be turned off on May 26, 2021.Use the business_status field to return the operational status of businesses.” So I created a map based on what business_status indicated as 'closed_temporarily'.

Steps for mapping the closed restaurants in new york city.

1. Download pfchnyc.py and type your desired location information at “search_lat_long” field.
2. Then the places.json file is created. 
3. Convert it to a csv file and upload the csv file from Google Map to check the status of closed restaurants. You can see how in Place.csv file. I simply used a converter for converting a json file to a csv file. 

Final result can be found at: https://sites.google.com/pratt.edu/nyc/introduction
