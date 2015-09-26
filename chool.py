__author__ = 'sorokin'
import json

a = open("Students.json")
b = open("Teachers.json")

#st = a.read()
#th = b.read()

students = json.load(a)
teachers = json.load(b)


print("Имена студентов")
for el in students:
    print(el["name"])


for el2 in students:
    print (el["school"])

print("Имена учителей")
for el1 in teachers:
    print(el1["name"])

for el1 in teachers:
    print(el1["school"])



for el in students :
    print(el["class"])
    print(el["name"] , el["surname"])