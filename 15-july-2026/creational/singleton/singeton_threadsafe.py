import threading
class singleton_threadsafe:
    _initialized = False
    _instance = None
    _lock = threading.Lock()
    def __init__(self):
        if not self._initialized:
            with self._lock:
                if not self._initialized:
                    # Initialize the instance here
                    self._initialized = True
                    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(singleton_threadsafe, cls).__new__(cls)
        return cls._instance

db = singleton_threadsafe()
db1 = singleton_threadsafe()
print(db is db1)  # Output: True