# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Facturacio (models.Model):
    _name='facturacion_harmonia.facturacio'
    _description='Facturas Hotel Harmonia'

    nom=fields.Char(string="Número de factura", required=True, readonly=True)
    client_id=fields.Many2one('', string="Cliente", required=True)
    date_factura=fields.Date(string="Fecha de factura", default=fields.Date.context_today)
    linia_factura=fields.One2many("facturacion_harmonia", "factura_id", string="Línia de factura")
    total=fields.Float(string="Total", compute="compute_total")

    #Total, cada vegada que s'actualitza
    @api.depends("linea_factura.subtotal")
    def _compute_total(self):
        for factura in self:
            factura.total = sum(li.subtotal for li in factura.linia_factura)

    
class Linea_factura(models.Model):
    _name = 'facturacion_harmonia.lineafactura'
    _description = 'Línea de factura harmonia'

    producto_id = fields.Many2one("ventas_harmonia.venta", string="Producto", required=True)
    cantidad = fields.Integer(string="Cantidad", required=True)
    preu_unit = fields.Float(string="Precio Unitario", required=True)
    subtotal = fields.Float(string="Subtotal", compute="compute_subtotal", store=True)
    factura_id = fields.Many2one("facturacion_harmonia.facturacio", string="Factura", required=True)

    #Actualitza el preu 'subtotal' cada vegada que s'actualitza
    api.depend("cantidad", "preu_unit")
    def compute_subtotal(self):
        for li in self:
            li.subtotal = li.cantidad * li.preu_unit