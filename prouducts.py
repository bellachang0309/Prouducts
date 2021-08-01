prouducts=[]
while True:
	name=input('請輸入商品名稱：')
	if name=='q':
		break
	price=input('請輸入商品價格：')
	prouducts.append([name,price])
print(prouducts)

for a in prouducts:
	print(a[0],'的價格是',a[1])

with open('prouducts.csv','w')as f:
	f.write('商品,價格\n')
	for p in prouducts:
		f.write(p[0]+','+p[1]+'\n')
