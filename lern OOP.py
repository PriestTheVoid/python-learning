class Test:
    def __init__(self, name):
        self.name = name
        print(f"создан новый объект {self.name}")

    def __del__(self):
        print(f"созданный объект {self.name} удалён")

tom = Test("Tom")