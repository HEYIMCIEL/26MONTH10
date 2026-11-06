# # # # # print("Hello, Python!") 

# # # # # #str 字符（串）型 +“” system_name="wechat" 不使用驼峰法命名 使用下划线
# # # # # #int（整型 / Integer）：用于表示整数（如 10、-5、0）。在 Python 中，整数的大小没有限制，可以精确计算
# # # # # #float（浮点型 / Floating-point）：用于表示带有小数点的数字（如 3.14、-0.01、2.0）。它用于需要小数精度的场景。
# # # # # #bool（布尔型 / Boolean）：用于表示逻辑值，只有两个取值：True（真）或 False（假），常用于条件判断和循环控制。在 Python 中，bool 实际上是 int（整型）的子类型（True 对应 1，Fale 对应 0）

# # # # # system_name="wechat"
# # # # # print(f"system_name:{type(system_name)}")
# # # # # #f=format 格式化 了解每个变量对应的type

# # # # # ticket_id = 101
# # # # # air_temperature = 36.8

# # # # # flag = False
# # # # # print(f"ticket_id:{type(ticket_id)}")
# # # # # print(f"air_temperature:{type(air_temperature)}")
# # # # # print(flag)

# # # # # name=input("Please Input Your Name:")
# # # # # print(f"ようこそ、{name}")

# # # # # is_urgent = True
# # # # # if is_urgent:
# # # # #     print("emergency contact")
# # # # # else:
# # # # #     print("normal situation")  

# # # # impact_count = 8  # 你可以尝试修改这个数字（比如改成 12、7 或 3）看看不同的结果

# # # # # if impact_count > 10:
# # # # #     print("第一个情况")
# # # # # elif 5 <= impact_count <= 10:
# # # # #     print("第二个情况")
# # # # # else:
# # # # #     print("第三个情况")

# # # # # a=20
# # # # # b=3
# # # # # print(a//b)

# # # # # height=float(input("Please input your height(cm):"))
# # # # # weight=float(input("Please input your weight(kg):"))
# # # # # height_m=height / 100
# # # # # bmi=weight/(height_m **2)
# # # # # print(f"Your BMI is{bmi:.2f}")

# # # # # message="iloveyouforever"
# # # # # print(len(message))
# # # # # print(message[9])
# # # # # print(message.upper())

# # # # # total=999
# # # # # payment=int(input("金额："))
# # # # # change=total-payment
# # # # # print(f"花费金额：{total}元")
# # # # # print(f"金额:{payment}元")
# # # # # print(f"剩余:{change}元")

# # # # # if change<0:
# # # # #     print("金额不足")

# # # # # age=int(input("Please input your age:"))
# # # # # if age>=20:
# # # # #     print("You can legally drink alcohol.")
# # # # # else:
# # # # #     print("You can't legally drink alcohol.")

# # # # # 1. 让用户输入购入金额 (subtotal)
# # # # # subtotal = int(input("输入购入金额："))

# # # # # 2. 用 if-else 条件判断运费 (delivery)
# # # # # if subtotal >= 3000:   # 如果购入金额大于等于 3000
# # # # #     delivery = 0        # 免运费
# # # # # else:                   # 否则（小于 3000）
# # # # #     delivery = 500      # 运费 500

# # # # # # 3. 计算最终总金额 (payment)
# # # # # payment = subtotal + delivery

# # # # # # 4. 打印输出结果（不加双引号才能打印出变量的数字）
# # # # # print(f"运费为：{delivery}")
# # # # # print(f"总金额为：{payment}")

# # # # # 循环 包前不包后
# # # # # for i in range(1,6):
# # # # #     print(i)

# # # # # # 最后的2 步径长度 1/3/5
# # # # # for i in range(1,6,2):
# # # # #     print(i)

# # # # # # sum() 直接对 range(1, 101) 生成的数字序列求和
# # # # # total_sum = sum(range(1, 101))
# # # # # print(total_sum)

# # # # # # 初始化一个变量用来存总和
# # # # # total_sum = 0



# # # # # # 使用 for 循环遍历从 1 到 100 的数字
# # # # # # 注意：range(1, 101) 的意思是：从 1 开始，到 101 结束（但不包含 101），也就是数到 100
# # # # # for i in range(1, 101):
# # # # #     total_sum += i  # 相当于 total_sum = total_sum + i

