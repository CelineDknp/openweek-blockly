#!/bin/python3
from fractions import gcd

@@PGCD@@

def test_pgcd(n1, n2):
    return gcd(n1, n2)

if __name__ == "__main__":
    message = ""
    # Test 1: No common divisor (1)
    n1_test = 33
    n2_test = 17
    test = (pgcd(n1_test, n2_test) == test_pgcd(n1_test, n2_test))
    if test != True:
        message += "("+str(n1_test)+", "+str(n2_test)+") : Le PGCD est "+str(test_pgcd(n1_test, n2_test))+", mais votre fonction renvoie "+str(pgcd(n1_test, n2_test))+" !\n\n"
    # Test 2: Great numbers
    n1_test = 292758
    n2_test = 296893
    test = (pgcd(n1_test, n2_test) == test_pgcd(n1_test, n2_test))
    if test != True:
        message += "("+str(n1_test)+", "+str(n2_test)+") : Le PGCD est "+str(test_pgcd(n1_test, n2_test))+", mais votre fonction renvoie "+str(pgcd(n1_test, n2_test))+" !\n\n"
    # Test 3: With zero
    n1_test = 0
    n2_test = 98
    test = (pgcd(n1_test, n2_test) == test_pgcd(n1_test, n2_test))
    if test != True:
        message += "("+str(n1_test)+", "+str(n2_test)+") : Le PGCD est "+str(test_pgcd(n1_test, n2_test))+", mais votre fonction renvoie "+str(pgcd(n1_test, n2_test))+" !\n\n"
    n1_test = 12
    n2_test = 0
    test = (pgcd(n1_test, n2_test) == test_pgcd(n1_test, n2_test))
    if test != True:
        message += "("+str(n1_test)+", "+str(n2_test)+") : Le PGCD est "+str(test_pgcd(n1_test, n2_test))+", mais votre fonction renvoie "+str(pgcd(n1_test, n2_test))+" !\n\n"
    # Test 4: Forget to set the result
    n1_test = 12
    n2_test = 36
    if pgcd(n1_test, n2_test) == None:
        message = "Votre fonction ne renvoie pas de résultat. N'oubliez pas de définir la variable resultat !"
    print(message)
    