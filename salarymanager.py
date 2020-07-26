from pickle import dump, load
import os

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
    def getBonus(self) :
        return self.__bouns

# 관리자
class Manager() :
    def __init__(self) :
        (self.__full, self.__part) = pullDB() #사원이 없다면 ([],[])

    def setFull(self) :
        f = Full()
        f.setNumber(input("사원번호를 입력해주요>"))
        f.setName(input("이름을 입력해주요>"))
        f.setRank(input("직급을 입려해주요>"))
        f.setBirthday(input("생일을 입력해주세요>"))
        f.setSalary(input("기본급을 입력해주세요>"))
        f.setJoinDate(input("입사일을 입력해주세요>"))
        f.setBonus(input("보너스를 입력해주세요>"))
        self.__full.append(f)
        pushDB(self)        
    def setPart(self) :
        self.__part = part
    def getFull(self) :
        return self.__full
    def getPart(self) :
        return self.__part


# 파일가져오기
def pullDB() :
    if os.path.getsize("databaseF.p") > 0 :
        with open("databaseF.p","br") as fileF :
            arrayF = load(fileF)
    else :
        arrayF = []
    if os.path.getsize("databaseP.p") > 0 :
        with open("databaseP.p","br") as fileP :
            arrayP = load(fileP)
    else :
        arrayP = []
    print("데이터로딩 완료")
    return (arrayF, arrayP)

# 파일입력하기
def pushDB(manager) :
    with open("databaseF.p","bw") as fileF :
        dump(manager.getFull(), fileF)
    with open("databaseP.p","bw") as fileP :
        dump(manager.getPart(), fileP)
    print("데이터입력완료")
