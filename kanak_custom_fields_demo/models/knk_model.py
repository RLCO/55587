# -*- coding: utf-8 -*-
# Powered by Kanak Infosystems LLP.
# © 2020 Kanak Infosystems LLP. (<https://www.kanakinfosystems.com>)

from odoo import fields, models


class CustomModel(models.Model):
    _name = 'custom.model'
    _description = "Custome Model"
    _rec_name = 'knk_name'

    knk_name = fields.Char(string='Name')
    knk_roll_no = fields.Integer(string='Roll No')
    knk_partner = fields.Many2one('res.partner', string='Partner')
    knk_city_details = fields.One2many('custom.model.lines', 'knk_custom_inverse_field', string='City Details')
    knk_attendee_ids = fields.Many2many('hr.employee', string='Attendees')
    knk_attachment_ids = fields.Many2many('ir.attachment', string='Attachments')


class CustomModelLines(models.Model):
    _name = 'custom.model.lines'
    _description = "Custome Model Lines"
    _rec_name = 'knk_city'

    knk_city = fields.Char(string='City')
    knk_pincode = fields.Integer(string='Pincode')
    knk_custom_inverse_field = fields.Many2one('custom.model', string='Inverse')
