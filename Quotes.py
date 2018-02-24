import requests
import re
import urllib.request
import time
def get_html(url):
    response=requests.get(url)
    return response.text #Returns page html code
def main():
    #Getting Links From Main Page
    url="https://quotefancy.com/"
    all_html=get_html(url)
    p=re.compile(r'<a href=\"https://quotefancy.com/.*?\">',re.S)
    p1 = re.compile(r'\"https://quotefancy.com/media/wallpaper/1600x900.*?\.jpg\"', re.S)
    res = p.findall(all_html)
    main_page_links=[]
    for i in range (0,res.__len__()):
        res[i]=res[i].replace("<a href=\"","")
        res[i]=res[i].replace("\">","")
    main_page_links=res[::2]
    ##We've got all the links from main page(categories)
    res.clear()
    index=0
    for link in main_page_links: #finding img links in every category
        html = get_html(link)
        res = p1.findall(html) #list with img links
        for img_link in res: #for every picture link in every category
            url=str(img_link)
            url=url.replace("\"","")
            img = urllib.request.urlopen(url).read()
            out = open("img" + str(index) + ".jpg", "wb")
            out.write(img)
            out.close
            index+=1
            if (index%50)==0:
                time.sleep(5) #sleep 5 seconds at every 50th picture
        res.clear()
main()
