# -*- coding: utf-8 -*-
# from odoo import http


# class DimabeQuality(http.Controller):
#     @http.route('/dimabe_quality/dimabe_quality/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dimabe_quality/dimabe_quality/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('dimabe_quality.listing', {
#             'root': '/dimabe_quality/dimabe_quality',
#             'objects': http.request.env['dimabe_quality.dimabe_quality'].search([]),
#         })

#     @http.route('/dimabe_quality/dimabe_quality/objects/<model("dimabe_quality.dimabe_quality"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dimabe_quality.object', {
#             'object': obj
#         })
