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
    j = 2
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
        k = 1
        # 2-1-1. 정직원삭제
        if k == 1 :
            pass
        # 2-1-2. 계약직직원삭제
        if k == 2 :
            pass
    # 2-3.직원수정
    elif j == 3 :
        pass
    # 2-4.전체직원 출력
    elif j == 4 :
        print("전체직원을 출력합니다.")
        arrayF = m1.getFull()
        arrayP = m1.getPart()
        print("******정직원******")
        for i in arrayF :
            print(i.getNumber(), i.getName(), i.getRank(),\
                  i.getBirthday(), i.getSalary(), i.getJoinDate(), i.getBonus())
        print("******계약직******")
        for i in arrayP :
            print(i.getNumber(), i.getName(), i.getRank(),\
                  i.getBirthday(), i.getSalary(), i.getJoinDate(), i.getContract())
    # 2-5. 직원검색
    elif j == 5 :
        pass

else :
    print("로그인이 잘못되었습니다.")
