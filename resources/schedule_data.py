###
# Copyright (c) 2023 Wind River Systems, Inc.
#
# The right to copy, distribute, modify, or otherwise make use of this software may be licensed only pursuant to the terms of an applicable Wind River license agreement.
###

create_scheduled_job_body = {
    "name": "loadtesting",
    "description": "New scheduled job",
    "cron": "* * * * *",
    "scheduleOptions": {
        "endpoint": "https://630d388753a833c5343d72ed.mockapi.io/api/v1",
        "httpMethod": "POST",
        "httpParams": {
            "param1": 1
        },
        "httpPayload": {
            "id": 1,
            "name": "test"
        },
        "authRequired": True
    }
}

modify_schedule_job_body = {
    "description": "Updated description",
    "cron": "*/2 * * * *",
    "scheduleOptions": {
        "endpoint": "https://630d388753a833c5343d72ed.mockapi.io/api/v1",
        "httpMethod": "GET",
        "httpParams": {
            "param1": 1
        },
        "httpPayload": {
            "id": 2,
            "name": "Examples payload"
        },
        "authRequired": False
    }
}
