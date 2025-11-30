class Time:
    def __init__(self, h, m, s):
        self.__hour = h
        self.__minute = m
        self.__second = s

    def __add__(self, other):
        h = self.__hour + other._Time__hour
        m = self.__minute + other._Time__minute
        s = self.__second + other._Time__second

        if s >= 60:
            m += s // 60
            s = s % 60

        if m >= 60:
            h += m // 60
            m = m % 60

        return Time(h, m, s)

    def display(self):
        print("hour:minute:second")
        print(f"{self.__hour}:{self.__minute}:{self.__second}")


t1 = Time(2, 34, 56)
t2 = Time(1, 45, 50)
t3 = t1 + t2
t3.display()
