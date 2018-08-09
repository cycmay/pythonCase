# !/usr/bin/python
# coding:utf-8
# author:bicycle

"""

插入排序不是通过交换位置而是通过比较找到合适的位置插入元素来达到排序的目的的。
相信大家都有过打扑克牌的经历，特别是牌数较大的。在分牌时可能要整理自己的牌，
牌多的时候怎么整理呢？就是拿到一张牌，找到一个合适的位置插入。这个原理其实
和插入排序是一样的。举个栗子，对5,3,8,6,4这个无序序列进行简单插入排序，
首先假设第一个数的位置时正确的，想一下在拿到第一张牌的时候，没必要整理。
然后3要插到5前面，把5后移一位，变成3,5,8,6,4.想一下整理牌的时候应该也是
这样吧。然后8不用动，6插在8前面，8后移一位，4插在5前面，从5开始都向后移一位
。注意在插入一个数的时候要保证这个数前面的数已经有序。简单插入排序的时间复杂度
也是O(n^2)。

"""
import numpy

def insertion_sort(array:list):
	result = array.copy()
	lenth = len(array)
	 # 假设第一个数不用排序
	for i in range(1, lenth):
		while i > 0 and result[i] < result[i-1]:
			result[i-1],result[i] = result[i],result[i-1] 
			i -= 1

	return result

def main():
	array = numpy.random.randint(10000, size=10000)
	print(array)
	print(insertion_sort(array))
	
if __name__ == '__main__':
	main()
