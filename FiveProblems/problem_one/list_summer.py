class ListSummer(object):
    def sum_with_for(self, list_to_sum):
        list_sum = 0

        for i in list_to_sum:
            list_sum += i

        return list_sum

    def sum_with_while(self, list_to_sum):
        list_sum = 0
        i = 0

        while i < len(list_to_sum):
            list_sum += list_to_sum[i]
            i += 1

        return list_sum

    def sum_with_recursion(self, list_to_sum):
        list_sum = 0

        return self.sum_list(list_sum, list_to_sum)

    def sum_list(self, list_sum, list_to_sum):
        if len(list_to_sum) > 0:
            list_sum += list_to_sum.pop()
            return self.sum_list(list_sum, list_to_sum)
        else:
            return list_sum
