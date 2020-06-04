import requests

def get_loc():
    response = requests.request("GET", "https://coronavirus-19-api.herokuapp.com/countries")
    data = response.json()
    country_list = [e["country"] for e in data]
    r = requests.get('http://api.ipstack.com/check?access_key=9a3c1586757a2dab1aaa51f7919ab64e')
    data = r.json()
    if data["country_name"] == "United States":
        return "USA"
    elif data["country_name"] == "Great Britan":
        return "UK"
    elif data["country_name"] in country_list:
        return data["country_name"]
    else:
        return None    