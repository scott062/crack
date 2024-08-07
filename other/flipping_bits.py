def flipping_bits(n):
    org_bits = list(bin(n).lstrip('0b'))
    remaining = 32 - len(org_bits)
    new = [0 for x in range(remaining)] + org_bits
    new_again = ['0' if int(x) else '1' for x in new]
    print(new_again)
    return int("".join(new_again), 2)
print(flipping_bits(9))
