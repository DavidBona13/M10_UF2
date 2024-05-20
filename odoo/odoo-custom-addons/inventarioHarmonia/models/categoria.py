from odoo import models, fields, api

class Categoria(models.Model):
    _name = 'inventario.categoria'
    _description = 'Categoría del producto'

    nom = fields.Char(string="Nombre categoría", required=True)
    descripcion = fields.Text(string="Descripción.")

    @api.multi 
    def consultar_prodCat(self, categoria_id):
        productos = self.env['inventario.inventario'].search([('categoria_id', '=', categoria_id)])
        return productos
    
    @api.multi 
    def cantidad_prod(self, categoria_id):
        productos = self.consultar_prodCat(categoria_id)
        quantitat = sum(producto.cantidad for producto in productos)
        return quantitat