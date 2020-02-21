# -*- coding:utf-8 -*-
#随机生成密码16位

import random,string

def sjmm():
	mima = [] 
	sz = '123456789'
	xzm = 'abcdefghijklmnopqrstuvwxyz'
	dzm = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	tzf = '~!#@$%^&*?'
	all = sz + xzm + dzm + tzf
	m1 = random.choice(sz)

	m2 = random.choice(xzm)
	m3 = random.choice(dzm)
	m4 = random.choice(tzf)
	m5 = "".join(random.sample(all,12))
	mima.append(m1)
	mima.append(m2)
	mima.append(m3)
	mima.append(m4)
	mima.append(m5)
	random.shuffle(mima)
	a = "".join(mima)
	return a

if __name__ == '__main__':
	#id = int(input("请输入密码个数："))
	for i in range(1,2):
		aa = sjmm()
		print(aa)
		with open("随机密码.txt","a")as file:
			file.write("密码"+str(i)+"："+ aa +"\n")
			file.close()