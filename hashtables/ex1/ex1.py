def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    hash = {}
    lis = [None]
    if len(weights) >= 2:
        for x in weights:
            for y in weights:
                hash.update({(x,y):x+y})
        for x in hash:        
            if hash[x] is limit:
                lis = [x[0],x[1]]
                if lis[0] < lis[1]:
                    lis[0],lis[1] = lis[1],lis[0]
        for x in range(length):
            if lis[0] is weights[x]:
                lis[0] = x
            if lis[1] is weights[x]:
                lis[1] = x
        return lis
    

    return None

    
weights = [12, 6, 7, 14, 19, 3, 0, 25, 40]

print(get_indices_of_item_weights(weights,9,7))
