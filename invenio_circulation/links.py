# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 CERN.
# Copyright (C) 2018 RERO.
#
# Invenio-Circulation is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

"""Links for record serialization."""

from flask import current_app

from .api import Loan
from .views import build_url_action_for_pid


def loan_links_factory(pid, record=None):
    """Factory for links generation."""
    links = {}
    record = record or Loan.get_record(pid.object_uuid)
    available_actions = {}
    transitions_config = current_app.config.get(
        'CIRCULATION_LOAN_TRANSITIONS', {}
    )
    for transition in transitions_config.get(record['state']):
        action = transition.get('trigger', 'next')
        available_actions[action] = build_url_action_for_pid(pid, action)
    links.setdefault('available_actions', available_actions)
    return links
