""" Задача "Учёт товаров":  """


# Необходимо реализовать 2 класса Product и Shop,
# с помощью которых будет производиться запись в файл с продуктами.
# Объекты класса Product будут создаваться следующим образом - Product('Potato', 50.0, 'Vagetables')
# и обладать следующими свойствами:

from pprint import pprint

class Product():
    def __init__(self, name: str, whight: float, cotegory: str):
      self.name = name # название продукта
      self.whight = whight # вес
      self.cotegory = cotegory # катекория продукта

    def str (self):
        return (f"Название : {self.name} , вес: {self.whight} , категория продукта : {self.cotegory}")


class Shop():

    def __init__(self):
        self.__file_name = 'products.txt'



    def get_products(self):
        file = open(self.__file_name, 'r')
        product = file.read()
        file.close()
        return product


    def add(self, *products):
        for i in products:
           veg = (str(i))
           file = open(self.__file_name, 'r')
           pprint(file.read())
           file.close()
           if veg in self.__file_name:
              print(f'Продукт {veg} уже есть в магазине')
           else:
              file = open(self.__file_name, 'a')
              file.write(f'\n{veg}')
              file.close()


if __name__=="__main__":

    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')

    p1.str()
    print(p1)
    p2.str()
    print(p2)
    p3.str()
    print(p3)
    s1.add(p1, p2, p3)
    print(s1.get_products())

