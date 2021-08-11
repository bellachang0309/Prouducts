
#讀取檔案
prouducts=[]
with open('prouducts.csv','r')as f:
	for line in f:
		if '商品,價格' in line:
			continue
		name,price=line.strip().split(',')
		prouducts.append([name,price])
print(prouducts)

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
