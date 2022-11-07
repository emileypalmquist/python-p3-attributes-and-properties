#!/usr/bin/env python3

class Person:
    jobs = ["ITC"]

    def __init__(self, name="Doe", job="Unknown"):
        self._name = name
        self._job = job

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        if type(new_name) is str and 1 <= len(new_name) <= 25:
            self._name = new_name.title()
            return self._name
        else:
            print("Name must be string between 1 and 25 characters.")

    def get_job(self):
        return self._job

    def set_job(self, new_job):
        if new_job in self.jobs:
            self._job = new_job
        else:
            print("Job must be in list of approved jobs.")

    job = property(get_job, set_job,)
    name = property(get_name, set_name,)
