from scrapeasy import Website, Page

web = Website("https://photokinesiologas.com/")

for f in web.getImages(): 
    print(f)
    
