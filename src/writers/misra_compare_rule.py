""" This module contains the functions to compare MISRA rules """

def misra_c2004_compare(rule):
    """ compare misra C2004 rules """

    return int(rule.split('.')[0])*100 + int(rule.split('.')[1])


def misra_c2012_compare(rule):
    """ compare misra C2012 rules """

    return int(rule.split('.')[0])*100 + int(rule.split('.')[1])


def determine_compare_method(standard):
    """ determine the compare method based upon the provided standard """

    possibles = globals().copy()
    possibles.update(locals())
    method_name = "misra_" + standard.lower() + "_compare"
    method = possibles.get(method_name)
    if not method:
        raise NotImplementedError("Method %s not implemented" % method_name)

    return method
