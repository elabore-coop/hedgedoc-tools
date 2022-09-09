# Copyright 2021 Elabore ()
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Pad Hedgedoc Leads",
    "version": "12.0.1.0.0",
    "author": "Elabore",
    "maintainer": "False",
    "website": "False",
    "license": "AGPL-3",
    "category": "False",
    "summary": "Add hedgedoc pad to CRM leads",
    "description": """
   :image: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3
==================
Pad Hedgedoc Leads
==================
Add hedgedoc pad to CRM leads

Installation
============
Just install Pad Hedgedoc Leads, all dependencies will be installed by default.

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
    # any module necessary for this one to work correctly
    "depends": [
        "base",
        "pad_hedgedoc_connector",
        "crm",
    ],
    "external_dependencies": {
        "python": [],
    },
    # always loaded
    "data": [
        "security/ir.model.access.csv",
        "views/crm_lead.xml",
        "wizard/create_pad.xml",
    ],
    # only loaded in demonstration mode
    "demo": [],
    "js": [],
    "css": [],
    "qweb": [],
    "installable": True,
    # Install this module automatically if all dependency have been previously
    # and independently installed.  Used for synergetic or glue modules.
    "auto_install": False,
    "application": False,
}
