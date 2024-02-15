import requests

req_data = {
    "bill_length_mm": 0,
    "species_Chinstrap": False,
    "species_Gentoo": False,
    "sex_male": False
}
req = requests.post('http://127.0.0.1:8080/predict', json = [req_data])
res = req.json().get('predict')[0]
