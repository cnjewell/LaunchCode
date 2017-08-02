# Lists

def get_country_codes(prices):
    country_codes = []
    prices = prices.split(",")

    for price in prices:
        country_prices = price.split("$")
        country_codes.append(country_prices[0])
    output = ','.join(country_codes)
    return output


print(get_country_codes("NZ$300, KR$1200, DK$5"), "NZ, KR, DK")
print(get_country_codes("US$40, AU$89, JP$200"), "US, AU, JP")
print(get_country_codes("AU$23, NG$900, MX$200, BG$790, ES$2"), "AU, NG, MX, BG, ES")
print(get_country_codes("CA$40"), "CA")
