class Singleton:
    _instance = None
    _initialized = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self, *args, **kwargs):
        if not self._initialized:
            self._initialized = True
            print("Singleton instance initialized.")

db = Singleton()
db1 = Singleton()