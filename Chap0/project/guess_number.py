import random

random_number = random.randint(1, 20)

i = 0

while i < 10:

    input_number = int(input("请输入数字："))
    
    if random_number > input_number:
        print("比正确的数字小了。")
        i += 1
        print(f"你还有 {10-i} 次机会可以输入")

    elif random_number < input_number:
        print("比正确的数字大了。")
        i += 1
        print(f"你还有 {10-i} 次机会可以输入")

    else:
        print(f"答案正确，答案就是 {random_number}")
        print("结束")
        break

    if i == 10:
        print("结束")
    else:
        pass

        
