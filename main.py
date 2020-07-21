a = "Hello Worid"

print(len(a))

print(a[5:11])

print(a[5:len(a)])

print(a[5:])

print(a[1:11:2])

# 練習數字與字串的方法
# 0721

int = 666
print (str(int))

# *可以複製字串
print ("It's was so " + "C" + "o"*7 + "l")



# Python字符串比較，包含和串聯
A = "The cat is brown"
q = "cat"
 
if q in A:
    print ( q + " found in " + A )

# Python字符串格式化
print ("我叫 %s 今年 %d 歲!" % ('小雞', 18))

# %c	 格式化字符及其ASCII码
# %s	 格式化字符串
# %d	 格式化整数
# %u	 格式化无符号整型
# %o	 格式化无符号八进制数
# %x	 格式化无符号十六进制数
# %X	 格式化无符号十六进制数（大写）
# %f	 格式化浮点数字，可指定小数点后的精度
# %e	 用科学计数法格式化浮点数
# %E	 作用同%e，用科学计数法格式化浮点数
# %g	 %f和%e的简写
# %G	 %f 和 %E 的简写
# %p	 用十六进制数格式化变量的地址


# 字面量格式化字符串
x = 1
print ( f'{x+1=}' ) 
# 'x+1=2'


# 以 {:,} 的方式以逗號分隔數字
print ('{:,}' . format (10000000))




