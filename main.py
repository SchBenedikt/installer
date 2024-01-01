# File for downloading multiple files.
# In this example, it is used for installing the Text-Editor (https://github.com/SchBenedikt/Text-Editor), but can also used for other softwares.
import requests
import os

def download_file(url, destination_folder="."):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            # Extract the filename from the URL
            filename = os.path.join(destination_folder, url.split("/")[-1])
            
            # Save the downloaded file
            with open(filename, 'wb') as file:
                file.write(response.content)
            
            print(f"Download successful: {filename}")
        else:
            print(f"Error downloading {url}. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")

# Example URLs
urls = [
    "https://github.com/SchBenedikt/Text-Editor/blob/main/decrease_font.png",
    "https://github.com/SchBenedikt/Text-Editor/blob/main/auth.py",
    "https://github.com/SchBenedikt/Text-Editor/blob/main/italic.png"
]

# Target folder for download
download_folder = "Text-Editor"

# Create the target folder if it doesn't exist
os.makedirs(download_folder, exist_ok=True)

# Flag to track successful downloads
success = True

# Iterate through the URLs and download the files
for url in urls:
    download_file(url, download_folder)
    # Check if the download was unsuccessful
    if not os.path.exists(os.path.join(download_folder, url.split("/")[-1])):
        success = False

# Display the overall success message
if success:
    print("All files were downloaded successfully.")
else:
    print("Some files failed to download. Please check the error messages above.")
