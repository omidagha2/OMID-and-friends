def main():
    a, b = input().split()
    fpoint = (a.count(".") + b.count(".")) + (a.count(".") + b.count("."))
    a, b = int(a.replace(".", "")), int(b.replace(".", ""))
    prod = str(div_by_ten(mult(a, b), fpoint))
    print(prod[:-2] if fpoint == 4 else prod)
    
def div_by_ten(num, n):
    if n== 0:
        return num
    return float(str(num)[:-n] + "." + str(num)[-n:])

def mult(a, b):
    if (a == 0 or b == 0):
        return 0
    c = 0
    if (a < b):
        a, b = b, a
    c = a
    for i in range(1, b):
        a += c
    return a

main()
