# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Inventario(models.Model):
    _name = 'inventario.inventario'
    _description = 'Almacenamiento de objetos'

    #id_inv = fields.Integer(string="ID")
    nom = fields.Char(string="Nombre", required=True)
    descripcion = fields.Text(string="Descripción", required=True)
    categoria_id = fields.Many2one('inventario.categoria', string='Categoría')
    cantidad = fields.Integer(string="Cantidad", default=0)
    precio = fields.Float(string="Precio", required=True)
    precio_venta = fields.Float(string="Precio de venta", required=True)
    marca = fields.Char(string="Marca", required=True)
    categoria = fields.Char(string="Categoría", required=True)
    obj_perdut = fields.Boolean(string="Objeto perdido", default=False)
    fecha_caducidad = fields.Date(string='Fecha de Caducidad')


    

#class FacturacionInventario(models.Model):
#    _name = 'inventario.facturacion'
#    _description = 'Facturación de los objetos que se almacenan (compras o ventas)'

#    id_facturaInv = fields.Integer(string="ID Factura Inventario")
#    titulo = fields.Char(string="Título", required=True)
#    desc_factInv = fields.Text(string="Descripción", required=True)
#    id_cliente = fields.Many2one('res.partner', string="Cliente", required=True) 
#    id_inventario = fields.Many2one('inventario.inventario', string="Producto", required=True)  
#    precio_ventaFact = fields.Float(string="Precio", required=True)
#    cantidadFact = fields.Integer(string="Cantidad", required=True, default=0)
#    fecha = fields.Date(string="Fecha", default=fields.Date.today, required=True)


@api.model
def crear_producto(self, nom, descripcion, categoria_id, cantidad, precio, precio_venta, marca, categoria, obj_perdut, fecha_caducidad):
    producto = self.create({
        'nombre': nom,
        'description': descripcion,
        'categoria_id': categoria_id,
        'cantidad': cantidad,
        'precio': precio,
        'precio_venta': precio_venta,
        'marca': marca,
        'categoria': categoria,
        'obj_perdut': obj_perdut,
        'fecha_caducidad': fecha_caducidad,
    })
    return producto

def crear_producto_button(self):
        self.crear_producto({
            self.nom,
            self.descripcion,
            self.categoria_id.id,
            self.cantidad,
            self.precio,
            self.precio_venta,
            self.marca,
            self.categoria,
            self.obj_perdut,
            self.fecha_caducidad
        })

def modificar_producto_btn(self):
     self.write({
          'nom': self.nom,
          'descripcion': self.descripcion,
          'categoria_id': self.categoria_id.id,
          'cantidad': self.cantidad,
          'precio': self.precio,
          'precio_venta': self.precio_venta,
          'marca': self.marca,
          'categoria': self.categoria,
          'obj_perdut': self.obj_perdut,
          'fecha_caducidad': self.fecha_caducidad,

     })

def reduir_cantidad(self, cantidad_red):
    if cantidad_red > self.cantidad:
        raise ValueError("Cantidad disponible insuficiente")
    else:
        self.cantidad -= cantidad_red
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
