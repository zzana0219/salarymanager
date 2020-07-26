from salarymanager import *
import os

# 파일생성하기(파일이 없다면)
if not (os.path.exists("databaseF.p")) :
    with open("databaseF.p","bw") as fileF :
        pass
if not (os.path.exists("databaseP.p")) :
    with open("databaseP.p","bw") as fileP :
        pass

# 매니저객체 생성
m1 = Manager()

# 로그인
# 관리자클래스에 로그인하는 로직을 넣어야 하나?

i = 2
# 1. 사원모드
if i == 1 :
    pass

# 2. 관리자모드
elif i == 2 :
    j = 4
    # 2-1.직원추가
    if j == 1 :
        k = 1
        # 2-1-1. 정직원추가
        if k == 1 :
            m1.setFull()
        # 2-1-2. 계약직직원추가
        if k == 2 :
            m1.setPart()
    # 2-2.직원삭제
    elif j == 2 :
        numberEm = input("삭제하려는 직원번호를 입력해주세요>")
        outputF = m1.findFull(numberEm)
        outputP = m1.findPart(numberEm)
        print("******정직원******")
        for i in outputF :
            printF(i)
        print("******계약직******")
        for i in outputP :
            printP(i)
        i = input("정말 지우시겠습니까?(Y/N)>")
        if i in ["Y", "y"] :
            m1.deleteEm(numberEm)
        else :
            print("삭제하지 않았습니다.")
    # 2-3.직원수정
    elif j == 3 :
        numberEm = input("수정하려는 직원번호를 입력해주세요>")
        outputF = m1.findFull(numberEm)
        outputP = m1.findPart(numberEm)
        print("어떤것을 수정하시겠습니까?")
        for i in outputF :
            printF(i)
        for i in outputP :
            printP(i)
        for i in outputF :
            print("1.사원번호\n2.이름\n3.직급\n4.생일\n5.기본급\n6.입사일\n7.보너스")
            numberIn = int(input("번호를 입력해주세요.>"))
            m1.modify(numberEm, numberIn)
        for i in outputP :
            print("1.사원번호\n2.이름\n3.직급\n4.생일\n5.기본급\n6.입사일\n7.계약기간")
            numberIn = int(input("번호를 입력해주세요.>"))
            m1.modify(numberEm, numberIn)
    # 2-4.전체직원 출력
    elif j == 4 :
        print("전체직원을 출력합니다.")
        outputF = m1.getFull()
        outputP = m1.getPart()
        print("******정직원******")
        for i in outputF :
            printF(i)
        print("******계약직******")
        for i in outputP :
            printP(i)
    # 2-5. 직원검색
    elif j == 5 :
        number = input("검색하려는 직원번호를 입력해주세요>")
        outputF = m1.findFull(number)
        outputP = m1.findPart(number)
        for i in outputF :
            printF(i)
        for i in outputP :
            printP(i)
        

else :
    print("로그인이 잘못되었습니다.")
