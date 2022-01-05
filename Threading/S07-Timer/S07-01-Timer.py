from threading import Timer

def hello(name, family):
    print(f"hello, world to {name} {family}")

t = Timer(5, hello, args=("Mohammad", "Taghizadeh", ))
t.start()  # after 5 seconds, "hello, world" will be printed