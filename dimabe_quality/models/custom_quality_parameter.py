from odoo import fields, models, api


class CustomQualityParameter(models.Model):
    _name = 'custom.quality.parameter'
    _description = 'Parametros de Calidad'

    name = fields.Char('Nombre')
