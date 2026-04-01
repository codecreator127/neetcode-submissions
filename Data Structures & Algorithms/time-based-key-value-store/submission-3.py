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

        if key not in self.key_store:
            return out

        values = self.key_store[key]

        left = 0
        right = len(values) - 1

        if timestamp >= values[-1][1]:
            return values[-1][0]


        while left <= right:
            middle = (left + right) // 2

            if middle < len(values) - 1 and timestamp >= values[middle][1] and timestamp < values[middle + 1][1]:
                return values[middle][0]

            if values[middle][1] > timestamp:
                right = middle - 1
            else:
                left = middle + 1

        if values[middle][1] < timestamp:
            return values[middle][0]

        return out
