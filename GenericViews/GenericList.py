"""
Provides generic object listing functionality.
"""

from google.appengine.ext import ndb
import flask

from GenericViews.GenericBase import GenericBase
from util.request_util import request_wants_json


class GenericList(GenericBase):
    template = 'generic-list.html'
    table_content_template = 'components/inline-table-content.html'

    order_by = '-date_created'

    # TODO: Add sort by
    # TODO: Add grouping

    def get_query(self):
        q = self.model.query()
        if self.order_by:
            if self.order_by.startswith('-'):
                q = q.order(-getattr(self.model, self.order_by[1:]))
            else:
                q = q.order(getattr(self.model, self.order_by))

        return q

    def get(self):
        cursor = flask.request.args.get('cursor', None)

        if cursor:
            try:
                cursor = ndb.Cursor.from_websafe_string(cursor)
            except (ValueError, TypeError):
                return self.show_404()
        else:
            cursor = None

        query = self.get_query()
        rows, next_cursor, more = query.fetch_page(page_size=self.page_size, start_cursor=cursor)

        for row in rows:
            row = self.add_extra_fields(row)

        if next_cursor and more:
            next_cursor = next_cursor.to_websafe_string()
        else:
            next_cursor = None

        context = {
            'controller': self,
            self.variable_rows: rows,
            self.variable_next_cursor: next_cursor,
            'table_content_template': self.table_content_template
        }

        if request_wants_json():
            if next_cursor:
                next_url = flask.url_for(self.list_view, cursor=next_cursor)
            else:
                next_url = False
            return flask.jsonify({
                'next_cursor': next_cursor,
                'next_cursor_url': next_url,
                'content': flask.render_template(self.table_content_template, **context)
            })
        else:
            return self.render(**context)
