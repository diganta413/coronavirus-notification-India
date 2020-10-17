from bs4 import BeautifulSoup
from win10toast import ToastNotifier
import requests
import time
def notification(s):
    n=ToastNotifier()
    n.show_toast("Corona Virus Notification(India)",s, duration=5,
                 icon_path="coronavirus.ico")

if __name__ == '__main__':

    while True:
        url="https://www.worldometers.info/coronavirus/country/india/"
        u=requests.get(url)
        content=u.content
        l=[]
        #print(content)
        soup=BeautifulSoup(content,'html.parser')
        soup_1=soup.prettify()
        t=soup_1.title
        i=soup.find_all('div',class_='maincounter-number')
        for i1 in i:
            i3=i1.find('span').text
            l.append(i3)
        s="Coronavirus Cases : " + l[0]
        s1="Total Deaths : " + l[1]
        s2="Total Recovered : " + l[2]
        s3=s+"\n"+s1+"\n"+s2
        notification(s3)
        time.sleep(60)





