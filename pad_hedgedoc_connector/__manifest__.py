# -*- coding: utf-8 -*-
{
    "name": "Pad Hedgedoc Connector",
    "category": "Notes",
    "version": "13.0.1.0.0",
    "summary": "Connect Odoo to Hedgedoc server",
    "author": "Elabore",
    "website": "https://elabore.coop/",
    "installable": True,
    "application": True,
    "auto_install": False,
    "description": """
======================
Pad Hedgedoc Connector
======================
This module provides the capacity to link Odoo to a Hedgedoc instance in order to generate and manage Hedgedoc documents

Installation
============
Just install pad_hedgedoc_connector, all dependencies will be installed by default.
On your Hedgedoc server, the parameter CMD_ALLOW_FREEURL must be set to True

Known issues / Roadmap
======================

Bug Tracker
===========
Bugs are tracked on `GitHub Issues
<https://github.com/elabore-coop/pad-tools/issues>`_. In case of trouble, please
check there if your issue has already been reported. If you spotted it first,
help us smashing it by providing a detailed and welcomed feedback.

Credits
=======

Images
------
* Elabore: `Icon <https://elabore.coop/web/image/res.company/1/logo?unique=f3db262>`_.

Contributors
------------
* Stéphan Sainléger <https://github.com/stephansainleger>

Funders
-------
The development of this module has been financially supported by:
* Elabore (https://elabore.coop)

Maintainer
----------
This module is maintained by ELABORE.

""",
    "depends": [
        "base",
        "base_setup",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/res_config_settings_view.xml",
        "wizard/create_pad.xml",
    ],
    "qweb": [],
}
