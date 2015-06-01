# Doesn't work. 'Solution' by the person who wrote the problem doesn't work
# either. At least I learned about list and dictionary comprehensions.

class NumberMaker(object):
    def biggest_number(self, integer_list):
        sorted_list = sorted([str(integer) for integer in integer_list])
        first_chars = [string[0] for string in sorted_list]

        dup_indices = list(reversed([list(reversed([index
            for index, char in enumerate(first_chars)
                if char == c]))
                    for c in set(first_chars)
                        if first_chars.count(c) > 1]))

        if len(dup_indices) > 0:
            dup_lists = [[sorted_list.pop(int(i)) for i in arr] for arr in dup_indices]
            dup_lists = list(reversed([list(reversed(arr)) for arr in dup_lists]))

            for i, arr in enumerate(dup_lists):
                sorted_list.insert(int(dup_indices[i][0]), arr)

        sorted_list = list(reversed(sorted_list))
        sorted_flat_list = [item for inner_list in sorted_list for item in inner_list]

        return int(''.join(sorted_flat_list))
