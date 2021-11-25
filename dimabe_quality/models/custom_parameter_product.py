from odoo import fields, models, api


class CustomParameterProduct(models.Model):
    _name = 'custom.parameter.product'
    _description = 'Parametro de Producto'

    product_id = fields.Many2one(
        comodel_name='product.template',
        string='Producto',
        required=False)

    parameter_id = fields.Many2one(
        comodel_name='custom.quality.parameter',
        string='Parámetro',
        required=True)

    min_value = fields.Float(
        string='Valor Minimo', )

    max_value = fields.Float(
        string='Valor Maximo',
    )

    remark = fields.Text(
        string="Observaciones",
        required=False)

    type_of_parameter = fields.Selection(
        string='Tipo de Parametro',
        selection=[('range', 'Rango'),
                   ('select', 'Seleccion'), ],
        required=True, )

    parameter_value_id = fields.Many2one(
        comodel_name='custom.parameter.value',
        domain=lambda x: [('parameter_id', '=', x.parameter_id.id)],
        string='Valor')

    @api.constrains('min_value', 'max_value')
    def _check_values(self):
        for item in self:
            if item.type_of_parameter == 'range':
                if item.min_value and item.max_value:
                    if item.min_value > item.max_value:
                        raise models.UserError('El valor minimo no puede ser mayor al valor maximo')
                    elif item.max_value < item.min_value:
                        raise models.UserError('El valor maximo no puede ser menor al valor minimo')

    @api.onchange('parameter_id')
    def _onchange_parameter_id(self):
        res = {
            "domain": {
                "parameter_id": [('id', 'not in', self.product_id.quality_parameter_ids.mapped('parameter_id').ids)]
            }
        }
        return res
