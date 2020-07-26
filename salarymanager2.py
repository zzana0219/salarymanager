from salarymanager import *

# 파일생성하기
mkDB()

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
    # 2-1.정직원 추가
    if j == 1 :
        m1.setFull()
    # 2-2.정직원 출력?
    elif j == 2 :
        print("전체직원을 출력합니다.")
        arrayF = m1.getFull()
        for i in arrayF :
            print(i.getName())

else :
    print("잘못된 사원번호입니다.")
