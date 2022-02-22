class Solution:

	def run(self, N, M):
		#
		# Write your code below; return type and arguments should be according to the problem\'s requirements
		#
		sequence =""

		for i in range(N,M+1):
			# if it has both dividance to 3 and 5 then this prints
			if i % 15 == 0:
				sequence += ("FizzBuzz,")
			# if it has dividance to 3 then this prints
			elif i % 3 == 0:
				sequence += ("Fizz,") 
			# if it has dividance to 5 then this prints
			elif i % 5 == 0:
				sequence += ("Buzz,") 
			# if they have no mods of 3 or 5 then number is printed
			else:
				sequence += (str(i)+",")
		
		# remove last ","
		sequence = sequence[:-1]
		
		return sequence
