# Exercise 3. Write a Python program that can store a polynomial such as
# p(x) = 12x
# 10 + 9x7
# – x – 10
# as a list of terms. A term contains the coefficient and the power of x. For example, you
# would store p(x) as
# (12,10),(9,7),(–1,1),(–10,0)
# Supply functions to add, multiply, and print polynomials. Supply a function that makes a
# polynomial from a single term. For example, the polynomial p can be constructed as
# p = newPolynomial(-10, 0)
# addTerm(p, -1, 1)
# addTerm(p, 9, 7)
# addTerm(p, 12, 10)
# Then compute p(x) × p(x).
# q = multiply(p, p)
# printPolynomial(q)
# Provide a module for the polynomial functions and import it into the driver module.
import pol_mod

def main():
    p1 =pol_mod.new_polynomial(-10, 0)
    pol_mod.add_term(p1, -1, 1)
    pol_mod.add_term(p1, 9, 7)
    pol_mod.add_term(p1, 12, 10)

    p2 =pol_mod.new_polynomial(12, 0)
    pol_mod.add_term(p2, 42, 1)
    pol_mod.add_term(p2, 13, 8)
    pol_mod.add_term(p2, 14, 10)

    p_union = pol_mod.pol_all(p1, p2)
    p_sum = pol_mod.pol_sum(p_union)
    p_product = pol_mod.product_pol(p_union)

    pol_mod.print_pols(p1)
    pol_mod.print_pols(p2)
    pol_mod.print_pols(p_union)
    pol_mod.print_pols(p_sum)
    pol_mod.print_pols(p_product)



if __name__ == '__main__':
    main()