# Implement the MoneyBox class
# https://stepik.org/lesson/24461/step/8?auth=login&unit=6767
class MoneyBox:
    def __init__(self, capacity, money_cop=0):
        self.capacity = capacity
        self.money_cop = money_cop
        # конструктор с аргументом – вместимость копилки

    def can_add(self, v):
        if (self.money_cop + v) <= self.capacity:
            return True
        else:
            return False
        # True, если можно добавить v монет, False иначе

    def add(self, v):
        if self.can_add(v):
            self.money_cop += v
        return self.money_cop

        # положить v монет в копилку


first_cop = MoneyBox(5)
first_cop.add(5)
print(first_cop.add((1)))
