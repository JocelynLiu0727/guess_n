import random
r = random.randint(1, 100)
count = 0 
while True:
	count += 1 # count = count + 1
	number = input('請輸入數字: ')
	number = int(number)
	if number == r:
		print ('你猜中了!')
		break
	elif number > r:
		print('猜錯囉! 比答案大!')
	else:
		print('猜錯囉! 比答案小!')
	print('這是你猜的第', count, '次')

