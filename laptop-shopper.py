from bs4 import BeautifulSoup
from bs4.element import NavigableString
import urllib2

req = urllib2.Request(
    'http://category.gmarket.co.kr/listview/List.aspx?gdmc_cd=200001966')
req.add_header(
    'User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36')
r = urllib2.urlopen(req)

soup = BeautifulSoup(r, 'lxml')
li_list = [li
           for ul in soup.find_all('ul', class_='item_list type_list')
           for li in ul.find('li')
           if type(li) is not NavigableString]

product_names = [span.get_text() for span in [li.find(
    'span', class_='title') for li in li_list] if span is not None]

for pn in product_names:
    print(pn)
