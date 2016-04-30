import urllib2
from lxml import html
from bs4 import BeautifulSoup

from ClassFileOperations import FileOperations

class WebScrapping:
    
    soup = None
    link = None
    def __init__(self, link, name):    
        ObjFileOp = FileOperations()
        self.link = link
        #page = urllib2.urlopen(link)        
        #self.soup = BeautifulSoup(page, "lxml")
        #ObjFileOp.WriteToFile(name, self.soup)
        page = ObjFileOp.ReadFile(name)
        self.soup = BeautifulSoup(page, "lxml")
        
        
        
    def GetListByDivAndClass(self, className):
        return self.soup.find_all("div", class_ = className)
        
    def TagText(self, item):
        return item.get_text()
        
    def GetParsed(self, item):
        return BeautifulSoup(item, "lxml")
        
    def GetChildren(self, item):
        return list(item.children)