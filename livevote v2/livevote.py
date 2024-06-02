#모듈 임포트(advancedprint 모듈은 깃헙에 있어용)
from modules.advanceprint import *
import os
import gspread
import time

os.system('')

#서비스용 API 계정을 만들어야 API를 사용할 수 있는데, 그 때 서비스 계정이 접근할 수 있게 하는 키를 받아야 쓸수 있어요
credentials = "여기에 키 넣기"

#credentials에 넣은 키 내용을 바탕으로 객체를 생성
gc = gspread.service_account_from_dict(credentials)

#실시간 집계하는거
def livevote():
    try:
        while True:
            sp = gc.open('test1')
            votelist = sp.sheet1.col_values(2)
            cd1 = votelist.count('후보1')
            cd2 = votelist.count('후보2')
            cd3 = votelist.count('후보3')
            log_print('진행', "후보1: " + str(cd1) + " 후보2: " + str(cd2) + " 후보3: " + str(cd3), 'blue', sliceprint=False)
            time.sleep(5)
    except KeyboardInterrupt:
    	log_print('중지', '집계를 중단합니다. 메뉴로 이동합니다.', 'red', sliceprint=False)
    	menu()

#파이썬은 goto가 없어서 참 불편해용
def menu():
    log_print('+', 'LIVEVOTE V2', 'green', sliceprint=False)
    log_print('+', 'MADE BY STUDENTS COUNCIL', 'green', sliceprint=False)
    print('')
    log_print('알림', 'Enter키를 누르면 실시간 집계를 시작합니다. 5초 간격으로 수행하며 이는 코드에서 수정할 수 있습니다.', 'yellow', sliceprint=False)
    input("[PRESS ENTER]")
    livevote()
menu()