class Employee :
    def __init__(self) :
        self.__number = "null"
        self.__name = "null"
        self.__rank = "null"
        self.__birthday = "null"
        self.__salary = "null"
        self.__joinDate = "null"

    def setNumber(self,number) :
        self.__number = number
    def setName(self,name) :
        self.__name = name
    def setRank(self,rank) :
        self.__rank = rank
    def setBirthday(self, birthday) :
        self.__birthday = birthday
    def setSalary(self, salary) :
        self.__salary = salary
    def setJoinDate(self, joinDate) :
        self.__joinDate = joinDate
    def getNumber(self) :
        return self.number
    def getName(self) :
        return self.__name
    def getRank(self) :
        return self.__rank
    def getBirthday(self) :
        return self.__birthday
    def getSalary(self) :
        return self.__salary
    def getJoinDate(self) :
        return self.__joinDate
