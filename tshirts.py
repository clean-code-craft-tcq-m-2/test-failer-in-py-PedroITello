
def size(cms):
    if cms < 38:
        return 'S'
    elif cms >= 38 and cms < 42: # Add >= here to decide 38 be M size
        return 'M'
    else:
        return 'L'


# assert(size(37) == 'S')
# assert(size(40) == 'M')
# assert(size(43) == 'L')
# 38 is out of his input because it maybe needs to clasify as S or M
# inside if condition but currently its L in any case
# This loop are created to include 38 inside M size using >= evaluation
for x in range(100):
    print(x)
    if x < 38:
        assert(size(x) == 'S')
    elif x >= 38 and x < 42:
        assert(size(x) == 'M')
    else:
        assert(size(x) == 'L')

print("All is well (maybe!)\n")
