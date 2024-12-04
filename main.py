from  pprint import pprint
name = "smile.txt"
file = open(name,"r",encoding="utf-8")
print(file)
pprint(file.read())
file.close()
name = "smile.txt"
file = open(name,"w",encoding="utf-8")
file.write("Здраствуйте ,меня зовут Маришка")
file.close()
name = "smile.txt"
file = open(name,"a",encoding="utf-8")
file.write("\nУ меня наступили каникулы")
file.close()
name = "smile.txt"
file = open(name,"a+",encoding="utf-8")
file.write("\nЯ собираюсь в поездку на море")
file.close()
name = "sun.txt"
file = open(name,"a",encoding="utf-8")
file.write("\n Я обожаю морские прогулки")
file.close()