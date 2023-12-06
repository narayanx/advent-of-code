from math import prod

times = [41, 66, 72, 66]
dists = [244, 1047, 1228, 1040]
time = 41667266
dist = 244104712281040


def part_1(times, dists):
    res = 1
    for t, d in zip(times, dists):
        running_valid = 0
        for i in range(1, t):
            if i * (t - i) > d:
                running_valid += 1
        res *= running_valid
    return res


def part_1_oneline(times, dists):
    return prod(
        sum(1 for i in range(1, time) if i * (time - i) > dist)
        for time, dist in zip(times, dists)
    )


def part_2(time, dist):
    min_wt = max_wt = 0
    for i in range(1, time):
        if i * (time - i) > dist:
            min_wt = i
            break

    for i in range(time, 0, -1):
        if i * (time - i) > dist:
            max_wt = i
            break

    return max_wt - min_wt + 1


print(f"{part_1(times, dists)= }")
# oneliner for part 1
print(f"{part_1_oneline(times, dists)= }")
# original part 2 solution
print(f"{part_2(time, dist)= }")
# part 1 solution passes part 2
print(f"{part_1([time], [dist])= }")
