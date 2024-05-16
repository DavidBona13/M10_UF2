# -*- coding: utf-8 -*-

from odoo import models, fields, api


class inventario(models.Model):
    _name = 'inventario.inventario'
    _description = 'Almacenamiento de objetos'

    id_inv = fields.Integer(string="id")
    nom = fields.Char(string="nombre", required= True, type="Nombre del producto/objeto.")
    descripcion = fields.Text(string="descripción", required= True, type="Descripción del producto/objeto.")
    cantidad = fields.Integer(string="cantidad", default=0 ,type="Cantidad de objetos.")
    precio = fields.Float(string="precio",required= True, type="Precio total o del producto.")
    precio_venta = fields.Float(string="precio de venta", required= True, type="Precio de venta.")
    marca = fields.Char(string="empresa", required= True, type="Marca del producto")
    categoria = fields.Char(string="categoria", required= True, type="Cateogira (limpieza, cocina, medicina...)")
    obj_perdut = fields.Boolean(String="objeto perdido", 
                                selection=[('true', 'True'), ('false', 'False')],
                                default=False,
                                type="Objetos perdidos.")

# class inventario(models.Model):
#     _name = 'inventario.inventario'
#     _description = 'inventario.inventario'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
