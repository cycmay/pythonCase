# !/usr/bin/python
# coding:utf-8
# author:bicycle

"""

选择排序的思想其实和冒泡排序有点类似，都是在一次排序后把最小的元素放到最前面。但是过程不同，
冒泡排序是通过相邻的比较和交换。而选择排序是通过对整体的选择。举个栗子，对5,3,8,6,4这个无
序序列进行简单选择排序，首先要选择5以外的最小数来和5交换，也就是选择3和5交换，一次排序后就
变成了3,5,8,6,4.对剩下的序列一次进行选择和交换，最终就会得到一个有序序列。其实选择排序可
以看成冒泡排序的优化，因为其目的相同，只是选择排序只有在确定了最小数的前提下才进行交换，大
大减少了交换的次数。选择排序的时间复杂度为O(n^2)

"""
import numpy

def selection_sort(array:list):
	result = array.copy()
	lenth = len(array)
	for i in range(lenth):
		least = i
		for k in range(i+1, lenth):
			if result[least] > result[k]:
				least = k
		result[least],result[i] = result[i], result[least]

	return result

def main():
	array = numpy.random.randint(10000, size=10000)
	print(array)
	print(selection_sort(array))
	
if __name__ == '__main__':
	main()
