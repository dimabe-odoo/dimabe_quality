from odoo import fields, models, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    quality_parameter_ids = fields.One2many(
        comodel_name='custom.parameter.product',
        inverse_name='product_id',
        string='Calidad',
        required=False)