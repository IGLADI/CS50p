import requests
import sys
if len(sys.argv) >= 1:
    try:
        bictoins_amount = float(sys.argv[1])
        try:
            response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
            amount = response.json()["bpi"]["USD"]["rate_float"] * bictoins_amount
            print(f"${amount:,.4f}")
        except requests.RequestException:
            pass
    except ValueError:
        sys.exit("Error: Invalid amount")