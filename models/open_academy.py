# -*- coding: utf-8 -*-

from odoo import _, api, exceptions, fields, models

class Course(models.Model):
     _name = 'openacademy.course'
     _description = 'Cursos'
     name = fields.Char(string="Title", required=True)    
     description = fields.Text("Description")
     responsible_id = fields.Many2one(
          'res.users',
          ondelete = 'set null',
          string="Responsible",
          index=True
     )


     def copy(self, default=None):
        default = dict(default or {})

        copied_count = self.search_count(
            [('name', '=like', _(u"Copy of {}%").format(self.name))])
        if not copied_count:
            new_name = _(u"Copy of {}").format(self.name)
        else:
            new_name = _(u"Copy of {} ({})").format(self.name, copied_count)

        default['name'] = new_name
        return super(Course, self).copy(default)

     _sql_constraints = [
        ('name_description_check',
         'CHECK(name != description)',
         "El titulo y la descripción no pueden ser iguales"),

        ('name_unique',
         'UNIQUE(name)',
         "El titulo del curso debe ser unico"),
    ]
