def print_pairs(items):
    for i in items:
        for j in items:
            print(i, j)

print_pairs([1, 2, 3])
# Two nested loops over n items: O(n^2)
