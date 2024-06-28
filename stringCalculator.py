class StringCalculator:
    def add(self, numbers:str) -> int:
        if not numbers:
            return 0
        
        delimiter =','
        if numbers.startswith('//'):
            delimiter_str , numbers = numbers.split('\n',1)
            delimiter = delimiter_str[2:]

        numbers = numbers.replace(delimiter, ',')
        numbers = numbers.replace('\n', ',')
        number_list = numbers.split(',')

        negatives = [num for num in number_list if num and int(num) < 0]
        if negatives:
            raise ValueError(f"negative numbers not allowed {', '.join(negatives)}")
        

        total = sum(int(num) for num in number_list if num)

        return total


calculator = StringCalculator()

try:
    result = calculator.add("1,2,3,4")
    print(result)

except ValueError as e:
    print(e)
