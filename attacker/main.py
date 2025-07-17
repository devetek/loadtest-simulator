from locust import HttpUser, between
import os
import task
 
class WebsiteUser(HttpUser):
    service = 'example'

    if os.environ['SERVICE'] is not None:
        service = os.environ['SERVICE']


    get_task = getattr(task, service)

    # task_set = get_task.Behavior
    tasks = [get_task.Behavior]
    wait_time = between(5, 15)