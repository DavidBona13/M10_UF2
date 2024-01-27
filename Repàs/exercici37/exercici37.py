
def amb_iva(ftotal,iva):
    ivaTotal = iva / 100 + 1
    ftotal = ftotal * ivaTotal
    return ftotal