class TimeMap:
    def __init__(self):
        self.key_store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.key_store:
            self.key_store[key].append((value, timestamp))
        else:
            self.key_store[key] = [(value, timestamp)]
        

    def get(self, key: str, timestamp: int) -> str:
        
        out = ""
        values = self.key_store.get(key, [])

        left = 0
        right = len(values) - 1

        while left <= right:
            mid = (left + right) // 2
            if values[mid][1] <= timestamp:
                out = values[mid][0]
                left = mid + 1
            else:
                right = mid - 1
        
        return out