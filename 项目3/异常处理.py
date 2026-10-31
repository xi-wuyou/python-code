#数值累加器
total=0#初始值
while True:
    try:
        user_input=int(input('请输入整数：'))#可能错误的代码输入
    except ValueError:
        print('错误，请输入整数')
    except KeyboardInterrupt:
        print('程序中断，已退出')
        break
    except Exception as e:
        print('产生意外错误：{type(e).__name__} - {e}')
    else:
        if user_input==0:
            break
        total+=user_input
        print(f'结果为{total}')
    finally:
        pass
print(f'最终结果为：{total}')
    