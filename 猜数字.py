
import random

def guess_number():

    number = random.randint(1, 100)
    num_guesses = 0

    print("欢迎来到猜数字游戏！")
    print("我已经想好了一个 1 到 100 之间的整数。")

    while True:
        try:
            guess = int(input("请输入你猜测的数字："))
        except ValueError:
            print("输入无效，请输入一个整数。")
            continue

        num_guesses += 1

        if guess < number:
            print("猜小了！")
        elif guess > number:
            print("猜大了！")
        else:
            print(f"恭喜你，猜对了！你总共尝试了 {num_guesses} 次。")
            break

if __name__ == "__main__":

    guess_number()

