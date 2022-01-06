# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 10:32:04 2021

@author: graciellafavoreto
"""

#pega valores de posicao e projecao das cam 1 e 2 do usuario
def position():
    #print('Entre com os valores:')
    x = float(input('x: '))
    y = float(input('y: '))
    z = float(input('z: '))
    return x, y, z

#calcula e retorna coefs linear e angular
def coefs(ic, ip, jc, jp):
    m = (jp-jc)/(ip-ic) #coeficiente angular
    b = -1*(m*ic-jc) #coeficiente linear
    return m, b
    
print('Entre com os valores da camera 1: ')
print('Posicao da camera 1: ')
xc1, yc1, zc1 = position()
print('Projecao da camera 1: ')
xp1, yp1, zp1 = position()

print('Entre com os valores da camera 2: ')
print('Posicao da camera 2: ')
xc2, yc2, zc2 = position()
print('Projecao da camera 2: ')
xp2, yp2, zp2 = position()

#XY reta 1
mr1, br1 = coefs(xc1, xp1, yc1, yp1)
print('m XY da reta 1:', mr1)
print('b XY da reta 1:', br1)
#XY reta 2
mr2, br2 = coefs(xc2, xp2, yc2, yp2)
print('m XY da reta 2:', mr2)
print('b XY da reta 2:', br2)

xr_XY = (-(mr2*xc2)+yc2+(mr1*xc1)-yc1)/(mr1-mr2)
yr_XY = (mr1*xr_XY)-(mr1*xc1)+yc1
print(xr_XY, yr_XY)

#XZ reta 1
mr1, br1 = coefs(xc1, xp1, zc1, zp1)
print('m XZ da reta 1:', mr1)
print('b XZ da reta 1:', br1)
#XZ reta 2
mr2, br2 = coefs(xc2, xp2, zc2, zp2)
print('m XZ da reta 2:', mr2)
print('b XZ da reta 2:', br2)

xr_XZ = (-(mr2*xc2)+zc2+(mr1*xc1)-zc1)/(mr1-mr2)
yr_XZ = (mr1*xr_XZ)-(mr1*xc1)+zc1
print(xr_XZ, yr_XZ)

#ZY reta 1
mr1, br1 = coefs(zc1, zp1, yc1, yp1)
print('m ZY da reta 1:', mr1)
print('b ZY da reta 1:', br1)
#ZY reta 2
mr2, br2 = coefs(zc2, zp2, yc2, yp2)
print('m ZY da reta 2:', mr2)
print('b ZY da reta 2:', br2)

xr_ZY = (-(mr2*zc2)+yc2+(mr1*zc1)-yc1)/(mr1-mr2)
yr_ZY = (mr1*xr_ZY)-(mr1*zc1)+yc1
print(xr_ZY, yr_ZY)

print('Os valores de cruzamento são:')
result_x = (xr_XY+xr_XZ)/2
result_y = (yr_XY+yr_ZY)/2
result_z = (yr_XZ+xr_ZY)/2
print('x: ', result_x)
print('y: ', result_y)
print('z: ', result_z)