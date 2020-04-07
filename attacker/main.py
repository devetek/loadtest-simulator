from locust import HttpLocust, between
import os
import task
 
class WebsiteUser(HttpLocust):
    service = 'zeus'

    if os.environ['SERVICE'] is not None:
        service = os.environ['SERVICE']


    get_task = getattr(task, service)

    task_set = get_task.Behavior
    wait_time = between(5, 15)