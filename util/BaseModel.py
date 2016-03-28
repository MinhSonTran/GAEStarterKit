"""
Contains base class for ndb models. This adds functionality that is expected (or at least useful) elsewhere in GEAStarterKit.
"""
from google.appengine.ext import ndb


class BaseModel(ndb.Model):
    date_created = ndb.DateTimeProperty(auto_now_add=True, required=True)
    date_modified = ndb.DateTimeProperty(auto_now=True, required=True)