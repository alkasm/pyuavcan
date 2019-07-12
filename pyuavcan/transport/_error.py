#
# Copyright (c) 2019 UAVCAN Development Team
# This software is distributed under the terms of the MIT License.
# Author: Pavel Kirienko <pavel.kirienko@zubax.com>
#


class TransportError(RuntimeError):
    """
    This is the root exception class for all transport-related errors.
    """
    pass


class InvalidTransportConfigurationError(TransportError):
    """
    The transport could not be initialized because the specified configuration is invalid.
    """
    pass


class InvalidMediaConfigurationError(InvalidTransportConfigurationError):
    """
    The transport could not be initialized because the specified media configuration is invalid.
    """
    pass


class UnsupportedSessionConfigurationError(TransportError):
    """
    The requested session configuration is not supported by this transport.
    For example, this exception would be raised if one attempted to create a unicast output for messages over
    the CAN bus transport.
    """
    pass


class OperationNotDefinedForAnonymousNodeError(TransportError):
    """
    The requested action would normally be possible, but it is currently not because the transport instance does not
    have a node ID assigned.
    """
    pass


class ResourceClosedError(TransportError):
    """
    The requested operation could not be performed because an associated resource has already been disposed.
    Double-close should not raise exceptions.
    """
    pass


class SendTimeoutError(TransportError):
    """
    The media has taken too long to transmit the frame and is probably malfunctioning.
    """
    pass