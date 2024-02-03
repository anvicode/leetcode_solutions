class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for operation in operations:
            if operation.lstrip("-").isdigit():
                record.append(int(operation))
            elif operation == "C":
                record.pop()
            elif operation == "D":
                record.append(record[-1] * 2)
            elif operation == "+":
                prev1 = record.pop()
                prev2 = record[-1]
                record.append(prev1)
                record.append(prev1 + prev2)
        return sum(record)
