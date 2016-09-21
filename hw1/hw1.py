def gcd(m, n):
	while m % n != 0:
		oldm = m
		oldn = n
		m = oldn
		n = oldm % oldn
	return n

class Fraction:

	def __init__(self,upper,lower):
		self.num = upper
		self.den = lower
		if self.den < 0:
			self.num = -self.num
			self.den = -self.den
		commonden = gcd(self.num, self.den)
		self.num//=commonden
		self.den//=commonden
	
	def getNum(self):
		return self.num

	def getDen(self):
		return self.den

	def __add__(self,otherfraction):
		num2 = self.num*otherfraction.den + self.den*otherfraction.num
		den2 = self.den * otherfraction.den
		return Fraction(num2,den2)

	def __str__(self):
		return str(self.num)+"/"+str(self.den)

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
		num2 = self.num*otherfrac.den - self.den*otherfrac.num
		den2 = self.den*otherfrac.den
		return Fraction(num2,den2)

	def __mul__(self, otherfrac):
		num2 = self.num*otherfrac.num
		den2 = self.den*otherfrac.den
		return Fraction(num2,den2)

	def __truediv__(self, otherfrac):
		num2 = self.num*otherfrac.den
		den2 = self.den*otherfrac.num
		return Fraction(num2,den2)





def main():
	testfrac1 = Fraction(1, 2)
	testfrac2 = Fraction(-2, 9)
	addfrac = testfrac1 + testfrac2
	print(addfrac)

	testfrac1 = Fraction(1, 2)
	testfrac2 = Fraction(1, -4)
	addfrac = testfrac1 + testfrac2
	print(addfrac)

	den1 = testfrac1.getDen()
	num1 = testfrac1.getNum()

	num2 = testfrac2.getNum()
	den2 = testfrac2.getDen()


	print(num1)
	print(den1)
	print(num2)
	print(den2)


	print(addfrac.getDen())
	print(addfrac.getNum())

	test1 = testfrac1.__add__(testfrac2)
	print(test1)


	test2 = testfrac1+testfrac2
	print(test2)


main()



