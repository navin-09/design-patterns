from  threading import Lock
class ThreadSafeSingleTon:
    _instance = None
    _initialized = None
    _lock = Lock()

    def __new__(cls,*args, **kwargs):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self, *args, **kwargs):
        if not self._initialized:
            with self._lock:
                if not self._initialized:
                    self._initialized = True
                    print("Thread-safe Singleton instance initialized.")

db = ThreadSafeSingleTon()
db1 = ThreadSafeSingleTon()
print(db is db1)  # Output: True

