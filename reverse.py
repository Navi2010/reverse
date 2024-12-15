class StringReverser:
    def __init__(self, input_string):
        self.__input_string = input_string

    def reverse(self):
        words = self.__input_string.split()
        reversed_words = words[::-1]
        return ' '.join(reversed_words)

# Example usage
reverser = StringReverser("hello my name is navya.")
print(reverser.reverse())  # Output: "Copilot Microsoft from world Hello"
