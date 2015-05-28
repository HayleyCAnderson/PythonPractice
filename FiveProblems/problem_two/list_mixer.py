class ListMixer(object):
    def combine(self, list_one, list_two):
        combined_list = []

        return self.combine_lists(list_one, list_two, combined_list)

    def combine_lists(self, list_one, list_two, combined_list):
        if len(list_one) > 0 or len(list_two) > 0:
            combined_list = self.combine_list_one(list_one, combined_list)
            combined_list = self.combine_list_two(list_two, combined_list)

            return self.combine_lists(list_one, list_two, combined_list)
        else:
            return combined_list

    def combine_list_one(self, list_one, combined_list):
        if len(list_one) > 0:
            combined_list.append(list_one.pop(0))

            return combined_list
        else:
            return combined_list

    def combine_list_two(self, list_two, combined_list):
        if len(list_two) > 0:
            combined_list.append(list_two.pop(0))

            return combined_list
        else:
            return combined_list
