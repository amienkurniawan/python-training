import bs4

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/global/id-en/Product/ProductList.aspx?Submit=ENE&N=-1&IsNodeId=1&Description=laptop&bop=And&PageSize=96&order=BESTMATCH'

# open connection, grab all data
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html,'html.parser')
# grab each products
containers = page_soup.findAll("div",{"class":"item-info"})

filename = "product.csv"
f = open(filename,"w")

header = "Brand, Product Name, Product Price\n"
f.write(header)

for container in containers[4:]:
    brand = container.a.img["title"]
    if not brand:
        brand = "empty brand"

    title_container = container.findAll("a", {"class": "item-title"})
    product_name = title_container[0].text

    price_container = container.findAll("li", {"class": "price-current"})
    price_product = price_container[0].text[:-16].strip()

    print("Brand :" + brand)
    print("Product Name:" + product_name)
    print("Product Price :" + price_product)
    f.write(brand+","+product_name.replace(",","|")+","+price_product.replace(",",".")+"\n")
f.close()

