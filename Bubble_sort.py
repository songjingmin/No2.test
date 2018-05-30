import random  
# 定义冒泡排序函数  
def bubble_sort(data):  
    for i in range(len(data) - 1):# 外循环每一次使得有序的数增加一个  
        indicator = False # 用于优化（没有交换时表示已经有序，结束循环）  
        for j in range(len(data) - 1 - i):#内循环每次将无序部分中的最大值放到最上面  
            if data[j] > data[j + 1]:  
                data[j], data[j+1] = data[j+1], data[j]  
                indicator = True  
        if not indicator:#如果没有交换说明列表已经有序，结束循环  
            break  
# 验证算法正确性  
data = list(range(10))#产生一个有序列表  
random.shuffle(data) # 调用shuffle函数打乱顺序  
print(data)# 排序前  
bubble_sort(data)# 调用冒泡排序算法  
print(data)#排序后  