# Implement the Buffer class
# https://stepik.org/lesson/24461/step/9?auth=login&unit=6767

# my solution
class Buffer:
    def __init__(self):
        self.current_list = []
        # конструктор без аргументов

    def add(self, *a):
        # добавить следующую часть последовательности
        self.current_list.extend(a)
        while len(self.current_list) >= 5:
            counter = 0
            for i in range(5):
                num = self.current_list.pop(0)
                counter += num
            print(counter)

    def get_current_part(self):
        # вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были добавлены
        return self.current_list

buf = Buffer()
buf.add(1, 2, 3)
buf.get_current_part() # вернуть [1, 2, 3]
buf.add(4, 5, 6) # print(15) – вывод суммы первой пятерки элементов
buf.get_current_part() # вернуть [6]
buf.add(7, 8, 9, 10) # print(40) – вывод суммы второй пятерки элементов
buf.get_current_part() # вернуть []
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) – вывод сумм третьей и четвертой пятерки
buf.get_current_part() # вернуть [1]

# Good Solution

# class Buffer:
#     def __init__(self):
#         self.part = []
#
#     def add(self, *a):
#         for i in a:
#             self.part.append(i)
#             if len(self.part) == 5:
#                 print(sum(self.part))
#                 self.part.clear()
#
#     def get_current_part(self):
#         return self.part

# Good Solution
# class Buffer:
# 	def __init__(self):
# 		self.l=[]
# 	def add(self, *a):
# 		self.l.extend(a)
# 		while len(self.l)>=5:
# 			print(sum(self.l[:5]))
# 			del(self.l[:5])
# 	def get_current_part(self):
# 		return self.l
