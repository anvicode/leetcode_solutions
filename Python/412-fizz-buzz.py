class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = [str(i) for i in range(1, n + 1)]
        for i, _ in enumerate(answer):
            if (i + 1) % 3 == 0 and (i + 1) % 5 == 0:
                answer[i] = "FizzBuzz"
            elif (i + 1) % 3 == 0:
                answer[i] = "Fizz"
            elif (i + 1) % 5 == 0:
                answer[i] = "Buzz"
            else:
                answer[i] = str(i + 1)
        return answer
