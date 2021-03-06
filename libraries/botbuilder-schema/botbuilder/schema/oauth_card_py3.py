# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class OAuthCard(Model):
    """A card representing a request to peform a sign in via OAuth.

    :param text: Text for signin request
    :type text: str
    :param connection_name: The name of the registered connection
    :type connection_name: str
    :param buttons: Action to use to perform signin
    :type buttons: list[~botframework.connector.models.CardAction]
    """

    _attribute_map = {
        'text': {'key': 'text', 'type': 'str'},
        'connection_name': {'key': 'connectionName', 'type': 'str'},
        'buttons': {'key': 'buttons', 'type': '[CardAction]'},
    }

    def __init__(self, *, text: str=None, connection_name: str=None, buttons=None, **kwargs) -> None:
        super(OAuthCard, self).__init__(**kwargs)
        self.text = text
        self.connection_name = connection_name
        self.buttons = buttons
