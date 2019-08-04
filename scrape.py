from bs4 import BeautifulSoup
from urllib.request import urlopen
import io

a = 'https://jadijadi.github.io/snowcrash/chapter-00.html'

soup = []

for i in range(1, 73):
    if(i < 10):
        b = '0' + str(i)
    else:
        b = str(i)
    c = a.replace('00', b)
    source = urlopen(c).read()
    print(i)
    s = BeautifulSoup(source, features="html.parser")
    soup.append(s)
    f = io.open("pages/page_00.txt".replace('00', b), "w", encoding = 'utf-8')
    for paragraph in s.findAll('p'):
        try:
            f.write(paragraph.string)
        except TypeError:
            print()
        f.write('\n')
    f.close()
