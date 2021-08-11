import os #operating system

#讀取檔案
prouducts=[]
if os.path.isfile('prouducts.csv'):  #檢查檔案在不在
	print('耶！你找到檔案了！')
	with open('prouducts.csv','r')as f:
	for line in f:
		if '商品,價格' in line:
			continue #繼續
		name,price=line.strip().split(',')
		prouducts.append([name,price])
print(prouducts)
else:
	print('找不到檔案......')



#讓使用者輸入
while True:
	name=input('請輸入商品名稱：')
	if name=='q':
		break
	price=input('請輸入商品價格：')
	prouducts.append([name,price])
print(prouducts)

#印出所有購買紀錄
for a in prouducts:
	print(a[0],'的價格是',a[1])

#寫入檔案
with open('prouducts.csv','w')as f:
	f.write('商品,價格\n')
	for p in prouducts:
		f.write(p[0]+','+p[1]+'\n')
