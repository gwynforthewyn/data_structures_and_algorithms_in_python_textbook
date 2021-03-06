# c.4-10
# What is the integer part of a logarithm? If you have:
# log(n) = x.y, then integer_part = floor(x.y) = x


# c-4.12
def _compute_product(m, n):
    """
    >>> _compute_product(3, 5)
    15
    """

    if (m == 1):
        return n
    else:
        return n + _compute_product(m - 1, n)


# c-4.14
# top disk      source         spare       destination
#   1           1               0               0
#   2           2               1               0
#   3           3               1               2
#   3           3               0               1
#   4           4               3               1
#   4           4               1               0
#   5           5               4               0
#
# For two disks
# Step 1 : Shift first disk from 'A' to 'B'.
# Step 2 : Shift second disk from 'A' to 'C'.
# Step 3 : Shift first disk from 'B' to 'C'.
#
# The pattern here is :
# Shift 'n-1' disks from 'A' to 'B'.
# Shift last disk from 'A' to 'C'.
# Shift 'n-1' disks from 'B' to 'C'.
#
def moveHanoiTower(disk_number, _from="origin", spare="spare", destination="destination", note="initial"):
    """
    >>> moveHanoiTower(1, _from = "origin", spare = "spare", destination = "destination", note = "initial")
    initial: Move disk 1 from origin to destination


    >>> moveHanoiTower(2, _from = "origin", spare = "spare", destination = "destination", note = "initial")
    put_on_spare: Move disk 1 from origin to spare
    after_first_recursion: Move disk 2 from source origin to destination
    move_spare_to_dest: Move disk 1 from spare to destination


    >>> moveHanoiTower(3, _from = "origin", spare = "spare", destination = "destination", note = "initial")
    put_on_spare: Move disk 1 from origin to destination
    after_first_recursion: Move disk 2 from source origin to spare
    move_spare_to_dest: Move disk 1 from destination to spare
    after_first_recursion: Move disk 3 from source origin to destination
    put_on_spare: Move disk 1 from spare to origin
    after_first_recursion: Move disk 2 from source spare to destination
    move_spare_to_dest: Move disk 1 from origin to destination
    """
    SMALLEST = 1
    if disk_number == SMALLEST:
        print(f"{note}: Move disk {disk_number} from {_from} to {destination}")
        return

    next_disk = disk_number - 1

    moveHanoiTower(next_disk, _from=_from, destination=spare, spare=destination, note="put_on_spare")

    note = "after_first_recursion"
    print(f"{note}: Move disk {disk_number} from source {_from} to {destination}")
    moveHanoiTower(next_disk, _from=spare, spare=_from, destination=destination, note="move_spare_to_dest")

# c.4-15
def powerset(set: list):
    """
    >>> powerset([])

    >>> powerset(["a"])
    ['a']

    >>> powerset(["a", "b"])
    ['a', 'b']
    ['b']
    ['a']
    """

    # smallest possible set!
    if len(set) == 0:
        return

    print(set)

    for i in set:
        smoller_set = [m for m in set if m != i]

        powerset(smoller_set)

# 4_16
def reverseString(a: str) -> str:
    """
    >>> reverseString("foo")
    oof

    >> reverseString("roflcopter")
    retpoclfor
    """
    if not a:
        return

    print(a[-1], end="")
    reverseString(a[:-1])


# 4_18
def vowelsAndConsonantCount(candidate: str):
    """
    >>> vowelsAndConsonantCount("")
    (0, 0)

    >>> vowelsAndConsonantCount("d")
    (1, 0)

    >>> vowelsAndConsonantCount("a")
    (0, 1)

    >>> vowelsAndConsonantCount("aazvogel")
    (4, 4)
    """

    def _counter(cand: str):

        if not cand:
            return 0

        if cand[0] in "aeiouAEIOU":
            return 1 + _counter(cand[1:])

        return 0 + _counter(cand[1:])

    vowels_count = _counter(candidate)

    return (len(candidate)-vowels_count, vowels_count)