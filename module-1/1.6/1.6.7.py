class SingletonFive:

    amount_of_created_objects = 0
    max_amount_of_objects = 5
    last_instance = None

    def __new__(cls, *args, **kwargs):
        if cls.amount_of_created_objects < cls.max_amount_of_objects:
            cls.last_instance = super().__new__(cls)
        cls.amount_of_created_objects += 1

        return cls.last_instance

    def __del__(self):
        SingletonFive.amount_of_created_objects -= 1

    def __init__(self, name):
        self.name = name


objs = [SingletonFive(str(n)) for n in range(10)]
del objs[4:10]
obj_new = SingletonFive('hello')
objs.append(obj_new)
obj_new_2 = SingletonFive('hel')
objs.append(obj_new_2)
print(objs)
