import json
import requests

result = requests.get("http://saral.navgurukul.org/api/courses")
data = result.json()
with open("availablecourse.json","w") as file:
    json.dump(data,file,indent=4)
# print(data)

n = 0
id = []
for i in data["availableCourses"]:
    print(n, i["name"],":", i["id"])
    id.append(i["id"])
    n += 1
    # print(id)

user = int(input("enter your serial number:"))
d = 0
req = requests.get("http://saral.navgurukul.org/api/courses/"+id[user]+"/exercises")
f = req.json()
list = []
for i in f["data"]:
    print(d,i["slug"])
    list.append(i["slug"])
    d += 1

user2 = int(input("enter the slug number:"))

h = requests.get("http://saral.navgurukul.org/api/courses/"+str(user)+"/exercise/getBySlug?slug=" +list[user2])
i = h.json()
print(i)


# import requests
# import json 
# result =requests.get("https://saral.navgurukul.org/api/courses")
# data=result.json()

# with open("availablecourses.json","w") as f:
#     json.dump(data,f,indent=4)

# def option(select,var1,slug,data2):
#     while True:
#         a=var1
#         print("***")
#         options=input("enter your options : up, next, exit back   !")
#         if options=="up":
#             print(a)
#             a-=1
#             req=requests.get("https://saral.navgurukul.org/api/courses/"+str(select)+"/exercise/getbyslug?slug = "+str(slug[a]))
#             x=req.json()
#             print("content",x["content"])    
#     while (True):
#         available_letters = get_available_letters(letters_guessed)
#         print ("Available letters: ") + avai
#         print(a)
#         if options=="next":
#             x+=1
#             req=requests.get("https://saral.navgurukul.org/api/courses/"+str(select)+"/exercise/getbyslug?slug = "+str(slug[a-1]))
#             x1=req.json()
#             print(a)
#         elif options=="back":
#             y=1
#             for dic1 in data2["data"]:
#                 print(y,dic1["name"])
#                 y+=1
#                 print("content",x1["content"])
#                 for i in dic1 [" childExercises "]:
#                     print("      ",y,i["name"])
#                     y+=1
#         else:
#             break
# def course(): 
#     index=0
#     for i in data["availableCourses"]:
#         print(index+1,i["name"],i["id"])
#         index+=1
#     for courses in data["availableCourses"]:
#         course=int(input("enter the your index of course = "))
#         select=data["availableCourses"][courses-1]["id"]
#         var=requests.get("http://saral.navgurukul.org/api/courses/"+str(select)+"/exercise")
#         data2=var.json()
#         count=1
#         slug=[ ]
#         for dic_data2 in data2["data"]:
#             print(count,dic_data2["name"])
#             slug.append(dic_data2["slug"])
#             count=count+1
#             for child in dic_data2["childExercises"]:
#                 print(count,child)["name"]
#                 slug.append(dic_data2["slug"])
#                 count=count+1
#         var2=int(input("select content slug"))
#         var3=requests.get("http://saral.navgurukul.org/api/courses/"+str(select)+"/exercise")
#         data3=var3.json
#         print("content",data3["content"])        
#         option (select,var2,slug,data2)
# course()