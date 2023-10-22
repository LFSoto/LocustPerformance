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
from resources import schedule_data as body
from resources import schedule_endpoints as endpoints
from dotenv import load_dotenv
from locust import HttpUser, task, between, events

load_dotenv()
user_info = {
    "username": os.getenv('username'),
    "password": os.getenv('password')
}
sch_qa_dev_env = os.getenv('sch_qa_dev_env')


class ScheduleBase(HttpUser):
    global scheduledJobsIds, auth_token, headers
    scheduledJobsIds = []
    wait_time = between(1, 4)

    @events.test_start.add_listener
    def on_start(self):
        print('Starting...')
        global headers
        headers = init_headers(get_authentication_token(self, user_info))
        self.client.base_url = sch_qa_dev_env
        return super().on_start()

    @task
    def execute_get_all_jobs(self):
        get_method(self, headers, endpoint=endpoints.get_all_jobs,
                   action='Get all scheduled job')

    @task
    def execute_get_job_by_id(self):
        createResponse = post_method(
            self, headers, action='Create scheduled job', body=body.create_scheduled_job_body, endpoint=endpoints.create_scheduled_job)
        if createResponse:
            jobId = createResponse.json()['data']['id']
            scheduledJobsIds.append(jobId)
            get_method(self, headers, endpoint=endpoints.get_job_by_id % jobId,
                       action='Get scheduled job by id')

    @task
    def execute_get_executions_by_job_id(self):
        createResponse = post_method(
            self, headers, action='Create scheduled job', body=body.create_scheduled_job_body, endpoint=endpoints.create_scheduled_job)
        if createResponse:
            time.sleep(65)
            jobId = createResponse.json()['data']['id']
            scheduledJobsIds.append(jobId)
            get_method(self, headers, endpoint=endpoints.get_executions_by_job_id % jobId,
                       action='Get executions of a job by id')

    @task
    def execute_create_job(self):
        createResponse = post_method(
            self, headers, action='Create scheduled job', body=body.create_scheduled_job_body, endpoint=endpoints.create_scheduled_job)
        if createResponse:
            scheduledJobsIds.append(createResponse.json()['data']['id'])

    @task
    def execute_delete_job(self):
        createResponse = post_method(
            self, headers, action='Create scheduled job', body=body.create_scheduled_job_body, endpoint=endpoints.create_scheduled_job)
        if createResponse:
            jobId = createResponse.json()['data']['id']
            delete_method(self, headers, action='Delete scheduled job',
                          endpoint=endpoints.alter_scheduled_job % jobId)

    @task
    def execute_edit_job(self):
        createResponse = post_method(
            self, headers, action='Create scheduled job', body=body.create_scheduled_job_body, endpoint=endpoints.create_scheduled_job)
        if createResponse:
            jobId = createResponse.json()['data']['id']
            scheduledJobsIds.append(jobId)
            put_method(self, headers, action='Edit scheduled job', body=body.modify_schedule_job_body,
                       endpoint=endpoints.alter_scheduled_job % jobId)

    def on_stop(self):
        print('Stopping...')
        if scheduledJobsIds.count != 0:
            for jobId in scheduledJobsIds:
                endpoint = endpoints.alter_scheduled_job % jobId
                print('Clean up: deleting scheduled job ' + jobId)
                delete_method(self, headers, 'Delete scheduled job', endpoint)
