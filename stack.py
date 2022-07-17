class item:
    def __init__(self,data,old_value = None):
        self.data = data
        self.old = old_value

class MyStack:
    def __init__(self):
        self.__item = item(None)

    def push(self,*args):
        for i in args:
            if self.__item:
                self.__item = item(i,old_value=self.__item)
            else:
                self.__item = item(i)

    def getData(self):
        if self.__item:
            return self.__item.data
        else:
            return None

    def pop(self):
        if self.__item:
            self.__item = self.__item.old
    def __len__(self):
        count = -1
        temp_item = self.__item
        while temp_item:
            count+=1
            temp_item = temp_item.old
        return  count

