#coding=utf-8
'''
使用postman进行接口测试的练习
'''
#------ 第一步 导包 ------
import requests
import unittest

#------ 第二步 定义参数 ------
url = "https://www.v2ex.com/api/nodes/show.json"
querystring = {"name": "python"}
headers = {
            'Cache-Control': "no-cache",
            'Postman-Token': "a74f2872-70ff-4643-9e68-9694a558feae"
}

#------ 第三步 定义测试类 ------
class v2exTestCase(unittest.TestCase):
    '''v2ex测试用例'''

    # ------ 初始化函数 ------
    def setUp(self):
        pass

    # ------ 获取id用例 ------
    def test_getId(self):
        '''获取id值用例'''

        response = requests.request("GET", url, headers=headers, params=querystring)

        #print(response.text)
        code = str(response.status_code)
        print("URL："+url+"，访问成功，状态码为：" + code)
        response = response.json()
        #print("" + response)
        id_result = str(response.get("id"))
        print("响应内容中的id值为：" + id_result)

        self.assertEqual("90",id_result)
        print("id正确！")

    # ------ 结束函数 ------
    def tearDown(self):
        pass

# ------ 第三步 运行 ------
if __name__ == "__main__":
    unittest.main()