from bs4 import BeautifulSoup
from bs4.element import NavigableString
import urllib2
import re

GET_GOODS_CODE_REGEX = re.compile(r'\\\'goodsCode\\\'\\\:\\\s\\\'(\\\d*)\\\'')

def get_title(li):
    span = li.find('span', class_='title')
    return span.get_text().strip() if span is not None else None

def get_goods_code(li):
    a = li.find('a', attrs={'target': '_blank'})
    m = GET_GOODS_CODE_REGEX.search(a['onclick'])
    return m.group(0) if m is not None else None

req = urllib2.Request(
    'http://category.gmarket.co.kr/listview/List.aspx?gdmc_cd=200001217')
req.add_header(
    'User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36')
r = urllib2.urlopen(req)

soup = BeautifulSoup(r, 'lxml')
li_list = [li
           for ul in soup.find_all('ul', class_='item_list type_list')
           for li in ul.find_all('li')]

products = [(get_title(li), get_goods_code(li)) for li in li_list]

for i, pn in enumerate(products):
    print(str(i) + '. ' + pn[0] + ' --> ' + (pn[1] if pn[1] else 'unknown'))
