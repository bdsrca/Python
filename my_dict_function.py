class myDict(object):
    """ Implements a dictionary without using a dictionary """

    def __init__(self):
        """ initialization of your representation """
        # FILL THIS IN
        self.dict = []

    def assign(self, k, v):
        """ k (the key) and v (the value), immutable objects  """
        value = (k, v)
        found = 0
        if k == "": raise KeyError

        for i in range(len(self.dict)):
            tup = self.dict[i]
            tup = list(tup)
            if tup[0] == k:
                #found the key
                tup[1] = v
                tup = tuple(tup)
                self.dict[i] = tup
                found = 1
        if not found:
            self.dict.append(value)

    def getval(self, k):
        """ k, immutable object  """
        found1 = 0
        for i in range(len(self.dict)):
            tup1 = self.dict[i]
            tup1 = list(tup1)
            if tup1[0] == k:
                # found the key
                val = tup1[1]
                tup = tuple(tup1)
                found1 = 1
                return val

        if not found1:
            raise KeyError

    def delete(self, k):
        """ k, immutable object """
        for i in range(len(self.dict)):
            tup2 = self.dict[i]
            tup2 = list(tup2)
            if tup2[0] == k:
                tup2 = tuple(tup2)
                self.dict.remove(tup2)
                return
        raise KeyError()



md = myDict()
print(md.dict)
md.assign(1,2)
print(md.dict)
print(md.getval(1))
print(md.dict)
md.delete(1)
print(md.dict)

# a = myDict()
# a.assign("",12)
# a.assign("a",12)
# a.assign("b",11)
# a.assign("a",1)
# a.assign("b",111)
# a.delete("a")
# print(a.dict)
# a.delete("a")

