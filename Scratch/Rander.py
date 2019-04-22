class Rander:

    def __init__(self, n=0):
        import time
        self.seed = int(time.time())
        self.__seed = self.seed
        self.__n = n

    def rander_half(self, n):
        if n == 1:
            return self.__seed
        else:
            self.__seed = int(self.__seed)
            length = len(str(self.__seed))
            self.__seed = int(self.__seed**2/pow(10, (length/2))) % int(pow(10.0, length))
            return self.rander_half(n-1)
