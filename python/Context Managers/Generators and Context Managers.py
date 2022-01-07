def my_gen():
    try:
        print("creating context and yeilding object..")
        lst = [1, 2, 3, 4, 5]
        yield lst
    finally:
        print("exiting contexy and cleaning up")

gen = my_gen() #create Generator

lst = next(gen) # enter context and get "as" object

print(lst)

# next(gen) # exit context but must catch the StopIteration exception

gen = my_gen()
lst = next(gen)
print(lst)

try:
    next(gen)
except StopIteration:
    pass


#context manager that can use the type of generator

class GenCtxManager:
    def __init__(self, gen_func):
        self._gen = gen_func()
    
    def __enter__(self):
        return next(self._gen)

    def __exit__(self, exc_type, exc_value, exc_tb):
        try:
            next(self._gen)
        except StopIteration:
            pass
        return False

with GenCtxManager(my_gen) as lst:
    print(lst)


class GenCtxManager:
    def __init__(self, gen_func, *args, **kwargs):
        self._gen = gen_func(*args, **kwargs)

    def __enter__(self):
        return next(self._gen)

    def __exit__(self, exc_type, exc_value, exc_tb):
        try:
            next(self._gen)
        except StopIteration:
            pass
        return False

def open_file(fname, mode):
    try:
        print("opening file")
        f = open(fname, mode)
        yield f
    finally:
        print("closeing file")
        f.close()

with GenCtxManager(open_file, 'test.txt', 'w') as f:
    print('writing to file')
    f.write("testing")

with open("test.txt") as f:
    print(next(f))