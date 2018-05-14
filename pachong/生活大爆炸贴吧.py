import requests
from bs4 import BeautifulSoup as bs

def get_html(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5083.400 QQBrowser/10.0.972.400"
    }
    try:
        r = requests.get(url=url, headers=headers,timeout=30)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        return "Error"

def get_content(html):

    comments = []

    #html = get_html(url)


    soup = bs(html, 'lxml')

    liTags = soup.find_all('li', attrs={'class': 'j_thread_list clearfix'})

    for li in liTags:
        comment = {}
        try:
            comment['title'] = li.find('a', attrs={'class': 'j_th_tit'}).text.strip()
            comment['link'] = "http://tieba.baidu.com/" + \
                              li.find('a', attrs={'class': 'j_th_tit '})['href']
            comment['name'] = li.find(
                'span', attrs={'class': 'tb_icon_author '}).text.strip()
            comment['time'] = li.find(
                'span', attrs={'class': 'pull-right is_show_create_time'}).text.strip()
            comment['replyNum'] = li.find(
                'span', attrs={'class': 'threadlist_rep_num center_text'}).text.strip()
            comments.append(comment)
            print(comments)
        except:
            print("error")

    return comments

def Out2File(dict):
    '''
    将爬取到的文件写入到本地
    保存到当前目录的 TTBT.txt文件中。

    '''
    with open('TTBT.txt', 'a+') as f:
        for comment in dict:
            f.write('标题： {} \t 链接：{} \t 发帖人：{} \t 发帖时间：{} \t 回复数量： {} \n'.format(
                comment['title'], comment['link'], comment['name'], comment['time'], comment['replyNum']))

        print('当前页面爬取完成')

def main(base_url, deep):
    url_list = []

    for i in range(0,deep):
        url_list.append(base_url + '&pn' + str(50*i))
    print('所有网页已经下载到本地，开始筛选信息')

    for url in url_list:
        content = get_content(url)
        Out2File(content)
    print('所有信息保存完毕')



# if __name__ == "__main__":
#     # headers = {
#     #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5083.400 QQBrowser/10.0.972.400"
#     # }
base_url = 'http://tieba.baidu.com/f?kw=%E7%94%9F%E6%B4%BB%E5%A4%A7%E7%88%86%E7%82%B8&ie=utf-8'
#     deep = 3
#     main(base_url, deep)

html = get_html(base_url)
get_content(html)
