from collections import defaultdict


class TimeMap(object):

    def __init__(self):
        self.time_dict = defaultdict(list)

    def set(self, key, value, timestamp):
        self.time_dict[key].append((timestamp, value))

    def get(self, key, timestamp):
        res = ""
        value = self.time_dict.get(key, [])

        l, r = 0, len(value) - 1

        while l <= r:
            m = (l + r) // 2

            if value[m][0] <= timestamp:
                res = value[m][1]
                l = m + 1
            else:
                r = m - 1

        return res

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
