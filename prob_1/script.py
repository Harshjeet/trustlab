

# # print("File downloaded successfully!")
# import requests
# from urllib.parse import urlsplit

# # Replace the URL with the actual link you see when hovering over the `href` tag
# url = 'https://www.scb.se/contentassets/edc2b33f85ad415d8e7909002253ed84/2023-05-11-preliminar_statistik_over_doda_inkl_eng.xlsx'

# # Send a GET request to the URL
# response = requests.get(url)

# # Extract the filename from the response headers
# content_disposition = response.headers.get("Content-Disposition", "")
# if content_disposition:
#     filename = content_disposition.split("filename=")[1].strip('"')
# else:
#     # If Content-Disposition header is not present, extract filename from URL
#     filename = urlsplit(url).path.split("/")[-1]

# # Open a file in write mode and write the content of the response
# with open(filename, "wb") as f:
#     f.write(response.content)

# print(f"Downloaded file: {filename}")

import requests
import pandas as pd
from urllib.parse import urlsplit

# Replace the URL with the actual link you see when hovering over the `href` tag
url = 'https://www.scb.se/contentassets/edc2b33f85ad415d8e7909002253ed84/2023-05-11-preliminar_statistik_over_doda_inkl_eng.xlsx'

# Send a GET request to the URL
response = requests.get(url)

# Extract the filename from the response headers
content_disposition = response.headers.get("Content-Disposition", "")
if content_disposition:
    filename = content_disposition.split("filename=")[1].strip('"')
else:
    # If Content-Disposition header is not present, extract filename from URL
    filename = urlsplit(url).path.split("/")[-1]

# Open a file in write mode and write the content of the response
with open(filename, "wb") as f:
    f.write(response.content)

print(f"Downloaded file: {filename}")

# Check if the downloaded file has a ".xlsx" extension
if filename.endswith(".xlsx"):
    sheet_name = input("Enter the sheet name you want: ")
    # Ask the user for the desired CSV filename
    csv_filename = input("Enter the desired CSV filename (without extension): ") + ".csv"
   
    #read specific sheet
    df = pd.read_excel(filename, sheet_name=sheet_name)

    # Save the DataFrame to a CSV file
    df.to_csv(csv_filename, index=False, header = None)

    print(f"File {csv_filename} downloaded successfully. ")
