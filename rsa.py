from modExpo import *

############################################################
# Generate the greatest common divisor.
############################################################
def extended_gcd(a, b):
    if b == 0:
        return (1, 0)
    else:
        q = a / int(b)
        r = a % b

        s, t = extended_gcd(b, r)
        return (t, s - q * t)

############################################################
# Return the GCD
############################################################
def gcd(a,b):
	t, ans = extended_gcd(a,b)
	return ans if ans > 0 else ans + a

############################################################
#
############################################################
def rsaGenerateSecretKey(anE=65537):
	d  = 1		#Secret Expo
	e  = anE	#Public Expo
	p  = 0		#Large Prime
	q  = 0		#Large Prime
	pN = 0		#Phi(n)
	n  = 0		#Modulous

	while (d == 1 or d == -1):
		#Generate p and q
		p = getPrimeP()
		q = getPrimeP()

		if bitLen(p) != 512 or \
		   bitLen(q) != 512 or \
		   testBit(p,512) != 0 or \
		   testBit(q,512) != 0:
			continue

		#Generate pN
		pN = (p-1)*(q-1)

		#Generate d
		d = gcd(pN, e)


	#Generate N
	n = p*q

	print "P: ", p
	print "Q: ", q
	return (d,n)




if __name__ == '__main__':
	e = 65537
	#d, n = rsaGenerateSecretKey()
	#print "d: ", d
	#print "n: ", n

	d = 95618645183246660182785685943482148211310366084802209175860448176506629146206881260703561863686696858053290778675207293909105913192649528903724236410791213606878088691250584930080652202647512308723164277030258223345884428234723409950111642464941760583306275153911730148326704194244576549674613820557367119353
	n = 123693481295141059737065759339899521284683736569809371575507603176813291112766183277066229794726521889902461761518239714597155150465964079107879185220757666419271218871162261222845535977607772354432013437657974129583030693681843056436028479933393107678114007944748876763113216975842390446852803337762180557769
	#message = 13945293450201704814553226581615391364450294031656145321247051595402407195776124062089668593622373390496593648357111962503436238929179078384473190096718407
	message2 = 20306241020233326969572750403118671361635765739564666633100953470260793460011295675507516242962463982208027863275912438042173481876366849965218633918534352481538544123468867121519581423448196702112476850025175819257486331317608329854136417634766518216813347980855010278534207267126553355296376799584397845245

	#print modExpo(message, e, n)
	print modExpo(message2, d, n)
	#m = 1234567890
	#m1 = 1029384710293847
	#m2 = 1340985730948572309485702394857

	#print modExpo(modExpo(m,e,n), d, n) == m
	#print modExpo(modExpo(m1,e,n), d, n) == m1
	#print modExpo(modExpo(m2,e,n), d, n) == m2