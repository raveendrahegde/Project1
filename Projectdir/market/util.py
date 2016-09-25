def valuate(data):
	fcf = calc_fcf(data)
	pcf = [fcf] #Projected Cash Flow for each year
	try:
		print dir(data)
		ltgr = data.get('ltgr')
		strg = data.get('stgr')
		discout_rate = data.get('discount_rate')
		duration = data.get('duration')
		print duration
	except Exception as e:
		print "Can't get " + str(e)
		return False

	try:
		for year in range(1, duration + 1):
			pcf.append(pcf[-1] * strg/100)
	except Exception as e:
		print "Can't calc " + e

	try:
		terminal_value = (pcf[-1] * (1 + ltgr/100)) / (discout_rate/100 - ltgr/100)
	except ZeroDivisionError:
		print "Can't devide by zero"
		return False


def calc_fcf(data):
	try:
		ebit = data.get('ebit')
		depriciation = data.get('depriciation')
		amortizatoin = data.get('amortizatoin')
		nwc_change = data.get('nwc_change')
		capx = data.get('capx')
		tax_rate = data.get('tax_rate')

		tax = tax_rate/100
	except Exception as e:
		print e
		return False

	fcf = ebit(1-tax) + depreciation + amortization - nwc_change - capx

	return fcf


