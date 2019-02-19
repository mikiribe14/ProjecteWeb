#download a web page
#searche activities in the web page
#print the activities

from urllib.request import urlopen
import bs4 #li dono un fitxer xml i em construeix un arbre
    #HTML es un exemple concret de xml, si està ben fet

class WebClient(object):
    """WebClient class"""
    def __init__(self):
        super(WebClient, self).__init__()

    def download_page(arg):
        #connect to the web site
        file=urlopen("https://www.banggood.com/es/")
        #get the download download_page
        page=file.read()
        #close the connection
        file.close()
        return page

    def search_activities(self,page):
        tree = bs4.BeautifulSoup(page,"lxml")
        unorderedList = tree.find("ul","goodlist_1")
        lista=unorderedList.find_all("li")

        for item in lista:
            print(item)


    def run(self):
        #download a web page
        page=self.download_page()
        #print it
    #    print(page)
        #search activities in the page
        data=self.search_activities(page)
        #print the activities
        print(data)

if __name__=="__main__":
    c = WebClient()
    c.run()
