import random
start = input('請決定隨機數字範圍開始值: ')
end = input('請決定隨機數字範圍結束值: ')
start = int(start)
end = int(end)
r = random.randint(start, end)
count = 0 
while True:
	count += 1 # count = count + 1
	number = input ('請輸入數字: ')
	number = int(number)
	if number == r:
		print ('你猜中了!')
		break
	elif number > r:
		print('猜錯囉! 比答案大!')
	else:
		print('猜錯囉! 比答案小!')
	print('這是你猜的第', count, '次')

