# import random as r
# from turtle import goto

# greeting = "hello world"
# print(greeting.upper())
# print(len(greeting))
# print(greeting[1])
# print(greeting.find("wo", 4))


# print(r.random())

# def cash_withdrawal(amount,accnum):
#     print(f"withdrawing {amount} from account {accnum}")

# cash_withdrawal(120,4584761)

# x=[1,2]
# print(x)
# y={1:"egg",3:"bob"}
# print(y[3])

# print(float(54))
# print(float("54"))

# print(str(54))
# print(str(54.0))


# l = [1,2,3]
# s=[x*2 for x in l]
# print(s)

# # light = False

# def light_switch():
    
#     if light:
#         print("Bright innit")
#         light = False
#     else:
#         print("Put big light on")
#         light = True

# # light_switch()
# # light_switch()

# num = [1,2,3]

# def show_num():
#     # global num
#     if 1 in num:
#         num.reverse()
#         print(num)
    
# show_num()

# even_nums = [2,4,6,8,10]
# odd_nums = [1,3,5,7]

# x = zip(even_nums,odd_nums)
# x = [a+b for (a,b) in x]

# print(x)

# a = [[1,2],[3,4]]
# print(a[0][1])

# b=[1,2,3,4,5]

# c=b[::2]
# print(c)


l1 = [1,2,3]
l2 = [3,2,1]
l2.reverse()
if l1 == l2:
    print("ye")

print(l1[0:-1])

