from odoo import models, fields, api

class Categoria(models.Model):
    _name = 'inventario_harmonia.categoria'
    _description = 'Categoría del producto'

    nom = fields.Char(string="Nombre categoría", required=True)
    descripcion = fields.Text(string="Descripción.")

   # Consulta els productes que formen part d'aquesta categoria.
    def consultar_prodCat(self):
        productos = self.env['inventario_harmonia.inventario'].search([('categoria_id', '=', self.id)])
        return productos
    
    #Fa la suma total de productes de qualsevol tipus que pertany a una categoria concreta
    def cantidad_prod(self):
        productos = self.consultar_prodCat()
        quantitat = sum(producto.cantidad for producto in productos)
        return quantitat
 