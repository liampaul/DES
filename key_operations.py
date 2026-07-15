def PC1 (K: int) -> int:
    
    # 64 bit -> 56 bit key

    PC1table =   [57, 49, 41, 33, 25, 17,  9,
                 1, 58, 50, 42, 34, 26, 18,
                10,  2, 59, 51, 43, 35, 27,
                19, 11,  3, 60, 52, 44, 36,
                63, 55, 47, 39, 31, 23, 15,
                 7, 62, 54, 46, 38, 30, 22,
                14,  6, 61, 53, 45, 37, 29,
                21, 13,  5, 28, 20, 12,  4]
    n = 0
    for i, pos in enumerate(PC1table):

        # 64 - 57,49,41, ...
        # accounts for reverse ordering and 0 index
        original_bit_index = 64 - pos

        # Shifts K forward (original_bit_index) and checks the least signinficant digit (rightmost).
        # rightmost bit becomes the intened bit
        bit_value = (K >> original_bit_index) & 1

        # inserts the bit into the appropriate slot
        if bit_value:
            n |= (1 << (55 - i))
    return n

def PC2 (K: int) -> int:
    PC2table = [
    14, 17, 11, 24,  1,  5,
     3, 28, 15,  6, 21, 10,
    23, 19, 12,  4, 26,  8,
    16,  7, 27, 20, 13,  2,
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53,
    46, 42, 50, 36, 29, 32]
    
    n = 0
    for i, pos in enumerate(PC2table):
        original_bit_index = 56 - pos
        bit_value = (K >> original_bit_index) & 1

        # inserts the bit into the appropriate slot
        if bit_value:
            n |= (1 << (47 - i))
    return n





def split (K: int) -> tuple:
    c0 = (K >> 28) & 0x0FFFFFFF
    d0 = K & 0x0FFFFFFF
    return (c0, d0)

def shift (K: int, n: int) -> int:
    return ((K << n) | (K >> (28 - n))) & 0x0FFFFFFF


