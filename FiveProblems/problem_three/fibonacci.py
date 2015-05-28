class Fibonacci(object):
    def __init__(self, length):
        self.length = length

    def return_numbers(self):
        sequence = []

        return self.calculate_numbers(sequence)

    def calculate_numbers(self, sequence):
        if len(sequence) == 0:
            sequence.append(0)
            sequence.append(1)

            return self.calculate_numbers(sequence)
        elif len(sequence) < self.length:
            last_number = sequence[len(sequence) - 1]
            second_to_last_number = sequence[len(sequence) - 2]

            sequence.append(last_number + second_to_last_number)

            return self.calculate_numbers(sequence)
        else:
            return sequence
