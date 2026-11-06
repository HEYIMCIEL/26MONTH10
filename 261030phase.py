# # # # with open("diary.txt","w",encoding="utf-8") as file:
# # # #     file.write("今日はpython操作学习。\n")
# # # #     file.write("如何打开关上文件。\n")
# # # # print("已保存。")

# # # # with open("diary.txt","r",encoding="utf-8")as file:
# # # #     content=file.read()
# # # # print(content)

# # # # with open("diary.txt","a",encoding="utf-8")as file:
# # # #     file.write("明天继续学习。\n")

# # from pathlib import Path
# # base_dir = Path(__file__).resolve().parent
# # print(base_dir)

# # data_dir=base_dir/"data"
# # data_dir.mkdir(exist_ok=True)

# # file_path=data_dir/"memo.txt"
# # file_path.write_text("正在练习中。\n",encoding="utf=8")

# # print(file_path.exists())
# # print(file_path.read_text(encoding="utf=8"))

# import csv
# sales=[
#     {"product":"note","quantity":2,"price":250},
#     {"product":"pen","quantity":3,"price":120},
# ]

# with open("sale.csv", "w",newline="",encoding="utf-8-sig")as file:
#     writer=csv.DictWriter(file,fieldnames=["product","quantity","price"])
#     writer.writeheader()
#     writer.writerows(sales)

# print("sale.csv制作成。")

# amount=0
# with open("sale.csv","r",newline="",encoding="utf-8-sig")as file:
#     reader=csv.DictReader(file)
#     for row in reader:
#         amount+=int(row["quantity"])*int(row["price"])

# print(f"税后价格合计：{amount:,}円")

# students=[
#     {"name":"nancy","score":80},
#     {"name":"cindy","score":90},
#     {"name":"lucy","score":70},
# ]

# total=0
# row_amount=0
# with open("students","w",newline="", encoding="utf-8-sig")as file:
#     writer=csv.DictWriter(file,fieldnames=["name","score"])
#     writer.writeheader()
#     writer.writerows(students)

# with open ("students","r",newline="", encoding="utf-8-sig")as file:
#     reader=csv.DictReader(file)
#     for row in reader:
#         total=total+int(row["score"])
#         row_amount+=1
#     print(f"学生的平均分：{total/row_amount}")


import json
student ={"name":"jack","age":24,"skills":["python","sql"]}

with open("student.json","w",encoding="utf-8")as file:
    json.dump(student,file,ensure_ascii=False,indent=2)

with open("student.json","r",encoding="utf-8")as file:
    loaded=json.load(file)

print(loaded["name"])
print(loaded["skills"])