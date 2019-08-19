from enum import Enum, unique


# @unique   #保证没有重复值

# 这是个映射关系？？
class VIP(Enum):
    YELLOW = 1
    GREEN = 2
    RED = 3
    BLACK = 4
    BLUE = 1


class VIP1(Enum):
    YELLOW = 1
    GREEN = 2
    RED = 3
    BLACK = 4
    BLUE = 1


# print(VIP.GREEN)
# print(VIP['BLACK'].value)
# print(VIP(3))
#
# for name,member in VIP.__members__.items():
#     print(name,'=>',member)
# print('\n')
# for data in VIP:
#     print(data.name,'==>',data)

ans = VIP1.BLUE.value == VIP.BLUE.value
print(ans)
a = 1
print(VIP(a))
