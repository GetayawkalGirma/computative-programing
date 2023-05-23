class Solution:
    def fizzBuzz(self, n: int) -> List[str]:

        answer_array = []

        for i in range(1, n+1):

            if ((i % 3 == 0) and (i % 5 == 0)):
                answer_array.append("FizzBuzz")
            elif i % 3 == 0:
                answer_array.append("Fizz")
            elif i % 5 == 0:
                answer_array.append("Buzz")
            else:
                answer_array.append(str(i))

        return answer_array
