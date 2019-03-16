from odoo import api, models
from odoo.exceptions import ValidationError

class TodoTask(models.Model):
    _inherit = 'todo.task'

    @api.model
    def website_form_input_filter(self, request, values):
        if values.get('name'):
            # Modify values
            values['name'] = values['name'].strip()
            # Validate values
            if len(values['name']) < 10:
                raise ValidationError(
                    'Text must be at least 10 characters long')
        return values
