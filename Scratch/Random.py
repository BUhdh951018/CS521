class Random(object):
    '''Random '''

    def __init__(self, x=None):
        if x is None:
            import time
            self.seed = int(time.time())
        else:
            self.seed = int(x)
        self._seed = self.seed

    def random_LCG(self):
        '''

        X(k) = [a * X(k-1) + c] mod m
        '''
        # The following parameters form GCC compiler
        m = 2 ** 32
        a = 1103515245
        c = 12345
        self._seed = (a * self._seed + c) % m
        return self._seed / float(m - 1)