# # # # # # 打印最终计算结果
# # # # # print(f"从 1 加到 100 的总和是：{total_sum}")

# # # # count=1

# # # # # while count<=5:
# # # # #     print(count)
# # # # #     count+=1


# # # # # while True:
# # # # #     command=input("enter Q to stop:")
# # # # #     if command.lower()=="q":
# # # # #         print("end")
# # # # #         break
# # # # #     print("continue")

# # # # # correctpassword = "imnotcielnow"

# # # # # for i in range(1, 4):  # 循环 3 次（i 的值分别为 1, 2, 3）
# # # # #     enter = input("PassWord: ")
    
# # # # #     if enter == correctpassword:
# # # # #         print("Correct!")
# # # # #         break  # 密码正确，直接跳出循环
# # # # #     else:
# # # # #         print("incorrect")

# # # # # else:
# # # # #     # 注意：这个 else 是和 for 对齐的！
# # # # #     # 意思是指：如果上面 3 次循环全部结束了，却一次都没有触发 break（说明 3 次全猜错），就会执行这里
# # # # #     print("exceed the limit")

# # # # for dan in range(1, 10):
# # # #     for number in range(1, 10):
# # # #         # 修正：将 (dan*number) 改为 {dan*number}
# # # #         print(f"{dan}x{number}={dan*number} ", end="\t")  # 用 \t 可以让格式对得更整齐
# # # #     print()  # 每打印完一行乘法后换行
# # # # # 外层的 for dan in range(1, 10) 代表行数（或者“几的乘法口诀”）。
# # # # # 内层的 for number in range(1, 10) 代表每一行里相乘的另一个数字（从 1 到 9）。
# # # # # end=""（或者用 end="\t" 制表符）可以让原本应该换行输出的结果排在同一行里。
# # # # # 最外层的 print() 负责在内层循环跑完一整行后进行换行。

# # # for dan in range(1, 10):
# # #     # 关键点：让内层循环只数到当前的 dan 为止
# # #     for number in range(1, dan + 1):
# # #         print(f"{dan}x{number}={dan*number}", end="\t")
# # #     print()  # 换行

# # # # 当 dan = 1 时，range(1, 2) 只会循环 1 次（打印 1x1=1）。
# # # # 当 dan = 2 时，range(1, 3) 会循环 2 次（打印 2x1=2 和 2x2=4）。
# # # # 以此类推，当 dan = 9 时，就会完整打印前 9 个算式。

# # import random

# # # 生成 1 到 100 之间的随机数
# # target = random.randint(1, 100)  # 提示：randint(1, 100) 才会真正生成 1~100
# # attemps = 0

# # print("1~100中随机数猜测")

# # while True:
# #     answer_text = input("猜测的数字（到q结束）:")

# #     if answer_text.lower() == "q":
# #         # 修正 1：加上 f，并将 (target) 改为 {target}
# #         print(f"游戏结束，正确答案是 {target}。")
# #         break

# #     try:
# #         answer = int(answer_text)
# #     except ValueError:
# #         print("请输入整数")
# #         continue

# #     if not 1 <= answer <= 100:
# #         print("1~100范围内输入")
# #         continue

# #     # 修正 2：每次有效猜测，尝试次数都要 +1
# #     attemps += 1

# #     if answer < target:
# #         print("更大的数字")
# #     elif answer > target:
# #         print("更小的数字")
# #     else:
# #         # 修正 3：加上 f，并将 (attemps) 改为 {attemps}
# #         print(f"正确！你总共用了 {attemps} 回成功猜出")
# #         break


# import math

# # 初始化一个空列表用来存放购买的商品
# cart = []

# print("=== 欢迎来到自助购物结算系统 ===")
# print("提示：随时可以输入 'q' 结束商品录入并开始结账。\n")

# # 第一阶段：循环输入商品信息
# while True:
#     name_input = input("请输入商品名（输入 q 开始结账）: ")
#     if name_input.lower() == 'q':
#         break
    
#     price_str = input("请输入单价（必须是正整数）: ")
#     if price_str.lower() == 'q':
#         break
        
