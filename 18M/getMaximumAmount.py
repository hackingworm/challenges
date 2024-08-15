import heapq

def getMaximumAmount(quantity: list[int], m: int) -> int:
    for i in range(len(quantity)):
        quantity[i] = -quantity[i]

    heapq.heapify(quantity)

    revenue = 0

    for _ in range(m):
        max_value = -heapq.heappop(quantity)
        revenue += max_value
        heapq.heappush(quantity, -(max_value - 1))

    return revenue

'''
def getMaximumAmount(quantity: list[int], m: int) -> int:
    quantity.sort(reverse = True)

    count = 0
    amount = 0
    for i in range(len(quantity)):
        if m == count:
            break

        while len(quantity) - 1 == i or quantity[i] > quantity[i + 1]:
            gap = quantity[i] - quantity[i - 1]
            if m == count:
                break

            for k in range(i + 1):
                if m == count:
                    break

                amount += quantity[k]
                quantity[k] -= 1
                count += 1

    return amount
'''

if __name__ == '__main__':
    print(getMaximumAmount([1, 2, 4], 4))