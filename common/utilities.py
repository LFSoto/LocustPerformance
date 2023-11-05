
import os
import logging
logging.basicConfig(level=logging.INFO)

um_auth = os.getenv('um_env')

def get_authentication_token(self, user_info):
    with self.client.post(url="url", catch_response=True, json=user_info) as response:
        if response.status_code == 200:
            token = 'Bearer ' + response.json()['data']['jwt']
            return token
        else:
            response.failure("Failed")


def init_headers(authToken):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': authToken
    }
    return headers


def log_response(action, response):
    if response.status_code == 200:
        logging.info(action + ' request was called successfully with status code: %s',
                     response.status_code)
    else:
        response.failure(
            action + ' request failed with status code: ' + str(response.status_code))
        logging.info(response.status_code, exc_info=True)


def log_exception(exception):
    template = "An exception of type {0} occurred. Arguments:\n{1!r}"
    message = template.format(type(exception).__name__, exception.args)
    logging.exception(message)
