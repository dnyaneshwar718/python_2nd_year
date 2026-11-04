import gc

class Demo:
    pass

gc.disable()

a = Demo()
b = Demo()

a.ref = b
b.ref = a

print("Automatic GC:", gc.isenabled())

del a
del b

count = gc.collect()

print("Objects collected:", count)

gc.enable()