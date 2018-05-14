#coding=utf-8
import types
allGuests = {'Alice': {'apples': 5, 'pretzels': {'12':{'beijing':456}}},
             'Bob': {'ham sandwiches': 3, 'apple': 2},
             'Carol': {'cups': 3, 'apple pies': 1},'ipad':['1','2','3']}
def dictget(dict1,obj,default=None):
    for k,v in dict1.items():
        if k == obj:
            print(v)
        else:
            if type(v) is dict:
                re=dictget(v,obj)
                if re is not default:
                    print(re)
                # else:
                #     return default
dictget(allGuests,'ipad')
