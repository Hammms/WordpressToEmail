# Things that need Done
#   1. Refactor
#   2. Featured Image 
#   3. Styling
#   4. Deathcare Jobs grab

import html
import requests, urllib.request, json
from bs4 import BeautifulSoup
import html5lib

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

FeaturedImage = input("Please enter the featured image \n")



f1 = open("Dist/Upload.html","w", encoding="utf-8")



#Call and grab wordpress article
url = "https://www.nhpco.org/find-a-care-provider/"
req = requests.get(url, headers)
soup = BeautifulSoup(req.content, 'html5lib')
test = soup.find_all("article")


FeaturedImage_Tag = soup.new_tag("img", src=FeaturedImage, id="featured")




#Strip out all unnecessary products that came with the wordpress article 
for div in soup.find_all("div", {'class':'wp-block-image'}): 
    div.unwrap()

for div in soup.find_all("figure"): 
    div.unwrap()

for div in soup.find_all("img", {'class' : "jetpack-lazy-image"}): 
    div.unwrap()

for tag in soup():
    for attribute in ["class", "id", "name", "style", "height", "data-lazy-fallback", "alt", "width", "loading"]:
        del tag[attribute]
    
for div in soup.find_all("noscript"): 
    div.unwrap()

for div in soup.find_all("iframe"): 
    div.decompose()

for div in soup.find_all("div", {"class" : "single-bottom-area"}): 
    div.decompose()

for div in soup.find_all("div", {"style" : "margin:5px auto; margin-bottom: 15px;"}): 
    div.decompose()

for div in soup.find_all("div", {"class" : "tags"}): 
    div.decompose()

for div in soup.find_all("broadstreet-zone"): 
    div.decompose()

for div in soup.find_all("script"): 
    div.decompose()

for div in soup.find_all("a", {"href" : "https://twitter.com/share?ref_src=twsrc%5Etfw"}): 
    div.decompose()

for div in soup.find_all("a", {"rel" : "tag"}): 
    div.decompose()

for div in soup.find_all("figcaption"):
    div = div.wrap(soup.new_tag("p"))
    
for div in soup.find_all("h2")[2:]:
    visualBreak = soup.new_tag("p", style="border-top:solid 4px #000000;font-size:1px;")
    div.insert_before(visualBreak)


for div in soup():
    for attribute in ["class", "id"]: # You can also add id,style,etc in the list
        del div[attribute]

for div in soup.find_all("hr"):
    div.decompose()



# Write Stripped Wordpress article to html doc
#print(soup)
#soup.find("article").find("div").insert(2, FeaturedImage_Tag)


f1.write(str(test)[1:-1])


f2 = open("email.html", 'r')
DCJ = f2.read()
f1.write(DCJ)

#write the styles to the bottom of the page 
f3 = open("styles.txt", 'r')
styles = f3.read()
f1.write(styles)
f3.close
f2.close
f1.close



   # with urllib.request.urlopen("https://deathcarejobs.com/wp-json/wp/v2/job_listing?per_page=5&_fields=title,link") as url:
#     input = json.load(url)
#     print(json2html.json2html.convert(json = input))
    
# f1.write(str(json2html.json2html.convert(json = input)))




# url = "../deathcarejobs/email.html"
# req = requests.get(url, headers)
# soup = BeautifulSoup(req.content, 'html5lib')




# with open("styles.txt") as f:
#     with open("soupTest.html", "w") as f1:
#         for line in f:
#             if "ROW" in line:
#                 f1.write(line) 
#print(test)
#print(soup.prettify())-–