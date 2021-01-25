import requests
from plyer import notification
from bs4 import BeautifulSoup
import time

def notifyMe(title, message): #To Show The Notification
    notification.notify(
        title= title,
        message = message,
        timeout = 20 #Timeout Settings In Seconds
    )

def webData(url): #Getting The Data From The Website
    r = requests.get(url)
    return r.text

if __name__ == "__main__":
    while True:
        html_doc = webData('https://news.google.com/covid19/map?hl=en-US&mid=%2Fm%2F0f4zv&gl=US&ceid=US%3Aen')
        soup = BeautifulSoup(html_doc, 'html.parser') #Parsing The Data
        mystr = ""

        for tr in soup.find_all ('tbody')[1].find_all('tr'):
            mystr += tr.get_text() #Converting the Parsed Data to a String        
        mystr = mystr[1:]
        myList = (mystr.split("\n\n")) 


        states = ['New York','Pennsylvania', 'Texas',] # Enter Your State Name Here (Dont Enter More Than 5 States)
        for item in myList[0:31]:
            dataList = (item.split('\n'))
            if dataList[1] in states:
                notify_title= 'Cases of Covid-19 In United States'
                notify_text= f" State: {dataList[1]}\n United States Cases : {dataList[2]} & International Cases : {dataList[3]}\n Cured : {dataList[4]}\n Deaths : {dataList[5]}"
                notifyMe(notify_title, notify_text)
                time.sleep(2)
        time.sleep(3600) #Loop For 1 Hour (1 hour = 3600 seconds)
