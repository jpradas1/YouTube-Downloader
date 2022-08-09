from pytube import YouTube
import os
import urllib.request
import re
import pandas as pd

class Downloader():

    query = "https://www.youtube.com/results?search_query="
    watch = "https://www.youtube.com/watch?v="

    def search_URL(self, name_input):
        file = open(name_input, 'r')
        urls = []

        for line in file:
            search_keyword = line
            search_keyword = search_keyword.replace(' ', '+')

            html = urllib.request.urlopen( self.query + search_keyword)
            video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
            urls.append(self.watch + video_ids[0])

        dataframe = pd.DataFrame(urls)    
        dataframe.to_csv("urls.csv", index=False, header=False)
        print("Information Gathering Finished\n")

    def download(self, urls):
        file = open(urls, 'r')

        for line in file:

            link = line

            try:

                yt = YouTube(link)

                print("Title: ", yt.title)
                time_mp3 = yt.length # duration in seconds

                hours = int(time_mp3/60/60)
                time_mp3 -= hours*60*60
                minutes = int(time_mp3/60)
                time_mp3 -= minutes*60
                seconds = int(time_mp3)

                print("Duration: ", f"{hours}:{minutes}:{seconds}")


                mp3 = yt.streams.filter(only_audio=True).first()
                #print("Download in process")
                output_mp3 = mp3.download(output_path="./Output/")

                name, ext = os.path.splitext(output_mp3)
                new_mp3 = name + '.mp3'
                os.rename(output_mp3, new_mp3)

            except:
                pass

        file.close()
        print("Enjoy your music")