from lxml import etree
import requests
import json
import time
import re

url_home = 'https://www.888gp.net/249_249749/'
url_chapter = 'https://www.888gp.net/249_249749/{chapter}.html'
param_content = '//div[@id="content"]/text()'
param_mid = '本章未完.*\.html'
param_end = '本章已完成.*\.html'
param_count = '//font[text()="最新章节："]/a/text()'
param_chapter_name = '//div/h1/text()'

pattern_count = re.compile(".*?(\d+)")
MAXX = 10
INTERVAL = 0.05
start = 395
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}

fp = open("output.txt", "a", encoding='utf8')
result = []


def Get(url):
    res = requests.get(url, headers=headers)
    res.encoding = 'gbk'
    return res


def etHTML(url):
    s = etree.HTML(Get(url).text)
    return s


#计算end
end = int(
    re.search(pattern_count,
              etHTML(url_home).xpath(param_count)[0]).group(1))
# print(f"end={end}")

for i in range(start, end):
    # for i in range(start,start+1):
    print(f"chapter: {i} ", end='')
    try:
        j = 1
        tmp = {'chapter_id': i, 'chapter_name': i, 'content': ''}
        while (j < MAXX):
            ss = etHTML(url_chapter.format(chapter=f'{i}_{j}'))
            if (j == 1):
                tmp['chapter_name'] = ss.xpath(param_chapter_name)[0].strip(
                    '（1/3）24567890')
            s = ss.xpath(param_content)
            lst = s[-1]
            del s[-1]
            tmp['content'] += ("\n".join(s))
            if (re.match(param_mid, lst, re.S)):
                pass
            elif (re.match(param_end, lst, re.S)):
                break
            else:
                raise Exception(f"Unknown end. String: {lst}")
            j += 1
        result.append(tmp)
        fp.write(tmp['chapter_name'] + '\n')
        fp.write(tmp['content'] + '\n')
        fp.flush()
        print("succeed")
    except KeyboardInterrupt:
        fp.flush()
        exit(0)
    except Exception as e:
        print(f"err: {e}")
    time.sleep(INTERVAL)
with open("output.log", "a", encoding='utf8') as fp2:
    json.dump(result, fp2, ensure_ascii=False)
