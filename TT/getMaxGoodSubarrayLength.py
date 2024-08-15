from typing import List

def getMaxGoodSubarrayLength(financialMetrics: List[int], limit: int) -> int:
    maxLength = 0
    length = 0
    for i in range(financialMetrics):
        if financialMetrics[i] * (i + 1) > limit:
            length += 1
        else:
            if maxLength < length:
                maxLength = length
            length = 0

    if maxLength < length:
        maxLength = length
    
    return maxLength

if __name__ == '__main__':
    print(getMaxGoodSubarrayLength([1, 3, 4, 3, 1], 6))
    print(getMaxGoodSubarrayLength([1, 3, 4, 3, 1, 2, 1], 6))
    print(getMaxGoodSubarrayLength([1, 3, 4, 3, 1, 2, 3, 4, 4, 3], 6))