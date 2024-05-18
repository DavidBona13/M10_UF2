from odoo import models, fields, api

class Categoria(models.Model):
    _name = 'inventario.categoria'
    _description = 'Categoría del producto'

    nom = fields.Char(string="Nombre categoría", required=True)
    descripcion = fields.Text(string="Descripción.")