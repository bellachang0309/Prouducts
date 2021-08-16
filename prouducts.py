import os #operating system

def read_file(filename):
	prouducts=[]
	with open(filename,'r')as f:
		for line in f:
			if '商品,價格' in line:
				continue #繼續
			name,price=line.strip().split(',')
			prouducts.append([name,price])
	return prouducts

#讓使用者輸入
def user_input(prouducts):
	while True:
		name=input('請輸入商品名稱：')
		if name=='q':
			break
		price=input('請輸入商品價格：')
		prouducts.append([name,price])
	print(prouducts)
	return prouducts

#印出所有購買紀錄
def print_products(prouducts):
	for a in prouducts:
		print(a[0],'的價格是',a[1])

#寫入檔案
def write_file(filename,prouducts):
	with open(filename,'w')as f:
		f.write('商品,價格\n')
		for p in prouducts:
			f.write(p[0]+','+str(p[1])+'\n')


def main():
	filename = 'prouducts.csv'
	if os.path.isfile(filename): 
		print('耶！你找到檔案了！')
		prouducts = read_file(filename)
	else:
		print('找不到檔案......')
	
	prouducts = user_input(prouducts)
	print_products(prouducts)
	write_file('prouducts.csv',prouducts)

main()