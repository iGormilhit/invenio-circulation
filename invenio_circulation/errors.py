# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 CERN.
# Copyright (C) 2018 RERO.
#
# Invenio-Circulation is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

"""Circulation exceptions."""


class CirculationException(Exception):
    """Exceptions raised by circulation module."""

    def __init__(self, msg):
        """."""
        self.msg = msg


class InvalidState(CirculationException):
    """State not found in circulation configuration."""


class ItemNotAvailable(CirculationException):
    """Exception raised from action on unavailable item."""


class TransitionConditionsFailed(CirculationException):
    """Conditions for the transition failed at loan state."""


class NoValidTransitionAvailable(CirculationException):
    """Exception raised when all transitions conditions failed."""


class LoanActionError(CirculationException):
    """."""


class InvalidCirculationPermission(CirculationException):
    """Raised when permissions are not satisfied for transition."""


class TransitionConstraintsViolation(CirculationException):
    """Exception raised when constraints for the transition failed."""
