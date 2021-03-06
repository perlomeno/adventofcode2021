def new_lf(f):
    if f != 0:
        return f - 1
    else:
        return 6

# part 1
with open("input", "r") as lf_file:
    lf = [int(i) for i in lf_file.readline().split(",")]

for d in range(80):
    nf = lf.count(0)
    lf = list(map(new_lf, lf))
    for i in range(nf):
        lf.append(8)

print(len(lf))

# part 2
with open("input", "r") as lf_file:
    lf = [int(i) for i in lf_file.readline().split(",")]

f = [lf.count(i) for i in range(9)]

for d in range(256):
    nf = f.pop(0)
    f[6] += nf
    f.append(nf)

print(sum(f))
