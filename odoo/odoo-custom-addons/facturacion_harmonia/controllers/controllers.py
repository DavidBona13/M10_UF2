# -*- coding: utf-8 -*-
# from odoo import http


# class FacturacionHarmonia(http.Controller):
#     @http.route('/facturacion_harmonia/facturacion_harmonia', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/facturacion_harmonia/facturacion_harmonia/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('facturacion_harmonia.listing', {
#             'root': '/facturacion_harmonia/facturacion_harmonia',
#             'objects': http.request.env['facturacion_harmonia.facturacion_harmonia'].search([]),
#         })

#     @http.route('/facturacion_harmonia/facturacion_harmonia/objects/<model("facturacion_harmonia.facturacion_harmonia"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('facturacion_harmonia.object', {
#             'object': obj
#         })
