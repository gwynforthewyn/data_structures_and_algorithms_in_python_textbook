# Write a short Python function that takes a
# sequence of integer values and determines if
# there is a distinct pair of numbers in the
# sequence whose product is odd.
def distinct_pairs_generate_odd_number(seq_o_numbers):
    dat_cache = []

    for i in seq_o_numbers:
        if (i % 2 == 1):
            dat_cache.append(i)

    return len(dat_cache) > 1


# Write a Python function that takes a sequence of
# numbers and determines if all the numbers are
# different from each other (that is, they are distinct).
def are_seq_members_distinct(seq):
    return len(seq) == len(set(seq))

def genify(k):
    if k == 0:
      return k
    else:
      return pow(k, 2)

    return [ genify(i) for i in range(0, 10) ]

