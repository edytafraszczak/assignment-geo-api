import requests


class GeolocationClient:
    BASE_URL = "http://localhost:8000/api/"
    LOGIN_URL = f"{BASE_URL}token/"
    GEOLOCATION_URL = f"{BASE_URL}geolocation/"

    def __init__(self):
        self.token = None

    def login(self, username, password):
        response = requests.post(self.LOGIN_URL, data={"username": username, "password": password})
        if response.status_code == 200:
            self.token = response.json()["access"]
        return self.token

    def create_geolocation(self, geolocation):
        return requests.post(self.GEOLOCATION_URL, headers=self._get_headers(), data=geolocation).json()

    def get_geolocation(self, ip_or_url):
        return requests.get(self._get_api_url_for_params(ip_or_url), headers=self._get_headers()).json()

    def delete_geolocation(self, ip_or_url):
        return requests.delete(self._get_api_url_for_params(ip_or_url), headers=self._get_headers())

    def _get_api_url_for_params(self, ip_or_url):
        return f"{self.GEOLOCATION_URL}?ip_or_url={ip_or_url}"

    def _get_headers(self):
        return {"Authorization": f"Bearer {self.token}"} if self.token else {}


ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin"

test_cases = (
    ("admin", "admin123"),  # invalid
    ("admin", "admin"),  # admin
    ("user", "useruser"),  # normal user can only retrieve
)
for test_case in test_cases:
    client = GeolocationClient()
    client.login(test_case[0], test_case[1])
    print(f'\n\nTEST CASE {test_case}')
    print(f"GET LOCATION allegro.pl - {client.get_geolocation('allegro.pl')}")
    print(f"GET LOCATION 8.8.8.8 - {client.get_geolocation('8.8.8.8')}")
    # create test
    client.create_geolocation({
        "ip_or_url": "test",
        "ip": "212.77.98.9",
        "type": "ipv4",
        "continent_code": "EU",
        "continent_name": "Europe",
        "country_code": "PL",
        "country_name": "Poland",
        "region_code": "PM",
        "city": "Sopot",
        "zip": "80-009",
        "latitude": 54.31930923461914,
        "longitude": 18.63736915588379
    })
    print(f"GET LOCATION test after creating - {client.get_geolocation('test')}")
    # delete test
    client.delete_geolocation("test")
    # try to check after deleting
    print(f"GET LOCATION test after deleting - {client.get_geolocation('test')}")
