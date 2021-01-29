def new_polynomial(coefix, expo):
    pol = dict()
    pol[expo] = coefix
    return pol

def add_term(pol, coefix, expo):
    pol[expo] = coefix
    return pol


def product_pol(pol_all_dict):
    pol_product = dict()
    for key in pol_all_dict:
        pol_product[key] = pol_all_dict[key][0] * pol_all_dict[key][1]
    return pol_product


def pol_all(pol_1, pol_2):
    pol_all_set = set(pol_1).union(set(pol_2))
    pol_all_dict = dict()
    for key in pol_all_set:
        pol_all_dict[key] = [pol_1.get(key, 0), pol_2.get(key, 0)]
    return pol_all_dict

def print_pols(polynomial):
    i = 0
    for key in sorted(polynomial, reverse=True):
        print(f"{polynomial[key]}x^{key}", end="")
        i+=1
        if not i == len(polynomial):
            print(" + ", end="")

    print("\n")

def pol_sum(pol_all_dict):
    pol_sum = dict()
    for key in pol_all_dict:
        pol_sum[key] = pol_all_dict[key][0] + pol_all_dict[key][1]
    return pol_sum
