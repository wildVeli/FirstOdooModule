# -*- coding: utf-8 -*-
from odoo import http

# class Fctmanagent(http.Controller):
#     @http.route('/fctmanagent/fctmanagent/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fctmanagent/fctmanagent/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('fctmanagent.listing', {
#             'root': '/fctmanagent/fctmanagent',
#             'objects': http.request.env['fctmanagent.fctmanagent'].search([]),
#         })

#     @http.route('/fctmanagent/fctmanagent/objects/<model("fctmanagent.fctmanagent"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fctmanagent.object', {
#             'object': obj
#         })