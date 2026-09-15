class TimeMap:

    def __init__(self):
        self.d = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d:  
            self.d[key] = [(value, timestamp)]
        else:
            self.d[key].append((value, timestamp))
        
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ""

        values = self.d[key]

        if values[0][1] > timestamp:
            return ""

        
        l, r = 0, len(values) - 1

        while l <= r:
            m = (l + r) // 2

            if values[m][1] == timestamp:
                return values[m][0]

            elif values[m][1] < timestamp:
                l = m + 1
            
            else:
                r = m - 1
        
        return values[r][0]

        

        
 