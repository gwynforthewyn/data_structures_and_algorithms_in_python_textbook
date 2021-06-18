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
