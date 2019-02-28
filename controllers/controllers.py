# -*- coding: utf-8 -*-
from odoo import http

# class VenteS6(http.Controller):
#     @http.route('/vente_s6/vente_s6/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vente_s6/vente_s6/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vente_s6.listing', {
#             'root': '/vente_s6/vente_s6',
#             'objects': http.request.env['vente_s6.vente_s6'].search([]),
#         })

#     @http.route('/vente_s6/vente_s6/objects/<model("vente_s6.vente_s6"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vente_s6.object', {
#             'object': obj
#         })