import re

text = "ES oversold reading triggered at 3937.50 invalid under 3930"
'''
New entry made in the Index Quant Signals Table
SymbolESM23Period30minSignalShortSignal Price3,969.50Target3959- 3949- 3937Stop3976
'''
first_word = text.split()[0]
print("Instrument:", first_word)

def instrument(text):
    match = re.search(r'^\w+', text)
    instrument_match = match.group(0)
    return instrument_match

os_match = re.search(r'oversold reading triggered at (\d+)', text)
ob_match = re.search(r'overbought reading triggered at (\d+)', text)
os_stop = re.search(r'invalid under (\d+)', text)
ob_stop = re.search(r'invalid over (\d+)', text)

if instrument(text) == 'ES':
    if os_match != None: 
        os_strike = os_match.group(1)
        print('Strike:', os_strike)
        number = os_stop.group(1)
        print('Stop:', number)
        # TODO: Add code to set sell order 
else if instrument(text) == 'New':
        
else:
    print("No valid instrument found")
    
