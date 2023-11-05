###
# Copyright (c) 2023 Wind River Systems, Inc.
#
# The right to copy, distribute, modify, or otherwise make use of this software may be licensed only pursuant to the terms of an applicable Wind River license agreement.
###

import os
import json
import time
from common.utilities import get_authentication_token, init_headers
from common.http_methods import get_method, post_method, delete_method, put_method
from resources import endpoints as endpoints
from locust import HttpUser, task, between, events

class RandomUser(HttpUser):
    global headers;
    wait_time = between(1, 4)

    @task
    def execute_get_random_user(self):
        headers = {
        "Accept": "*/*",
        "Accept-Enconding":"gzip, deflate, br",
        "Connection":"keep-alive"
        }
        get_method(self, headers, endpoint=endpoints.get_random_user,
                   action='Get random user')
