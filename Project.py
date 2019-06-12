# -*- coding: utf-8 -*-

import math
import matplotlib.pyplot as plt
import numpy as np
from vpython import *


'''
2019년 1학기 정보 프로젝트 수행평가
2417 오혁재
2418 원준하

주제 : 컴프턴 산란
MVP: 45도 산란
'''



print("컴프턴 산란")


#######컴프턴 산란 수식 구현#######


#사용하는 상수
m = 9.10938356 * (10**-31)   #전자의 질량
c = 299792458                #빛의 속도
h = 6.62607004 * (10**-34)   #플랑크 상수



#산란각 및 입사광의 파장입력
inci = float(input("입사광의 파장 :"))
theta = float(input("산란각 :"))

theta=math.pi*(theta/180)

#수식
#scat - inci = (h/(m*c))*(1-math.cos(theta))

print(math.cos(theta))
scat = inci + (h/(m*c))*(1-math.cos(theta)) #산란광 파장 계산


print('산란파 파장:'+ str(scat)) #산란파 파장 출력


#######컴프턴 산란 그래픽 구현#######

