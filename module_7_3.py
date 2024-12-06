
"""  Задача "Найдёт везде":      """
class WordsFinder():
    def __init__(self, name):
        self.name = name

    def get_all_words (self):
        all_worlds = {}
        a = ''
        znak= [',', '.', '=', '!', '?', ';', ':', ' - ']
        with open (self.name,encoding="utf-8") as file:
             for wd in file:
                 wd = wd.lower()
                 for j in wd:
                    if j in znak:
                       wd = wd.replace(j," ")
                 a = a + wd
                 all_worlds.update({self.name: a.split()})

             return all_worlds

    def find(self, txt):
        dist = {}
        world = self.get_all_words()[self.name]
        for i in range(len(world)):
            if txt.lower() == world[i]:
                dist.update({self.name: i + 1})
                return dist

    def count(self, txt):
        dist = {}
        n = 1
        world = self.get_all_words()[self.name]
        dist.update({self.name: world.count(txt.lower())})
        # dist.update({self.file_names: n})
        return dist

res = WordsFinder("text1.txt")
print(res.get_all_words())
print(res.find('детство'))
print(res.count('весна'))