from time import perf_counter as pfc

day = ""
test = 1
if test:
    t = "test_"
else:
    t = ""
#
i = [
    l.split(" ")
    for l in open("./puzzle_inputs/" + t + "day" + day + ".txt", "r")
    .read()
    .strip()
    .splitlines()
]
print(i)


def p1():
    return


#
def p2():
    return


# Part 1:
start1 = pfc()
print(f"Part 1 result is: {p1()}, t = {pfc() - start1}")

# Part 2:
start2 = pfc()
print(f"Part 2 result is: {p2()}, t = {pfc() - start2}")
