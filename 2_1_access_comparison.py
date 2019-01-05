import timeit

setup = """\
class C(object):
    def __init__(self, a):
        self.a = a
c = C(0)
a = c.a
"""
stmt = 'c.a'
print(timeit.timeit(stmt, setup, number=1_000_000))
stmt = 'a'
print(timeit.timeit(stmt, setup, number=1_000_000))