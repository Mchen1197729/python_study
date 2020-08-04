class Chain(object):
    def __init__(self, url=''):
        self.url = url

    def __str__(self):
        return self.url

    __repr__ = __str__

    def __getattr__(self, url):
        return Chain('%s/%s' % (self.url, url))

    # 处理参数 /:idc
    def idc(self, idc):
        return Chain('%s/%s' % (self.url, idc))


c1 = Chain('http://localhost:5400')
print(c1.message.author.list)  # http://localhost:5400/message/author/list

print(c1.message.author.list.idc(100))  # http://localhost:5400/message/author/list/100
