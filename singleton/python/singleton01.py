class Singleton:
    _instance = None

    def __new__(self):
        if not isinstance(self._instance, self):
            self._instance = object.__new__(self)
        return self._instance


if __name__ == "__main__":
    a = Singleton()
    b = Singleton()

    print(id(a), id(b))
    print(a == b)
