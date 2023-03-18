# Code block from ChatGPT 

from bs4 import BeautifulSoup

# HTML code block
html_code = '<div class="tr-stocktradeBlock"><div class="tr-leftTrade">Symbol</div><div class="tr-rightTrade">SPX IC 4015/4020/3795/3790 Call/Put March 20</div><div class="tr-leftTrade">Period</div><div class="tr-rightTrade">30min</div><div class="tr-leftTrade">Signal</div><div class="tr-rightTrade">Short</div><div class="tr-leftTrade">Signal Price</div><div class="tr-rightTrade">0.55</div><div class="tr-leftTrade">Target</div><div class="tr-rightTrade">.10- zero</div><div class="tr-leftTrade">Stop</div><div class="tr-rightTrade"></div></div>'

# Parse the HTML code block with Beautiful Soup
soup = BeautifulSoup(html_code, 'html.parser')

# Extract the trade attributes and their values
trade_dict = {}
for left, right in zip(soup.select('.tr-leftTrade'), soup.select('.tr-rightTrade')):
    trade_dict[left.text.strip()] = right.text.strip()

# Print the trade dictionary
print(trade_dict)
