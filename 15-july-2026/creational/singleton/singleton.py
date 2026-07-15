class SingleTon:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(SingleTon, cls).__new__(cls)
        return cls._instance
    
db = SingleTon()
db1 = SingleTon()
print(db is db1)  # Output: True