#     qty_str = input("请输入数量（必须是正整数）: ")
#     if qty_str.lower() == 'q':
#         break
    
#     # 检查单价和数量是否为正整数
#     try:
#         price = int(price_str)
#         qty = int(qty_str)
        
#         if price <= 0 or qty <= 0:
#             print("【错误】单价和数量必须是大于 0 的正整数！请重新输入该商品。\n")
#             continue
#     except ValueError:
#         print("【错误】请输入有效的整数数字！请重新输入该商品。\n")
#         continue
    
#     # 将商品信息以字典形式存入购物车列表
#     cart.append({"name": name_input, "price": price, "qty": qty})
#     print(f"-> 已添加成功：{name_input} | 单价: {price} | 数量: {qty}\n")

# # 第二阶段：开始结算
# if not cart:
#     print("您没有购买任何商品，欢迎下次光临！")
# else:
#     print("\n========== 购物小票清单 ==========")
#     subtotal = 0
#     for item in cart:
#         item_total = item["price"] * item["qty"]
#         subtotal += item_total
#         print(f"商品: {item['name']} | 单价: {item['price']} | 数量: {item['qty']} | 小计: {item_total}")
    
#     print("----------------------------------")
#     print(f"商品税前总额: {subtotal} 円")
    
#     # 计算消费税 (10%)
#     tax_rate = 0.10
#     total_with_tax = subtotal * (1 + tax_rate)
    
#     # 判断税后是否满 5000
#     discount_applied = False
#     if total_with_tax >= 5000:
#         # 满 5000 享受 10% 打折（即总额乘以 0.9）
#         final_amount = total_with_tax * 0.9
#         discount_applied = True
#     else:
#         final_amount = total_with_tax
        
#     # 保留两位小数或取整（这里用 round 保留 2 位小数）
#     final_amount = round(final_amount, 2)
    
#     print(f"含税总额（10%消费税）: {round(total_with_tax, 2)} 円")
#     if discount_applied:
#         print("🎉 恭喜！税后金额满 5000 円，已享受 10% 折扣优惠！")
#     print(f"👉 应付最终金额: {final_amount} 円")
#     print("==================================")
    
#     # 第三阶段：支付与找零/余额循环
#     while True:
#         try:
#             payment_str = input("请投入支付金额: ")
#             payment = float(payment_str)
#         except ValueError:
#             print("【错误】请输入有效的金额数字！")
#             continue
            
#         if payment < final_amount:
#             shortage = round(final_amount - payment, 2)
#             print(f"❌ 金额不足！还差 {shortage} 円，请重新支付。")
#         else:
#             change = round(payment - final_amount, 2)
#             print(f"✅ 支付成功！找零（余额）: {change} 円")
#             print("谢谢惠顾，欢迎下次光临！")
#             break

print("=====简易账单v2=====")

# 1. 记得在最前面初始化 total
total = 0

while True:
    # 2. 必须把 input() 的结果赋值给 product_name
    product_name = input("please input product name: ").strip()

    if product_name == "q":
        break
    if product_name == "":
        print("please input your product")
        continue

    price_text = input("price: ")
    quantity_text = input("quantity: ")

    if not price_text.isdecimal() or not quantity_text.isdecimal():
        print("wrong price or quantity")
        continue

    price = int(price_text)
    quantity = int(quantity_text)

    if price <= 0 or quantity <= 0:
        print("at least have 1")
        continue

    item_total = price * quantity
    total += item_total

    print(f"item total: {item_total}")

# 计算折扣与税费
discount = total * 0.1 if total > 5000 else 0
after_discount = total - discount
tax = after_discount * 0.1
all_total = total + tax

# 3. 加上了 f 前缀，以便正确打印变量数值
print(f"商品原总价：{total}")
print(f"打折减免：{discount}")
print(f"消费税：{tax}")
print(f"应支付总金额：{all_total}")

# 支付循环
while True:
    payment_text = input("总付款：")

    if not payment_text.isdecimal():
        print("请输入0以上数字")
        continue  # 4. 加上 continue，防止非数字导致程序崩溃

    payment = int(payment_text)

    if payment < all_total:
        print(f"金额不足，还需要 {all_total - payment} 元")
        continue

    print(f"找零（余额）：{payment - all_total}")
    print("thank you so much")
    break