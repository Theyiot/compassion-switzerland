##############################################################################
#
#    Copyright (C) 2020 Compassion CH (http://www.compassion.ch)
#    @author: Théo Nikles <theo.nikles@gmail.com>
#
#    The licence is in the file __manifest__.py
#
##############################################################################
from odoo import models


class ThemeMuskathlon(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_muskathlon_post_copy(self, mod):
        self.disable_view('website_theme_install.customize_modal')
