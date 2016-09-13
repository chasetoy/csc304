class frac:
	
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

		def gcd(m, n):
			while m % n != 0:
				oldm = m
				oldn = n

				m = oldn
				n = oldm % oldn
			return n

		num2 = self.num*otherfraction.den + self.den*otherfraction.num

		den2 = self.den * otherfraction.den

		commonden = gcd(num2, den2)

		return frac(num2//commonden,den2//commonden)

	def __str__(self):
		return str(self.num)+"/"+str(self.den)

	def gcd(m,n):
		while m%n != 0:
			oldm = m
			oldn = n

			m = oldn
			n = oldm%oldn
		return n


	def __ge__(self,n,d):
		f1=frac(n,d)
		f2=frac(n,d)
		if f1 >= f2:
			return True
		else:
			return False

	def __gt__(selfself,n,d):
		f1 = frac(n, d)
		f2 = frac(n, d)
		if f1 > f2:
			return True
		else:
			return False

	def __le__(self,n,d):
		f1 = frac(n, d)
		f2 = frac(n, d)
		if f1 <= f2:
			return True
		else:
			return False

	def __lt__(self,n,d):
		f1 = frac(n, d)
		f2 = frac(n, d)
		if f1 < f2:
			return True
		else:
			return False

	def __ne__(self,n,d):
		f1 = frac(n, d)
		f2 = frac(n, d)
		if f1 != f2:
			return True
		else:
			return False


	def __sub__(selfself, otherfrac):
		def gcd(m,n):
			while m%n != 0:
				oldm = m
				oldn = n

				m = oldn
				n = oldm%oldn
			return n

		num2 = self.num*otherfrac.den - self.den*otherfrac.num
		den2 = self.den*otherfrac.den
		commonden = gcd(num2, den2)

		return frac(num2//commonden,den2//commonden)

	def __mul__(self, otherfrac):
		def gcd(m, n):
			while m % n != 0:
				oldm = m
				oldn = n

				m = oldn
				n = oldm % oldn
			return n

		num2 = self.num*otherfrac.num
		den2 = self.den*otherfrac.den
		commondem = gcd(num2, den2)

		return frac(num2//commonden,den2//commondem)

	def __truediv__(self, otherfrac):
		def gcd(m, n):
			while m % n != 0:
				oldm = m
				oldn = n

				m = oldn
				n = oldm % oldn
			return n

		num2 = self.num*otherfrac.den
		den2 = self.den*otherfrac.num
		commonden = gcd(num2, den2)

		return frac(num2//commonden,den2//commonden)

	def __init__(self,top,bottom):
		self.num=top
		try:
			if self.num == int(top) == False:
				self.num = None
		except ValueError:
			print("Value Error : please enter an integer value")
	
		self.den=bottom
		try:
			if self.den == int(bottom) == False:
				self.den = None
		except ValueError:
			print("Value Error : please enter an integer value")



def main():
	testfrac1 = frac(1, 2)
	testfrac2 = frac(1, 4)
	addfrac = testfrac1 + testfrac2
	print(addfrac)

	testfrac1 = frac(1, 2)
	testfrac2 = frac(1, -4)
	addfrac = testfrac1 + testfrac2
	print(addfrac)



main()



