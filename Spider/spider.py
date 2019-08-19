

import re
from urllib import request


class Spider():
    url = 'https://www.huya.com/g/393'
    root_pattern = '<span class="txt">([\s\S]*?)</li>'
    name_pattern = '<i class="nick" title="([\s\S]*?)">'
    number_pattern = '<i class="js-num">([\s\S]*?)</i>'

    def __get_content(self):
        r = request.urlopen(Spider.url)
        htmls = r.read()
        htmls = str(htmls, encoding='utf-8')
        return htmls

    def __analysis(self, htmls):
        root_html = re.findall(Spider.root_pattern, htmls)
        infs = []
        for html in root_html:
            name = re.findall(Spider.name_pattern, html)
            number = re.findall(Spider.number_pattern, html)
            inf = {'name': name, 'number': number}
            infs.append(inf)
        return infs
        # print(infs[0])

    def __refine(self, infs):
        for i in range(0, len(infs)):
            infs[i]['name'] = ''.join(infs[i]['name'])
            infs[i]['number'] = ''.join(infs[i]['number'])
        return infs
        # f = lambda infs: {'name': infs['name'][0], 'number': infs['number'][0]}
        # return map(f, infs)

    def __sort(self, infs):

        infs=sorted(infs,key=self.__cmp,reverse=True)
        return infs

    def __cmp(self,inf):
        r=re.findall('\d+\.?\d*',inf['number'])
        num=float(r[0])
        if '万' in inf['number']:
            num*=10000
        return num

    def __show(self,infs):
        for i in range(0,len(infs)):
            print(infs[i]['name']+'----'+infs[i]['number']+'人')

    def go(self):
        htmls = self.__get_content()
        infs = self.__analysis(htmls)
        infs = self.__refine(infs)
        infs = self.__sort(infs)
        self.__show(infs)

spider = Spider()
spider.go()


