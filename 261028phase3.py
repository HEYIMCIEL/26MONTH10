# # # # # # This is a list!
# # # # # fruits=["りんご","みかん","バナナ"]
# # # # # print(fruits[0])
# # # # # print(fruits[-1])

# # # # # fruits.pop()
# # # # # print(fruits)
# # # # # fruits.append("なし")
# # # # # print(fruits)

# # # # # fruits.insert(0,"スイカ")
# # # # # print(fruits)

# # # # # prices=[3,4,5,6]

# # # # # total=0
# # # # # for p in prices:
# # # # #     total=total+p

# # # # # print(f"合计：{total}")


# # # # numbers=[1,2,3,4,5,6,7]
# # # # multiply=[n*2 for n in numbers]
# # # # evens=[n for n in numbers if n % 2 == 0]
# # # # odds=[n for n in numbers if (n+1) % 2 == 0]

# # # # print(multiply)
# # # # print(evens)
# # # # print(odds)

# # # scores=[45,70,85,60,95]
# # # average=sum(scores)/len(scores)
# # # maxscore=max(scores)
# # # qualifiedscore= [s for s in scores if s >= 60]

# # # print(average)
# # # print(scores)
# # # print(qualifiedscore)

# # student={
# #     "id":101,
# #     "name":"田中",
# #     "score":85,
# # }

# # print(student["id"])
# # print(student["name"])
# # print(student["score"])

# product={"name":"NOTE","price":200}
# # create
# product["stock"]=30
# print(product)
# # read
# print(product["price"])
# print(product.get("category","undefined"))
# # update
# product["price"]=220
# # delete
# removed_stock=product.pop("stock")
# print(removed_stock)
# print(product)

# for key in product:
#     print(key)

# for value in product.values():
#     print(value)

# for key, value in product.items():
#     print(f"{key}:{value}")

cart= [
    {"name":"note","price":250,"quantity":2},
    {"name":"pen","price":150,"quantity":3},
    {"name":"note","price":250,"quantity":1},
]

remove_name=input("delete product name:").strip()
original_count=len(cart)
cart=[product for product in cart if product["name"]!=remove_name]

print(f"delete number:{original_count-len(cart)}件")
print("after deletion:",cart)