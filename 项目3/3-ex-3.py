target_number=56
attempts=0
game_over=False
while not game_over and attempts<5:
    attempts+=1
    guess_num=input("请输入继续或quit（游戏已退出）")
    if guess_num=='quit':
        game_over==True
        print('游戏已退出')
    else:
        user_input=int(input('请输入0到100之间的数字：'))
        if 1<user_input<100 :
            if user_input>target_number and attempts<5:
                print('太大了')
            elif user_input<target_number and attempts<5:
                print('太小了')
            elif user_input==target_number and attempts<=5:
                print(f"恭喜你，猜对了，你总共猜了{attempts}次。")
                game_over=True
            else:
                game_over=True
                print(f'很遗憾，你已经用完了{attempts}次机会，正确答案是{target_number}')
        else:
            print("请输入一个1到100之间的整数")




