# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import timedelta
from odoo.exceptions import ValidationError

class Course (models.Model):
    _name = 'openacademy.course'
    
    name = fields.Char(string='Title',required=True)
    description = fields.Text()
    
    responsible_id = fields.Many2one('res.users',ondelete='set null', string="Responsible",index=True)
    session_ids=fields.One2many('openacademy.session','course_id',string="Sessions")
    
    
class Session (models.Model):
    _name = 'openacademy.session'
    
    name = fields.Char (required=True)
    start_date = fields.Date(default=fields.Date.today)
    end_date = fields.Date(compute='_get_end_date')
    duration = fields.Float(digits=(6,2),help="Duration in days")
    seats = fields.Integer(string="Number of seats")
    active = fields.Boolean(default=True)
    
    instructor_id=fields.Many2one('res.partner',string="Instructor")
    course_id=fields.Many2one('openacademy.course',ondelete='cascade',string="Course",required=True)
    attendee_ids = fields.Many2many('res.partner',string= "Attendees")
    
    taken_seats = fields.Float(string="Taken seats", compute='_taken_seats')
    
    @api.depends('seats','attendee_ids')
    def _taken_seats(self):
        for r in self:
            if not r.seats:
                r.taken_seats = 0.0
            else:
                r.taken_seats = 100.0 * len(r.attendee_ids) / r.seats
                
    @api.onchange('seats', 'attendee_ids')
    def _verify_valid_seats(self):
        if self.seats <0:
            return{
                'warning':{
                    'title':"Incorrect 'seats' value",
                    'message': "The number of available seats my note be negative"
                },
            }
        if self.seats < len(self.attendee_ids):
            return{
                'warning':{
                    'title': "Too many attendees",
                    'message': "Increase seats or remove excess attendees"
                }
            }
            
    @api.constrains('instructor_id','attendee_ids')
    def _check_instructor_not_in_attendees(self):
        for r in self:
            if r.instructor_id and r.instructor_id in r.attendee_ids:
                raise exceptions.ValidationError("A session's instructor can't be an attendee")

    @api.depends('start_date','duration')
    def _get_end_time(self):
        for r in self:
            if not (r.start_date and r.duration):
                r.end_date = r.start_date
                continue
            start = fields.Datetime.from_string(r.start_date)
            duration = timedelta(days=r.duration, seconds=-1)
            r.end_date = start + duration
#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100