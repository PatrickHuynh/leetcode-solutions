class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        return [self.get_fizz_buzz(i) for i  in range(1,n+1)]
        
    def get_fizz_buzz(self, num):
        a = num % 3 == 0
        b = num % 5 == 0
        
        if a and b:
            return "FizzBuzz"
        if a:
            return "Fizz"
        if b:
            return "Buzz"
        return str(num)
            
        
    