import requests


class BackendHandler(object):
    BACKEND_ENDPOINT = "https://akef-test-ibm.eu-gb.mybluemix.net/"
    CREATE_DISASTER_ENDPOINT = "disasters/"
    GET_JWT_TOKEN_ENDPOINT = "auth/jwt-api-token/"

    @classmethod
    def get_jwt_token(cls, user= "nada", password = "nada123456"):
        url = cls.BACKEND_ENDPOINT + cls.GET_JWT_TOKEN_ENDPOINT
        headers = {'Content-Type': 'application/json'}
        payload = {
            "username": user,
            "password": password
        }
        print("getting jwt token")
        response = requests.post(url,json = payload, headers=headers)
        jwt_token = response.json().get('token')
        return jwt_token


    @classmethod
    def create_disaster(cls, lat, lang, level_of_danger, diameter = 50):
        url = cls.BACKEND_ENDPOINT + cls.CREATE_DISASTER_ENDPOINT
        jwt_token = cls.get_jwt_token()
        headers = {'Content-Type': 'application/json', 'Authorization': 'JWT ' + jwt_token}
        payload = {
            "diameter": diameter,
            "level_of_danger": level_of_danger,
            "lat"	:	lat,
            "lang"	:	lang
        }
        print("Creating disaster in the backend")
        response = requests.post(url,json = payload, headers=headers)
        return response.json()



# DANGER_LEVELS = (
#     ('E', 'Easy'),
#     ('M', 'Medium'),
#     ('D', 'Danger'),
#     ('ED', 'Extra Danger')
# )


if __name__ == "__main__":
    disaster = {
        "diameter": 30,
        "level_of_danger": "D",
        "lat"	:	80.5,
        "lang"	:	15.6
    }
    response = BackendHandler.create_disaster(**disaster)
    print(response)
