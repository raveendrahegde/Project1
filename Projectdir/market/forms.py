from django import forms

class CompanyData(forms.Form):
	name = forms.CharField(label='Company', max_length=30)
	duration = forms.IntegerField(label='Years of investment', widget=forms.NumberInput(attrs={'title': 'How many years you are planning on investing in this company?','max_digit': 5,}))
	ebit = forms.DecimalField(label='EBIT', widget=forms.NumberInput(attrs={'title': 'Earnings before interest and taxes','max_digit': 12,}))
	depreciation = forms.DecimalField(label='Depriciation', widget=forms.NumberInput(attrs={'max_digit': 10,}))
	amortizatoin = forms.DecimalField(label='Amortizatoin', widget=forms.NumberInput(attrs={'max_digit': 10,}))
	nwc_change = forms.DecimalField(label='Change in net working capital', widget=forms.NumberInput(attrs={'max_digit': 10,}))
	capx = forms.DecimalField(label='Capital expenditure', widget=forms.NumberInput(attrs={'max_digit': 10,}))
	tax_rate = forms.DecimalField(label='Tax rate', widget=forms.NumberInput(attrs={'min_value': 0, 'max_value': 100}))
	ltgr = forms.DecimalField(label='Long term growth rate', widget=forms.NumberInput(attrs={'min_value': 0, 'max_value': 100}))
	stgr = forms.DecimalField(label='Short term growth rate', widget=forms.NumberInput(attrs={'min_value': 0, 'max_value': 100})) #This sould be changed, coz this may change each year
	discount_rate = forms.DecimalField(label='Discount rate', widget=forms.NumberInput(attrs={'min_value': 0, 'max_value': 100}))



