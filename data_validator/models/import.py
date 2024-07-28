# -*- coding: utf-8 -*-

import logging

from odoo import models, api

_logger = logging.getLogger(__name__)


class Import(models.TransientModel):

    _inherit = 'base_import.import'

    @api.model
    def _convert_import_data(self, fields, options):
        # Override base method
        # Called when actual import start
        data, import_fields = super(Import, self)._convert_import_data(fields, options)

        # Do something ...

        return data, import_fields

    def parse_preview(self, options, count=10):
        # Override base method
        # Called when data loaded
        preview_data = super(Import, self).parse_preview(options, count=count)

        # Do something ...

        return preview_data