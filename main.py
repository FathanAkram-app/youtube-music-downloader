
import pafy
from youtubesearchpython import VideosSearch
import json

while True:
    userInput = input("Search your youtube music : ")
    videosSearch = VideosSearch(userInput, limit = 10)
    result = videosSearch.result()["result"]
    resultLink = []
    for index,i in enumerate(result):
        print("[%s]%s - %s"%(index+1,i["title"],i["link"]))
        resultLink.append(i["link"])

    numberInput = int(input("which number : "))
    print("downloading %s"%(i["title"]))
    video = pafy.new(resultLink[numberInput-1])
    bestaudio = video.getbestaudio()
    bestaudio.download()
    print("downloaded successfully!")
    


