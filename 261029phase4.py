# # # # def greet(name):
# # # #     print(f"{name}さん、こんにちは。")

# # # # greet("田中")


# # # # def introduce(name,age):
# # # #     print(f"私は{name}です。{age}です。")

# # # # introduce("大和",25)
# # # # introduce("佐渡",34)

# # # def add_item(item, items=None):
# # #     if items is None:
# # #         items=[]
# # #     items.append(item)
# # #     return items

# # # print(add_item())

# # def fruit_cart(*fruits, cart=None):
# #     if cart is None:
# #         cart = []  # 每次现场买个新购物车
    
# #     # 遍历传进来的所有水果，挨个放进购物车
# #     for fruit in fruits:
# #         cart.append(fruit)
        
# #     return cart

# # # 测试一下：一次加多个水果
# # print(fruit_cart("苹果", "香蕉", "西瓜"))

# square=lambda x:x*x
# print(square(5))

my_list = [1, 2, 3, 4, 5, 6, 7]

# 用 map 搭配 lambda 批量乘 2
result = list(map(lambda x: x * 2, my_list))

print(result)