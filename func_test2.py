# 装饰器
def tips2(args):
    def tips(func):
        def cal(a, b):
            print('start，装饰器传递的参数为 %s，被装饰的函数名为 %s' %(args,func.__name__))
            data = func(a, b)
            print(data)
            print('end')

        return cal

    return tips


@tips2('sum_model')
def sum(a, b):
    return a + b


@tips2('sub_model')
def sub(a, b):
    return a - b


sum(1, 2)
sub(1, 2)
