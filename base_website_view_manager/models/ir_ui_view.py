# -*- coding: utf-8 -*-
# Python source code encoding : https://www.python.org/dev/peps/pep-0263/
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    This module copyright :
#        (c) 2015 Antiun Ingenieria, SL (Madrid, Spain, http://www.antiun.com)
#                 Antonio Espinosa <antonioea@antiun.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import models, fields, api

import logging
from pprint import pprint, pformat
import traceback
_logger = logging.getLogger(__name__)


class IrUiView(models.Model):
    _inherit = 'ir.ui.view'

    noupdate = fields.Boolean(string='No update', compute='_noupdate_get',
                              inverse='_noupdate_set')

    @api.one
    def _noupdate_get(self):
        noupdate = False
        if self.xml_id:
            module, name = self.xml_id.split('.')
            data_obj = self.env['ir.model.data'].search([
                ('model', '=', 'ir.ui.view'), ('module', '=', module),
                ('name', '=', name)])
            _logger.info('_noupdate_get: data_obj = ' + pformat(data_obj))
            _logger.info('_noupdate_get: data_obj.noupdate = ' + pformat(data_obj.noupdate))
            noupdate = data_obj.noupdate or False
        self.noupdate = noupdate
        _logger.info('_noupdate_get: noupdate = ' + pformat(self.noupdate))

    @api.one
    def _noupdate_set(self):
        _logger.info('_noupdate_set: noupdate = ' + pformat(self.noupdate))
