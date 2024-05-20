# -*- coding: utf-8 -*-
# from odoo import http


# class VentasHarmonia(http.Controller):
#     @http.route('/ventas_harmonia/ventas_harmonia', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ventas_harmonia/ventas_harmonia/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ventas_harmonia.listing', {
#             'root': '/ventas_harmonia/ventas_harmonia',
#             'objects': http.request.env['ventas_harmonia.ventas_harmonia'].search([]),
#         })

#     @http.route('/ventas_harmonia/ventas_harmonia/objects/<model("ventas_harmonia.ventas_harmonia"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ventas_harmonia.object', {
#             'object': obj
#         })
