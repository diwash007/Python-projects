def is_boring(item,list1):
	item_list=[int(c) for c in str(item)]
	key =[]
	for i in range(len(item_list)):
		if item_list[i]%2==0 and (i+1)%2==0:
			key.append(1)
			item_list[i]="a"
		elif item_list[i]%2!=0 and (i+1)%2!=0:
			key.append(1)
			item_list[i]="a"
		else:
			item_list[i]="a"
			key.append(0)
	if 0 not in key:
		return True
	else:
		return False

n=int(input())
for i in range(n):
	x = list(map(int,input().split()))
	range_list = [item for item in range(x[0],x[1]+1)]
	boring=0
	for item in range_list:
		if is_boring(item,range_list):
			boring += 1
	print(f"Case #{str(i+1)}: {str(boring)}")