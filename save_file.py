from pymongo import MongoClient
import bson.binary

conn = MongoClient("localhost", 27017)
db = conn.images
myset = db.cat

# 存储图片
# with open("cat01.jpeg", "rb") as f:
#     data = f.read()
#
# # 将data转换为bson格式
# content = bson.binary.Binary(data)
#
# # 插入到集合之中
# dic = {"file_name":"cat01", "data":content}
# myset.insert_one(dic)

# 提取文件
img = myset.find_one({"file_name":"cat01"})
# print(img)
with open("f_cat.jpg","wb") as f:
    f.write(img["data"])


conn.close()



