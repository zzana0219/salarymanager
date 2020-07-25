class Employee :
    def __init__(self) :
        self.__number = "null"   #사원번호
        self.__name = "null"     #이름
        self.__rank = "null"     #직급
        self.__birthday = "null" #생일
        self.__salary = "null"   #기본금
        self.__joinDate = "null" #입사일

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

# 비정규직
class Part(Employee) :
    def __init__(self) :
        Employee.__init__(self)
        self.__contract = "null"  #계약기간

    def setContract(self, contract) :
        self.__contract = contract
    def getContract(self) :
        return self.__contract

# 정규직
class Full(Employee) :
    def __init__(self) :
        Employee.__init__(self)
        self.__bonus = "null"  #성과급

    def setBonus(self, bonus) :
        self.__bouns = bonus
    def getContract(self) :
        return self.__bouns

# 관리자
class Manager() :
    full = []  #정규직사원들
    part = []  #비정규직사원들
    def __init__(self) :
        pass
    
