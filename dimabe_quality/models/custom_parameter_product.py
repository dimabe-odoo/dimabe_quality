from odoo import fields, models, api


class ModelName(models.Model):
    _name = 'custom.parameter.product'
    _description = 'Parametro de Producto'

    product_id = fields.Many2one(
        comodel_name='product.template',
        string='Producto',
        required=False)

    parameter_id = fields.Many2one(
        comodel_name='custom.quality.parameter',
        string='Parametero',
        required=False)

    min_value = fields.Float(
        string='Valor Minimo',
        required=False)

    max_value = fields.Float(
        string='Valor Maximo',
        required=False)

    remark = fields.Text(
        string="Observaciones",
        required=False)

    @api.constrains('min_value','max_value')
    def _check_values(self):
        if self.min_value and self.max_value:
            if self.min_value > self.max_value:
                raise models.UserError('El valor minimo no puede ser mayor al valor maximo')
            elif self.max_value < self.min_value:
                raise models.UserError('El valor maximo no puede ser menor al valor minimo')

    @api.onchange('parameter_id')
    def _onchange_parameter_id(self):
        res = {
            "domain": {
                "parameter_id": [('id','not in',self.product_id.quality_parameter_ids.mapped('parameter_id').ids)]
            }
        }
        return res