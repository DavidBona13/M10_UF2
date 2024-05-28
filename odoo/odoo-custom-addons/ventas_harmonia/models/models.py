# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Venta (models.Modele):
    _name='ventas_harmonia.venta'
    _description='Venta de productos.'

    nom=fields.Char(string="Nombre", required=True)
    producto_id=fields.Many2one('inventario_harmonia.inventario', string="Producto", required=True)
    cantidad=fields.Integer(string="Cantidad", required=True, default=1)
    preu_unit=fields.Float(string="Precio unitario", related="producto_id.precio", readonly=True)
    preu_total=fields.Float(string="Total", compute='compute_total')
    date_venta=fields.Datetime(string="Fecha de venta", default=fields.Datetime.now)
    client_id=fields.Many2one('client.client', string="Cliente", required=True, readonly=True)
    factura_id=fields.Many2one('facturacion_harmonia.factura', string="Factura", readonly=True)

    #Calcular el preu total del producte multiplicant el preu base per la quantidad
    @api.depends('cantidad', 'preu_unit')
    def compute_total(self):
        for venta in self:
            venta.preu_total = venta.cantidad * venta.preu_unit

    #Creació de factures, és relaciona amb el model de facturació importat en el manifest.
    def crear_factura(self):
        #Environment, permet interectua amb la bases de dades i amb altres models.
        factura = self.env['facturacion_harmonia.factura'].create({
            'venta_id': self.id,
            'client_id': self.client_id.id,
            'date_factura': fields.Date.today(),
            'preu_total': self.preu_total,
        })
        self.factura_id = factura.id
        return factura
    



# class ventas_harmonia(models.Model):
#     _name = 'ventas_harmonia.ventas_harmonia'
#     _description = 'ventas_harmonia.ventas_harmonia'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
