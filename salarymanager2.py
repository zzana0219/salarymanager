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
login = login(m1)
(i, numberEm) = login

# 1. 사원모드
if i == 1 :
    outputF = m1.findFull(numberEm)
    outputP = m1.findPart(numberEm)
    if not outputF == [] :
        print("사원번호", "이름", "직급", "생일", "기본급", "입사일", "보너스")
        for i in outputF :
            printF(i)
            print("******세후 금액******")
            print(i.monAfter())
    elif not outputP == [] :
        print("사원번호", "이름", "직급", "생일", "기본급", "입사일", "계약기간")
        for i in outputP :
            printP(i)
            print("******세후 금액******")
            print(i.monAfter())
    else :
        print("로그인이 잘못되었습니다.")

# 2. 관리자모드
elif i == 2 :
    while True :
        print("1.직원추가", "2.직원삭제", "3.직원수정", "4.전체직원출력", "5.직원검색", "6.나가기")
        j = input("원하시는 작업을 선택해주세요>")
        # 2-1.직원추가
        if j == "1" :
            while True :
                print("1.정직원추가", "2.계약직직원추가", "3.돌아가기")
                k = input("원하시는 작업을 선택해주세요>")
                # 2-1-1. 정직원추가
                if k == "1" :
                    m1.setFull()
                # 2-1-2. 계약직직원추가
                elif k == "2" :
                    m1.setPart()
                elif k == "3" :
                    break
                else :
                    print("잘못된입력입니다")
                    continue
            continue
        # 2-2.직원삭제
        elif j == "2" :
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
                for i in numberEm :
                    m1.deleteEm(i)
            else :
                print("삭제하지 않았습니다.")
            continue
        # 2-3.직원수정
        elif j == "3" :
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
            continue
        # 2-4.전체직원 출력
        elif j == "4" :
            print("전체직원을 출력합니다.")
            outputF = m1.getFull()
            outputP = m1.getPart()
            print("******정직원******")
            for i in outputF :
                printF(i)
            print("******계약직******")
            for i in outputP :
                printP(i)
            continue
        # 2-5. 직원검색
        elif j == "5" :
            number = input("검색하려는 직원번호를 입력해주세요>")
            outputF = m1.findFull(number)
            outputP = m1.findPart(number)
            for i in outputF :
                printF(i)
            for i in outputP :
                printP(i)
            continue
        # 2-6. 나가기
        elif j == "6" :
            break
        else :
            print("잘못된 입력입니다.")
            continue
        
else :
    print("로그인이 잘못되었습니다.")

