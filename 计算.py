
# numb01 = int(input(f"电机功率"))
numb02 = int(input(f"电压"))
numb03 = int(input(f"AH"))
numb04 = int(input(f"续航"))
numb05 = numb02 * numb03
numb06 = (numb05 / numb04)/1000
numb07 = 11.6
numb08 = numb06 * 1.5 *30
print(numb08)
numb09 = 1
numb12 = int(input(f"价格"))
numb10 = numb08 + numb12
numb11 = numb07

for i in range(1000):
    if numb10 > numb11:
        numb10 += numb08
        numb11 += numb07
        numb09 += 1
print(numb09/24)
