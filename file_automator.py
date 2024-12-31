import os
import sys
import time
import logging
import schedule
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from time import sleep

# Getting your source directory (in my case:"/Users/Daniel/Downloads") where the program will grab your downloaded files
# with os.scandir("/Users/Daniel/Downloads") as entries:
#     for entry in entries:
#         print(entry.name) <----- This code is just for you to check if your source directory is correct, printing all its elements

class FileSorter(LoggingEventHandler):
    #This class handles file system events and sorts newly created files and organizes them
    def __init__(self, source_directory):
        super().__init__()
        self.source_directory = source_directory

    def on_created(self, event):
        #Triggered when a new file is created in the monitored folder.
        if not event.is_directory:
            sleep(2)
            self.sort_file(event.soruce_path)

    def sort_file(self, file_path):
    #Sorts a single file into the appropriate folder based on its type.
        file_type_directory = {
            #The first bit is the most important, rename these to all the folders (folders that will be created in the download directory)
            #you want your files to be, and you can mix them around (e.g., have my images and videos together)
            "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".csv", ".pptx", ".odt", ".rtf", ".html", ".xml"],
            "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv", ".webm"],
            "Audio": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a", ".wma"],
            "Images": [".png", ".jpeg", ".jpg", ".gif", ".bmp", ".svg", ".tiff", ".webp"],
            "Other": []
            }
        
        if os.path.isfile(file_path):
            _, ext = os.path.splitext(file_path)
            destination = "Other"

            for folder, extensions in file_type_directory.items():
                if ext.lower() in extensions:
                    destination = folder
                    break

        destination_directory = os.path.join(self.source_directory, destination)
        os.makedirs(destination_directory, exist_ok = True)
        
        
        
    