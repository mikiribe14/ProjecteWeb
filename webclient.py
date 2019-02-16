#download a web page
#searche activities in the web page
#print the activities

from urllib.request import urlopen

class WebClient(object):
    """WebVlient class"""
    def __init__(self):
        super(WebClient, self).__init__()


    def download_page(arg):
        #connect to the web site
        file=urlopen("http://www.eps.udl.cat/ca/")
        #get the download download_page
        page=file.read()
        #close the connection
        file.close()
        return page


    def run(self):
        #download a web page
        page=self.download_page()

        #print it
        print(page)



if __name__=="__main__":
    c = WebClient()
    c.run()
    print "prova de github desde portatil"
    print "prova 2 desde portatil"
