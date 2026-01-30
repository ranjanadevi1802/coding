class solution:
    def first_and_last_digit(self, n):
        def first_digit(num):
            while num >= 10:
                num //= 10
            return int(num)
        def last_digit(num):
            return int(num % 10)
        return (first_digit(n), last_digit(n))
    
# Example usage:
sol = solution()
print(sol.first_and_last_digit(12345))  # Output: (1, 5)
print(sol.first_and_last_digit(7))      # Output: (7, 7)
print(sol.first_and_last_digit(1001))   # Output: (1, 1)
