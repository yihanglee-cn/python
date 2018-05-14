

origin = input('please input the city you leave:')
destination = input('please input the city you want go:')
date = input('please input the date (ex:2017-07-23):')

#init()

class TrainsCollection:
    header = '航空公司 航班 机场 时间 机票价格 机场建设费'.split()
    def __init__(self, airline_tickets):
        self.airline_tickets = airline_tickets

    def plains(self):
        air_company = {"G5":"华夏航空","9C":"春秋航空","MU":"东方航空","NS":"河北航空",
                       "HU":"海南航空","HO":"吉祥航空","CZ":"南方航空","FM":"上海航空",
                       "ZH":"深圳航空","MF":"厦门航空","CA":"中国国航","KN":"中国联航"}
        for item in self.airline_tickets:
            try:
                strs = air_company[item['alc']]
            except KeyError:
                strs = item['alc']

