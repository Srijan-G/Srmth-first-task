from bs4 import BeautifulSoup
filexml=open("task.xml","r")
page_name=input()
frame_name=input()
soup=BeautifulSoup(filexml,"lxml-xml")
tag=soup.find("Page",{"name":page_name})
a=tag.find("step",{"frame":frame_name})
for i in (a["pose"].split()):
    if i[0]!='-':
        i=" "+i
    print(i)
filexml.close()
