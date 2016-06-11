from google.appengine.api import search
import flask
from flask import Blueprint

from apps.admin.models import Activity
from apps.users import decor
from util.BaseModel import BaseModel

from google.appengine.ext import ndb

admin_blueprint = Blueprint('admin', __name__, template_folder='templates')


def get_from_search_doc(doc_id):
    if hasattr(doc_id, 'doc_id'):
        doc_id = doc_id.doc_id
    if doc_id:
        try:
            return ndb.Key(urlsafe=doc_id).get()
        except:
            return None


@admin_blueprint.route('/')
@decor.admin_required
def dashboard():
    return flask.render_template('dashboard.html',
                                 navbar=admin_area.navbar,
                                 recent_activity=Activity.query().order(-Activity.date_created))


@admin_blueprint.route('search/')
@decor.admin_required
def admin_search():
    query = flask.request.args.get('q', '').strip()

    if query:
        results = BaseModel.search_get_index().search(query)
        number_found = results.number_found
    else:
        results = None
        number_found = None

    return flask.render_template(
        'search.html',
        query=query,
        get_from_search_doc=get_from_search_doc,
        navbar=admin_area.navbar,
        number_found=number_found,
        results=results)


#
# Maps model to admin view

from app import app

app.register_blueprint(admin_blueprint, url_prefix='/admin/')

from apps.admin.register import admin_area
