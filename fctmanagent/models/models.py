# -*- coding: utf-8 -*-

from odoo import models, fields, api,exceptions


# class fctmanagent(models.Model):
#     _name = 'fctmanagent.fctmanagent'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
class Tutor (models.Model):
    _inherit = 'res.users'
    
    isTutor = fields.Boolean()
    pupils = fields.Many2one('res.users',ondelete='set null',string="Pupil",index=True)
    
class Pupil (models.Model):
    _inherit = 'res.users'
    
    
    isPupil = fields.Boolean()
    
    activities = fields.One2many('fctmanagement.activity','owner',string="Activity")
    tutor = fields.One2many('res.users','pupils',string="Tutor")
    company = fields.One2many('res.partner','pupils',string="FCT Partner")
    
class FCTPartner (models.Model):
    _inherit = 'res.partner'
    
    isFCTPartner = fields.Boolean()
    
    pupils = fields.Many2one('res.users',ondelete='set null',string="Pupil",index=True)

class Activity (models.Model):
    _name = 'fctmanagement.activity'
    
    owner = field.Many2one('res.users',ondelete='set null',string="Pupil",index=True)
    
    date = fields.Date()
    description = fields.Char(string='Description')
    duration = fields.Float()
    remarks = fields.Char(string='Remarks')
    
    @api.constrains('duration')
    def _duration_lessorequal_to_eight_hours(self):
        for r in self:
            if self.duration >8:
                raise exceptions.ValidationError("Activity duration can not exceed 8 hours")
            
#    @api.constrains('duration')
#    def _duration_perday_lessorequal_to_eight(self):
#    
#    @api.constrains('')
#    def _duration_total_per_pupil_less_than_350(self):
        