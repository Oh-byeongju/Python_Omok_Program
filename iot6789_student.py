from player import *
from stone import *
from random import *

class iot6789_student(player):
     def __init__(self, clr):
          super().__init__( clr)  # call constructor of super class
          self.__max_x= 9
          self.__max_y= 9

     def __del__(self):  # destructor
         pass

     def ai_calculate(self,board):
        weight = 0   # ai가 돌상태를 수치화 했을 때의 값
        sum = 0   # ai가 오목보드상태를 수치화 했을 때의 값
        enemy = 1
        team = -1
        stone = []

        for i in range(0,22):
            stone.append([])
            for j in range(0,22):
                try:
                    stone[i].append(board[i][j])
                except:
                    stone[i].append(3)
        for i in range(0, 19):
            for k in range(0, 19):

                #가로 경우의수
                # ooooo 승리시
                if (stone[i][k - 2] == team and stone[i][k - 1] == team and stone[i][k] == team and stone[i][k + 1] == team and
                        stone[i][k + 2] == team):
                    weight = 100000
                    sum = sum + weight

                # oooo 4개 연속
                if (stone[i][k - 2] == team and stone[i][k - 1] == team and stone[i][k] == team and stone[i][
                    k + 1] == team and stone[i][k + 2] == 0):
                    weight = 500
                    sum = sum + weight

                # oooox 4개 연속 막힘
                if (stone[i][k - 2] == team and stone[i][k - 1] == team and stone[i][k] == team and stone[i][
                    k + 1] == team and stone[i][k + 2] == enemy):
                    weight = 400
                    sum = sum + weight

                # xoooo 4개 연속 막힘
                if (stone[i][k - 2] == enemy and stone[i][k - 1] == team and stone[i][k] == team and stone[i][k + 1] == team and
                      stone[i][k + 2] == team):
                    weight = 400
                    sum = sum + weight

                # ooo 3개 연속
                if (stone[i][k - 2] == 0 and stone[i][k - 1] == team and stone[i][k] == team and stone[i][k + 1] == team and
                      stone[i][k + 2] == 0):
                    weight = 60
                    sum = sum + weight

                # ooox 3개 연속 막힘
                if (stone[i][k - 2] == 0 and stone[i][k - 1] == team and stone[i][k] == team and stone[i][k + 1] == team and
                      stone[i][k + 2] == enemy):
                    weight = 40
                    sum = sum + weight

                # xooo 3개 연속 막힘
                if (stone[i][k - 2] == enemy and stone[i][k - 1] == team and stone[i][k] == team and stone[i][k + 1] == team and
                      stone[i][k + 2] == 0):
                    weight = 40
                    sum = sum + weight

                # oo 2개 연속
                if (stone[i][k - 1] == 0 and stone[i][k] == team and stone[i][k + 1] == team and stone[i][k + 2] == 0):
                    weight = 20
                    sum = sum + weight

                # oox 2개 연속 막힘
                if (stone[i][k - 1] == 0 and stone[i][k] == team and stone[i][k + 1] == team and stone[i][k + 2] == enemy):
                    weight = 10
                    sum = sum + weight

                # xoo 2개 연속 막힘
                if (stone[i][k - 1] == enemy and stone[i][k] == team and stone[i][k + 1] == team and stone[i][k + 2] == 0):
                    weight = 10
                    sum = sum + weight


                #세로 경우의수
                # ooooo 승리시
                if (stone[i - 2][k] == team and stone[i - 1][k] == team and stone[i][k] == team and stone[i + 1][
                    k] == team and stone[i + 2][k] == team):
                    weight = 100000
                    sum = sum + weight

                # oooo 4개 연속
                if (stone[i - 2][k] == team and stone[i - 1][k] == team and stone[i][k] == team and stone[i + 1][
                    k] == team and stone[i + 2][k] == 0):
                    weight = 500
                    sum = sum + weight

                # oooox 4개 연속 막힘
                if (stone[i - 2][k] == team and stone[i - 1][k] == team and stone[i][k] == team and stone[i + 1][
                    k] == team and stone[i + 2][k] == enemy):
                    weight = 400
                    sum = sum + weight

                # xoooo 4개 연속 막힘
                if (stone[i - 2][k] == enemy and stone[i - 1][k] == team and stone[i][k] == team and stone[i + 1][k] == team and
                      stone[i + 2][k] == team):
                    weight = 400
                    sum = sum + weight

                # ooo 3개 연속
                if (stone[i - 2][k] == 0 and stone[i - 1][k] == team and stone[i][k] == team and stone[i + 1][k] == team and
                      stone[i + 2][k] == 0):
                    weight = 60
                    sum = sum + weight

                # ooox 3개 연속 막힘
                if (stone[i - 2][k] == 0 and stone[i - 1][k] == team and stone[i][k] == team and stone[i + 1][k] == team and
                      stone[i + 2][k] == enemy):
                    weight = 40
                    sum = sum + weight

                # xooo 3개 연속 막힘
                if (stone[i - 2][k] == enemy and stone[i - 1][k] == team and stone[i][k] == team and stone[i + 1][k] == team and
                      stone[i + 2][k] == 0):
                    weight = 40
                    sum = sum + weight

                # oo 2개 연속
                if (stone[i - 1][k] == 0 and stone[i][k] == team and stone[i + 1][k] == team and stone[i + 2][k] == 0):
                    weight = 20
                    sum = sum + weight

                # oox 2개 연속 막힘
                if (stone[i - 1][k] == 0 and stone[i][k] == team and stone[i + 1][k] == team and stone[i + 2][k] == enemy):
                    weight = 10
                    sum = sum + weight

                # xoo 2개 연속 막힘
                if (stone[i - 1][k] == enemy and stone[i][k] == team and stone[i + 1][k] == team and stone[i + 2][k] == 0):
                    weight = 10
                    sum = sum + weight

                # 대각선 경우의 수
                # ooooo 승리시
                if (stone[i - 2][k + 2] == team and stone[i - 1][k + 1] == team and stone[i][k] == team and stone[i + 1][
                    k - 1] == team and stone[i + 2][k - 2] == team):
                    weight = 100000
                    sum = sum + weight

                # oooo 4개 연속
                if (stone[i - 2][k + 2] == team and stone[i - 1][k + 1] == team and stone[i][k] == team and stone[i + 1][
                    k - 1] == team and stone[i + 2][k - 2] == 0):
                    weight = 500
                    sum = sum + weight

                # oooox 4개 연속 막힘
                if (stone[i - 2][k + 2] == team and stone[i - 1][k + 1] == team and stone[i][k] == team and stone[i + 1][
                    k - 1] == team and stone[i + 2][k - 2] == enemy):
                    weight = 400
                    sum = sum + weight

                # xoooo 4개 연속 막힘
                if (stone[i - 2][k + 2] == enemy and stone[i - 1][k + 1] == team and stone[i][k] == team and stone[i + 1][
                    k - 1] == team and stone[i + 2][k - 2] == team):
                    weight = 400
                    sum = sum + weight

                # ooo 3개 연속
                if (stone[i - 2][k + 2] == 0 and stone[i - 1][k + 1] == team and stone[i][k] == team and stone[i + 1][
                    k - 1] == team and stone[i + 2][k - 2] == 0):
                    weight = 70
                    sum = sum + weight

                # ooox 3개 연속 막힘
                if (stone[i - 2][k + 2] == 0 and stone[i - 1][k + 1] == team and stone[i][k] == team and stone[i + 1][
                    k - 1] == team and stone[i + 2][k - 2] == enemy):
                    weight = 50
                    sum = sum + weight

                # xooo 3개 연속 막힘
                if (stone[i - 2][k + 2] == enemy and stone[i - 1][k + 1] == team and stone[i][k] == team and stone[i + 1][
                    k - 1] == team and stone[i + 2][k - 2] == 0):
                    weight = 50
                    sum = sum + weight

                # oo 2개 연속 얘만 가중치를 더 줌 밑에 대각선은 30임
                if (stone[i - 1][k + 1] == 0 and stone[i][k] == team and stone[i + 1][k - 1] == team and stone[i + 2][
                    k - 2] == 0):
                    weight = 40
                    sum = sum + weight

                # oox 2개 연속 막힘
                if (stone[i - 1][k + 1] == 0 and stone[i][k] == team and stone[i + 1][k - 1] == team and stone[i + 2][
                    k - 2] == enemy):
                    weight = 10
                    sum = sum + weight

                # xoo 2개 연속 막힘
                if (stone[i - 1][k + 1] == enemy and stone[i][k] == team and stone[i + 1][k - 1] == team and stone[i + 2][
                    k - 2] == 0):
                    weight = 10
                    sum = sum + weight


                # 반대 대각선 경우의수
                # ooooo 승리시
                if (stone[i - 2][k - 2] == team and stone[i - 1][k - 1] == team and stone[i][k] == team and stone[i + 1][
                    k + 1] == team and stone[i + 2][k + 2] == team):
                    weight = 100000
                    sum = sum + weight

                # oooo 4개 연속
                if (stone[i - 2][k - 2] == team and stone[i - 1][k - 1] == team and stone[i][k] == team and stone[i + 1][
                    k + 1] == team and stone[i + 2][k + 2] == 0):
                    weight = 500
                    sum = sum + weight

                # oooox 4개 연속 막힘
                if (stone[i - 2][k - 2] == team and stone[i - 1][k - 1] == team and stone[i][k] == team and stone[i + 1][
                    k + 1] == team and stone[i + 2][k + 2] == enemy):
                    weight = 400
                    sum = sum + weight

                # xoooo 4개 연속 막힘
                if (stone[i - 2][k - 2] == enemy and stone[i - 1][k - 1] == team and stone[i][k] == team and stone[i + 1][
                    k + 1] == team and stone[i + 2][k + 2] == team):
                    weight = 400
                    sum = sum + weight

                # ooo 3개 연속
                if (stone[i - 2][k - 2] == 0 and stone[i - 1][k - 1] == team and stone[i][k] == team and stone[i + 1][
                    k + 1] == team and stone[i + 2][k + 2] == 0):
                    weight = 70
                    sum = sum + weight

                # ooox 3개 연속 막힘
                if (stone[i - 2][k - 2] == 0 and stone[i - 1][k - 1] == team and stone[i][k] == team and stone[i + 1][
                    k + 1] == team and stone[i + 2][k + 2] == enemy):
                    weight = 50
                    sum = sum + weight

                # xooo 3개 연속 막힘
                if (stone[i - 2][k - 2] == enemy and stone[i - 1][k - 1] == team and stone[i][k] == team and stone[i + 1][
                    k + 1] == team and stone[i + 2][k + 2] == 0):
                    weight = 50
                    sum = sum + weight

                # oo 2개 연속
                if (stone[i - 1][k - 1] == 0 and stone[i][k] == team and stone[i + 1][k + 1] == team and stone[i + 2][
                    k + 2] == 0):
                    weight = 30
                    sum = sum + weight

                # oox 2개 연속 막힘
                if (stone[i - 1][k - 1] == 0 and stone[i][k] == team and stone[i + 1][k + 1] == team and stone[i + 2][
                    k + 2] == enemy):
                    weight = 10
                    sum = sum + weight

                # xoo 2개 연속 막힘
                if (stone[i - 1][k - 1] == enemy and stone[i][k] == team and stone[i + 1][k + 1] == team and stone[i + 2][
                    k + 2] == 0):
                    weight = 10
                    sum = sum + weight


                # 수비 경우의 수
                # oooxo 세로 수비시
                if (stone[i - 2][k] == enemy and stone[i - 1][k] == enemy and stone[i][k] == enemy and stone[i + 1][
                    k] == team and stone[i + 2][k] == enemy):
                    weight = 10000
                    sum = sum + weight

                # ooxoo 세로 수비시
                if (stone[i - 2][k] ==  enemy and stone[i - 1][k] ==  enemy and stone[i][k] ==  team and stone[i + 1][k] ==  enemy and
                      stone[i + 2][k] ==  enemy):
                    weight = 10000
                    sum = sum + weight

                # oxooo 세로 수비시
                if (stone[i - 2][k] ==  enemy and stone[i - 1][k] ==  team and stone[i][k] ==  enemy and stone[i + 1][k] ==  enemy and
                      stone[i + 2][k] ==  enemy):
                    weight = 10000
                    sum = sum + weight

                # oooxo 가로 수비시
                if (stone[i][k - 2] ==  enemy and stone[i][k - 1] ==  enemy and stone[i][k] ==  enemy and stone[i][k + 1] ==  team and
                      stone[i][k + 2] ==  enemy):
                    weight = 10000
                    sum = sum + weight

                # ooxoo 가로 수비시
                if (stone[i][k - 2] ==  enemy and stone[i][k - 1] ==  enemy and stone[i][k] ==  team and stone[i][k + 1] ==  enemy and
                      stone[i][k + 2] ==  enemy):
                    weight = 10000
                    sum = sum + weight

                # oxooo 가로 수비시
                if (stone[i][k - 2] ==  enemy and stone[i][k - 1] ==  team and stone[i][k] ==  enemy and stone[i][k + 1] ==  enemy and
                      stone[i][k + 2] ==  enemy):
                    weight = 10000
                    sum = sum + weight

                # oooxo 대각선 수비시
                if (stone[i - 2][k + 2] ==  enemy and stone[i - 1][k + 1] ==  enemy and stone[i][k] ==  enemy and stone[i + 1][
                    k - 1] ==  team and stone[i + 2][k - 2] ==  enemy):
                    weight = 10000
                    sum = sum + weight

                # ooxoo 대각선 수비시
                if (stone[i - 2][k + 2] ==  enemy and stone[i - 1][k + 1] ==  enemy and stone[i][k] ==  team and stone[i + 1][
                    k - 1] ==  enemy and stone[i + 2][k - 2] ==  enemy):
                    weight = 10000
                    sum = sum + weight

                # oxooo 대각선 수비시
                if (stone[i - 2][k + 2] ==  enemy and stone[i - 1][k + 1] ==  team and stone[i][k] ==  enemy and stone[i + 1][
                    k - 1] ==  enemy and stone[i + 2][k - 2] ==  enemy):
                    weight = 10000
                    sum = sum + weight

                # oooxo 반대 대각선 수비시
                if (stone[i - 2][k - 2] ==  enemy and stone[i - 1][k - 1] ==  enemy and stone[i][k] ==  enemy and stone[i + 1][
                    k + 1] ==  team and stone[i + 2][k + 2] ==  enemy):
                    weight = 10000
                    sum = sum + weight

                # ooxoo 반대 대각선 수비시
                if (stone[i - 2][k - 2] ==  enemy and stone[i - 1][k - 1] ==  enemy and stone[i][k] ==  team and stone[i + 1][
                    k + 1] ==  enemy and stone[i + 2][k + 2] ==  enemy):
                    weight = 10000
                    sum = sum + weight

                # oxooo 반대 대각선 수비시
                if (stone[i - 2][k - 2] ==  enemy and stone[i - 1][k - 1] ==  team and stone[i][k] ==  enemy and stone[i + 1][
                    k + 1] ==  enemy and stone[i + 2][k + 2] ==  enemy):
                    weight = 10000
                    sum = sum + weight

                # oooox 가로 수비시
                if (stone[i][k - 2] == enemy and stone[i][k - 1] == enemy and stone[i][k] == enemy and stone[i][k + 1] == enemy and
                      stone[i][k + 2] == team):
                    weight = 10000
                    sum = sum + weight

                # xoooo 가로 수비시
                if (stone[i][k - 2] == team and stone[i][k - 1] == enemy and stone[i][k] == enemy and stone[i][k + 1] == enemy and
                      stone[i][k + 2] == enemy):
                    weight = 10000
                    sum = sum + weight

                # oooox 세로 수비시
                if (stone[i - 2][k] == enemy and stone[i - 1][k] == enemy and stone[i][k] == enemy and stone[i + 1][k] == enemy and
                      stone[i + 2][k] == team):
                    weight = 10000
                    sum = sum + weight

                # xoooo 세로 수비시
                if (stone[i - 2][k] == team and stone[i - 1][k] == enemy and stone[i][k] == enemy and stone[i + 1][k] == enemy and
                      stone[i + 2][k] == enemy):
                    weight = 10000
                    sum = sum + weight

                # oooox 반대 대각선 수비시
                if (stone[i - 2][k - 2] == enemy and stone[i - 1][k - 1] == enemy and stone[i][k] == enemy and stone[i + 1][
                    k + 1] == enemy and stone[i + 2][k + 2] == team):
                    weight = 10000
                    sum = sum + weight

                # xoooo 반대 대각선 수비시
                if (stone[i - 2][k - 2] == team and stone[i - 1][k - 1] == enemy and stone[i][k] == enemy and stone[i + 1][
                    k + 1] == enemy and stone[i + 2][k + 2] == enemy):
                    weight = 10000
                    sum = sum + weight

                # oooox 대각선 수비시
                if (stone[i - 2][k + 2] == enemy and stone[i - 1][k + 1] == enemy and stone[i][k] == enemy and stone[i + 1][
                    k - 1] == enemy and stone[i + 2][k - 2] == team):
                    weight = 10000
                    sum = sum + weight

                # xoooo 대각선 수비시
                if (stone[i - 2][k + 2] == team and stone[i - 1][k + 1] == enemy and stone[i][k] == enemy and stone[i + 1][
                    k - 1] == enemy and stone[i + 2][k - 2] == enemy):
                    weight = 10000
                    sum = sum + weight

                # ooox 가로 수비시
                if (stone[i][k - 1] == enemy and stone[i][k] == enemy and stone[i][k + 1] == enemy and stone[i][k + 2] == team):
                    if (stone[i][k - 2] == team):
                        weight = 30   # 한쪽이 막혀있는데 수비 하려는 경우

                    else:
                        weight = 300
                    sum = sum + weight

                # xooo 가로 수비시
                if (stone[i][k - 2] == team and stone[i][k - 1] == enemy and stone[i][k] == enemy and stone[i][k + 1] == enemy):
                    if (stone[i][k + 2] == team):
                        weight = 30   # 한쪽이 막혀있는데 수비 하려는 경우

                    else:
                        weight = 2500

                    sum = sum + weight

                # ooox 세로 수비시
                if (stone[i - 1][k] == enemy and stone[i][k] == enemy and stone[i + 1][k] == enemy and stone[i + 2][k] == team):
                    if (stone[i - 2][k] == team):
                        weight = 30   # 한쪽이 막혀있는데 수비 하려는 경우

                    else:
                        weight = 2500

                    sum = sum + weight

                # xooo 세로 수비시
                if (stone[i - 2][k] == team and stone[i - 1][k] == enemy and stone[i][k] == enemy and stone[i + 1][k] == enemy):
                    if (stone[i + 2][k] == team):
                        weight = 30   # 한쪽이 막혀있는데 수비 하려는 경우

                    else:
                        weight = 2500

                    sum = sum + weight

                # ooox 대각선 수비시
                if (stone[i - 1][k + 1] == enemy and stone[i][k] == enemy and stone[i + 1][k - 1] == enemy and stone[i + 2][
                    k - 2] == team):
                    if (stone[i - 2][k + 2] == team):
                        weight = 30   # 한쪽이 막혀있는데 수비 하려는 경우

                    else:
                        weight = 2500

                    sum = sum + weight

                # xooo 대각선 수비시
                if (stone[i - 2][k + 2] == team and stone[i - 1][k + 1] == enemy and stone[i][k] == enemy and stone[i + 1][
                    k - 1] == enemy):
                    if (stone[i + 2][k - 2] == team):
                        weight = 30   # 한쪽이 막혀있는데 수비 하려는 경우

                    else:
                        weight = 2500

                    sum = sum + weight

                # ooox 반대 대각선 수비시
                if (stone[i - 1][k - 1] == enemy and stone[i][k] == enemy and stone[i + 1][k + 1] == enemy and stone[i + 2][
                    k + 2] == team):
                    if (stone[i - 2][k - 2] == team):
                        weight = 30   # 한쪽이 막혀있는데 수비 하려는 경우

                    else:
                        weight = 2500

                    sum = sum + weight

                # xooo 반대 대각선 수비시
                if (stone[i - 2][k - 2] == team and stone[i - 1][k - 1] == enemy and stone[i][k] == enemy and stone[i + 1][
                    k + 1] == enemy):
                    if (stone[i + 2][k + 2] == team):
                        weight = 30   # 한쪽이 막혀있는데 수비 하려는 경우

                    else:
                        weight = 2500

                    sum = sum + weight
        return sum

     def next(self, board,length):  # override
             print (" **** White player : My Turns **** ")

             stn = stone(self._color)
             temp = 0   # 수치화된 오목보드의 상태를 잠시 저장하는 변수
             AI = 0
             for i in range(0, 19):
                 for k in range(0, 19):
                     if (board[i][k] == 0 ):
                         board[i][k] = -1  # stone함수의 값이 0(돌이 없는 상태)일때 임의의 돌을 삽입
                         AI = self.ai_calculate(board)  # 그 결과 얼마나 유리한 수 인지 수치값으로 반환
                         if (temp <AI):  # temp에는 이전의 수치값 저장! , 이전의 수치값보다 좋은 수 일때
                             temp = AI
                             self.__max_x = i
                             self.__max_y=  k
                         board[i][k] = 0
             print("black:",AI)
             stn.setX(self.__max_x)
             stn.setY(self.__max_y)
             return stn

