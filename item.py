class Item:
    def __init__(self, zwmc, gsmc, zwyx, gzdd):
        self.zwmc = zwmc
        self.gsmc = gsmc
        self.zwyx = zwyx
        self.gzdd = gzdd

    def __str__(self):
        return "职位名称:{} 公司名称:{} 职位月薪:{} 工作地点:{}".format(self.zwmc, self.gsmc, self.zwyx, self.gzdd)