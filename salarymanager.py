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
        self.__passWord = "0000" #비밀번호

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
    def setPassWord(self, passWord) :
        self.__passWord = passWord
    def getNumber(self) :
        return self.__number
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
    def getPassWord(self) :
        return self.__passWord

# 비정규직
class Part(Employee) :
    def __init__(self) :
        Employee.__init__(self)
        self.__contract = "null"  #계약기간

    def setContract(self, contract) :
        self.__contract = contract
    def getContract(self) :
        return self.__contract
    def monAfter(self) :
        return self.getSalary() * 0.85

# 정규직
class Full(Employee) :
    def __init__(self) :
        Employee.__init__(self)
        self.__bonus = "null"  #성과급

    def setBonus(self, bonus) :
        self.__bouns = bonus
    def getBonus(self) :
        return self.__bouns
    def monAfter(self) :
        return (self.getSalary() + self.getBonus()) * 0.85

# 관리자
class Manager() :
    def __init__(self) :
        (self.__full, self.__part) = pullDB() #사원이 없다면 ([],[])

    def setFull(self) :
        f = Full()
        try :
            f.setNumber(input("사원번호를 입력해주요>"))
            f.setName(input("이름을 입력해주요>"))
            f.setRank(input("직급을 입려해주요>"))
            f.setBirthday(input("생일을 입력해주세요>"))
            f.setSalary(int(input("기본급을 입력해주세요>")))
            f.setJoinDate(input("입사일을 입력해주세요>"))
            f.setBonus(int(input("보너스를 입력해주세요>")))
        except :
            print("잘못된 값을 입력하셨습니다.")
            exit
        self.__full.append(f)
        pushDB(self)        
    def setPart(self) :
        p = Part()
        try :
            p.setNumber(input("사원번호를 입력해주요>"))
            p.setName(input("이름을 입력해주요>"))
            p.setRank(input("직급을 입려해주요>"))
            p.setBirthday(input("생일을 입력해주세요>"))
            p.setSalary(int(input("기본급을 입력해주세요>")))
            p.setJoinDate(input("입사일을 입력해주세요>"))
            p.setContract(input("계약기간을 입력해주세요>"))
        except :
            print("잘못된 값을 입력하셨습니다.")
            exit
        self.__part.append(p)
        pushDB(self)
    def getFull(self) :
        return self.__full
    def getPart(self) :
        return self.__part
    def findFull(self, number) :
        outputF = []
        for j in self.__full :
            if j.getNumber() == number :
                outputF.append(j)
        return outputF
    def findPart(self, number) :
        outputP = []
        for j in self.__part :
            if j.getNumber() == number :
                outputP.append(j)
        return outputP
    def modify(self, numberEm, numberIn) :
        outputF = self.findFull(numberEm)
        outputP = self.findPart(numberEm)
        output = outputF + outputP
        try :
            if numberIn > 6 :       #보너스와 계약기간 변경
                for i in outputF :  #보너스 변경
                    i.setBouns(int(input("변경할 값을 입력하세요>")))
                    pushDB(self)
                for i in outputP :  #계약기간변경
                    i.setContract(input("변경할 값을 입력하세요>"))
                    pushDB(self)
            elif numberIn > 5 :     #입사일 변경
                for i in output :
                    i.setJoinDate(input("변경할 값을 입력하세요>"))
                    pushDB(self)
            elif numberIn > 4 :     #기본급 변경
                for i in output :
                    i.setSalary(int(input("변경할 값을 입력하세요>")))
                    pushDB(self)
            elif numberIn > 3 :     #생일 변경
                for i in output :
                    i.setBirthday(input("변경할 값을 입력하세요>"))
                    pushDB(self)
            elif numberIn > 2 :     #직급 변경
                for i in output :
                    i.setRank(input("변경할 값을 입력하세요>"))
                    pushDB(self)
            elif numberIn > 1 :     #이름 변경
                for i in output :
                    i.setName(input("변경할 값을 입력하세요>"))
                    pushDB(self)
            elif numberIn > 0 :     #사원번호 변경
                for i in output :
                    print("***경고 : 사원번호를 신중하게 변경하세요.***")
                    i.setNumber(input("변경할 값을 입력하세요>"))
                    pushDB(self)
        except :
            print("잘못된 값을 입력하셨습니다.")
            exit
        else :
            print("잘못된 입력입니다.")
    def deleteEm(self, numberEm) :
        self.__full = [i for i in self.getFull() if (i.getNumber() != numberEm)]
        self.__part = [i for i in self.getPart() if (i.getNumber() != numberEm)]
        pushDB(self)

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

# 로그인
def login(m) :
    while True :
        numberEm = input("직원번호를 입력해주세요>")
        passWord = input("비밀번호를 입려해주세요>")
        if (numberEm  == "9999") and (passWord == "4321") :
            return (2, "9999")
        output = m.findFull(numberEm) + m.findPart(numberEm)
        for i in output :
            if i.getPassWord() == passWord :
                print("로그인되었습니다.")
                return (1, numberEm)
            else :
                print("잘못된정보입니다.")
                continue

# 프린트
def printF(i) :
    print(i.getNumber(), i.getName(), i.getRank(),\
                  i.getBirthday(), i.getSalary(), i.getJoinDate(), i.getBonus())
def printP(i) :
    print(i.getNumber(), i.getName(), i.getRank(),\
                  i.getBirthday(), i.getSalary(), i.getJoinDate(), i.getContract())
