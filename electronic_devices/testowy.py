from  statistics import mean

gg = "example.txt"

file = open(gg,"r")

with file as f:
    list_main = []
    for line in f:
        lista = []
        for i in line:
            if i.isdigit():
                lista.append(int(i))
                list_main.append(lista)


print(list_main)

for x in list_main:
    print(mean(x),end=", ")


