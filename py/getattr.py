class C(object):
    def __setattr__(self, name, value):
        print "__setattr__ called:", name, value
        object.__setattr__(self, name, value)

    def __getattr__(self, name):
        print "__getattr__ called:", name

    def __getattribute__(self, name):
        print "__getattribute__ called:",name
        return object.__getattribute__(self, name)

c = C()
c.x = "foo"
print c.__dict__['x']
print c.x
