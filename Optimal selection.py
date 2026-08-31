def fractional_knapsack(vals, wts, cap):
    data = []

    for idx in range(len(vals)):
        p = vals[idx]
        w = wts[idx]
        r = p / w
        data.append([p, w, r])

    # sort by value first
    data.sort(key=lambda x: x[2], reverse=True)

    res = 0.0
    rem = cap
    pick = []

    for row in data:
        if rem <= 0:
            break

        p = row[0]
        w = row[1]

        if w <= rem:
            res += p
            rem -= w
            pick.append((p, w, 1.0))
        else:
            tmp = rem / w
            res += p * tmp
            pick.append((p, w, tmp))
            rem = 0

    return res, pick


vals = [60, 100, 120]
wts = [10, 20, 30]
cap = 50

res, pick = fractional_knapsack(vals, wts, cap)

print(f"Maximum profit: {res}")

for p, w, frac in pick:
    print(f" profit={p:<3} weight={w:<3} fraction taken={frac:.2f}")