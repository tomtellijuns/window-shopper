from bs4 import BeautifulSoup
from bs4.element import NavigableString
import urllib2
import re

GET_GOODS_CODE_REGEX = re.compile(r'goodscode=(\d*)\&')

def get_title(li):
    span = li.find('span', class_='title')
    return span.get_text().strip() if span is not None else None

def get_goods_code(li):
    a = li.find('a', attrs={'target': '_blank'})
    m = GET_GOODS_CODE_REGEX.search(a['href'])
    return m.group(1) if m is not None else None

category_code = '200001217' # meat
# category_code = '200001054' # refrigerator


def crawl(page):
    req = urllib2.Request(
        'http://category.gmarket.co.kr/subpage/SearchItemListView.aspx?gdmc_cd={}&page={}&'.format(category_code, page))
    req.add_header(
        'User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36')
    r = urllib2.urlopen(req).read().decode('euc-kr')

    soup = BeautifulSoup(r, 'lxml')
    li_list = [li
            for ul in soup.find_all('ul', class_='item_list type_list')
            for li in ul.find_all('li')]

    for li in li_list:
        yield (get_title(li), get_goods_code(li))

# count = 1
# for page in range(1, 11):
#     for product in crawl(page):
#         print(str(count) + '. ' + product[0] + ' --> ' + product[1])
#         count += 1
