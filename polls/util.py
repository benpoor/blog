__author__ = 'Administrator'
import json

class MyJsonEncoder(json.JSONEncoder):
    def default(self, o):
        d={}
        d['__class__'] = o.__class__.__name__
        d['__module'] = o.__module__
        d.update(o.__dict__)
        return d