import math
from decimal import *
# getcontext().prec = 12 #Method from decimal module

def valuate(data):
    TWOPLACES = Decimal(10) ** -2
    fcf = calc_freecashflow(data)
    pcf = [fcf] #Projected Cash Flow for each year, 1st value is for current year

    try:
        ltgr = data.get('ltgr')
        strg = data.get('stgr')
        discout_rate = data.get('discount_rate')
        duration = data.get('duration')
    except Exception as e4:
        print "Can't extract values"
        return False

    try:
        for year in range(1, duration + 1):
            pcf.append(pcf[-1] * (1+ strg/100))
    except Exception as e3:
        print "Can't calc pcfs"

    try:
        terminal_value = (pcf[-1] * (1 + ltgr/100)) / (discout_rate/100 - ltgr/100)
    except ZeroDivisionError:
        print "Can't devide by zero"
        return False

    try:
        dcf_without_tv = 0
        for year in range(1, duration + 1):
            zz = math.pow((1 + discout_rate/100), year)

            dcf_without_tv += pcf[year] / Decimal(zz)

        dcf =  dcf_without_tv + terminal_value / Decimal(math.pow((1 + discout_rate/100), duration)) #CDF
        return dcf.quantize(TWOPLACES)

    except Exception as e5:
        print "Can't calc DCF"
        return False

    return dcf


def calc_freecashflow(data):
    try:
        ebit = data.get('ebit')
        depreciation = data.get('depreciation')
        amortization = data.get('amortization')
        nwc_change = data.get('nwc_change')
        capx = data.get('capx')
        tax_rate = data.get('tax_rate')
    except Exception as e1:
        return False

    try:
        fcf = ebit * (1 - tax_rate/100) + depreciation + amortization - nwc_change - capx
    except Exception as e2:
        print "Unable to calculate"
        return False

    return fcf


