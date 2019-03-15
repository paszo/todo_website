from odoo import http
from odoo.http import request

class Todo(http.Controller):

    @http.route('/helloworld', auth='public')
    def hello_world(self):
        return('<h1>Hello World!</h1>')

    @http.route('/hello', auth='public')
    def hello(self, **kwargs):
        return request.render('todo_website.hello')

    @http.route('/hellocms/<page>', auth='public')
    def hellocms(self, page, **kwargs):
        return request.render(page)
