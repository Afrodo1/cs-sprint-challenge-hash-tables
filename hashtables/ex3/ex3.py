def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    # hash = []
    # temp = []
    # results = []
    # count = 0
    # for x in arrays:
    #     for y in x:
    #         hash.append((count,y))
    #     count+=1

    # for x in hash:
    #     for y in hash:
    #         if x[0] == y[0]:
    #             pass
    #         elif x[1] == y[1]:
    #             temp.append(x[1])
    
    # for x in temp:
    #     if x not in results:
    #         results.append(x)

    #Above takes too long with larger inputs.

    counts = {}

    for a in arrays:
        for num in a:
            if num not in counts:
                counts[num] = 0
            counts[num] += 1

    result = []

    for i,x in counts.items():
        if x == len(arrays):
            result.append(i)

    return result

if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000, 2000)) + [1, 2, 3])
    arrays.append(list(range(2000, 3000)) + [1, 2, 3])
    arrays.append(list(range(3000, 4000)) + [1, 2, 3])
    arrays.append(list(range(4000, 5000)) + [1, 2, 3])
    arrays.append(list(range(5000, 6000)) + [1, 2, 3])
    arrays.append(list(range(6000, 7000)) + [1, 2, 3])
    arrays.append(list(range(7000, 8000)) + [1, 2, 3])

    print(intersection(arrays))

