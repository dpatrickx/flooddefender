lines = open('table').read().split('\n')

normal = 0
attack = 0
s = 0
num = 0
for line in lines:
	if len(line) == 0:
		continue
	nums = line.split(' ')
	assert len(nums) == 7
	normal += int(nums[0])
	normal += int(nums[1])
	normal += int(nums[2])
	normal += int(nums[3])
	attack += int(nums[4])
	attack += int(nums[5])
	s += int(nums[6])
	num += 1
print round(float(normal)/num, 2), round(float(attack)/num, 2), round(float(s)/num, 2), num
num *= 2000
print round(float(normal)/num, 2), round(float(attack)/num, 2), round(float(s)/num, 2)
