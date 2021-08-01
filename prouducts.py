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