class Fraction:	
	
	def getNum(self):
		return self.num

	def getDen(self):
		return self.den

	def gcd(self,m,n):

        while m%n != 0:

            oldm = m

            oldn = n

   			m = oldn

            n = oldm%oldn

        return n

	def __add__(self,otherfraction):

        newnum = self.num*otherfraction.den + self.den*otherfraction.num

        newden = self.den * otherfraction.den

        cd = self.gcd(newnum,newden)

        return Fraction(newnum//cd,newden//cd)


	def __sub__(self, otherfraction):


	def __init__(self,n,d):
		self.n=n
		try:
			if self.n = int(n) == False:
				self.n = None
		except ValueError:
			print("Value Error : please enter an integer value")
	
		self.d=d
		try:
			if self.d = int(d) == False:
				self.d = None
		except ValueError:
			print("Value Error : please enter an integer value")



