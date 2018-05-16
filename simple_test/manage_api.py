import requests

class testApi(object):
    def __init__(self, method, url, data):
        self.method =method
        self.url = url
        self.data = data

    @property
    def testApi(self):
        #根据不同的请求方式访问接口
        try:
            if self.method == 'post':
                if self.data == '':
                    print('No data post')
                else:
                    result = requests.post(self.url, data=(self.data).encode('utf-8'))
            elif self.method == 'get':
                if self.data == '':
                    result = requests.get(self.url)
                else:
                    result = requests.get(self.url, params=self.data)

            return result
        except:
            print("失败")

    def getCode(self):
        #获取接口状态码
        code = self.testApi.status_code
        return code

    def getJson(self):
        #获取返回的json数据
        json_data  = self.testApi.json()
        return json_data

