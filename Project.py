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
plt.rc('font', family = 'Malgun Gothic')
x=np.linspace(-10,10,100)
y1=np.sin(x/(inci*10**11)) #입사광 그래프 구현
y2=np.sin(x/(scat*10**11)) #산란파 그래프 구현
plt.plot(x,y1,label='입사광')
plt.plot(x,y2,label='산란파')
plt.show()


vp_inci = sphere(pos = vec(0,0,0), make_trail=True, radius=0.2, color=color.red)
vp_radi = sphere(pos = vec(5,0,0), make_trail=True, radius=0.2)
vp_inci.velocity = vec(1,0,0)
vp_radi.velocity = vec(0,0,0)

dt = 0.01
while True:
    rate(100)
    vp_inci.pos = vp_inci.pos + vp_inci.velocity * dt
    vp_radi.pos = vp_radi.pos + vp_radi.velocity * dt
    if vp_inci.pos.x>=5:
        vp_inci.velocity = vec(math.cos(theta),math.sin(theta),0)
        #vp_radi.velocity = vec()
