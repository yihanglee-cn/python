from requests_html import HTMLSession

session = HTMLSession()
r = session.get('https://python.org/')

print(r.html.absolute_links)

# css选择器，id=downloads的节点的文本
about = r.html.find('#about', first=True)
#print(about.text)
a = about.attrs()
print(a)