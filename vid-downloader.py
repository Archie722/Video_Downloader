#!/usr/bin/env python
# this works on YouTube and other popular video streaming websites
# youtube-dl is a terminal/command line program, modified to use in this program
# subprocess allows the user to enter command line input into the program itself
# each command is a seperate entity in a list and will accept variables
import subprocess

def single_url():
    url = input('Enter the URL of the video to download :> \n')
# enter the path of where you want the files to be saved
    path = '~/Movies/downloads/%(title)s.%(ext)s'
    subprocess.call(['youtube-dl', '-o', path, url])

def playlist():
    url = input("Enter the URL of playlist page :> \n")
    start = input("Enter the playlist stat number (eg 1):>\n")
    end = input("Enter the playlist end number (num of vids to download):>\n")
    format = 'mp4'

    path = '~/Movies/downloads/%(title)s.%(ext)s'
    subprocess.call(['youtube-dl', '-o', path, '--playlist-start', start,\
        '--playlist-end', end, '--recode-video', format,  url])
# save a vid_list.txt file in the same folder as this application
# copy and paste all all video urls into this on seperate lines
def from_file():
    path = '~/Movies/downloads/%(title)s.%(ext)s'
    format = 'mp4'
    urls = open('vid_list.txt', 'r')
    urls.read()
    urls.close()
    subprocess.call(['youtube-dl', '-o', path, '-a', 'vid_list.txt',\
        '--recode-video', format])
def main():
    print ("""Choose from the following options:\n
                1 - Download single Video by URL
                2 - Download multiple files from a playlist URL
                3 - Download multiple URLs from a .txt file
                """)
    choice = input(":>")
    if choice == "1":
        single_url()
    if choice == "2":
        playlist()
    if choice == "3":
        print ("Make sure the URL's saved to a file called 'vid_list' in the same folder")
        input("press Enter to confirm :>")
        from_file()
    else:
        print ("Please select a valid choice :> \n")
        main()
main()
