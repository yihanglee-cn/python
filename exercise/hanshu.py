#coding=utf-8

def print_models(unprinted_designs, completed_models):
    """
    打印每个设计，知道打印完为止
    每个设计打印完成后，都添加到completed列表中
    """
    while unprinted_designs:
        current_designs = unprinted_designs.pop()
        print("正在打印设计：" + current_designs)
        completed_models.append(current_designs)

def show_completed_models(completed_models):
    """显示所有打印好的设计"""
    print('\n')
    print("这些设计已经被打印好了：")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone', 'ipad', 'itouch', 'ipod']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)