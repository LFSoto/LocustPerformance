###
# Copyright (c) 2023 Wind River Systems, Inc.
#
# The right to copy, distribute, modify, or otherwise make use of this software may be licensed only pursuant to the terms of an applicable Wind River license agreement.
###

from common.utilities import log_response, log_exception

def get_method(self, headers, *args, **kwargs):
    action = kwargs.get('action', None)
    endpoint = kwargs.get('endpoint', None)
    try:
        with self.client.get(endpoint, catch_response=True, headers=headers) as response:
            log_response(action, response)
            return response
    except Exception as ex:
        log_exception(ex)

def post_method(self, headers, *args, **kwargs):
    action = kwargs.get('action', None)
    body = kwargs.get('body', None)
    endpoint = kwargs.get('endpoint', None)
    try:
        with self.client.post(endpoint, catch_response=True, headers=headers, json=body) as response:
            log_response(action, response)
            return response
    except Exception as ex:
        log_exception(ex)

def put_method(self, headers, *args, **kwargs):
    action = kwargs.get('action', None)
    body = kwargs.get('body', None)
    endpoint = kwargs.get('endpoint', None)
    try:
        with self.client.put(endpoint, catch_response=True, headers=headers, json=body) as response:
            log_response(action, response)
            return response
    except Exception as ex:
        log_exception(ex)

def delete_method(self, headers, *args, **kwargs):
    action = kwargs.get('action', None)
    endpoint = kwargs.get('endpoint', None)
    try:
        with self.client.delete(endpoint, catch_response=True, headers=headers) as response:
            log_response(action, response)
            return response
    except Exception as ex:
        log_exception(ex)
