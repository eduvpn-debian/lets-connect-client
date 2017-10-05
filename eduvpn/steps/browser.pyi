# python-eduvpn-client - The GNU/Linux eduVPN client and Python API
#
# Copyright: 2017, The Commons Conservancy eduVPN Programme
# SPDX-License-Identifier: GPL-3.0+

from eduvpn.metadata import Metadata

def browser_step(builder, meta: Metadata, verifier): ...
def _phase1_background(meta: Metadata, dialog, verifier, builder): ...
def _phase1_callback(meta:  Metadata, port, code_verifier, oauth, auth_url, dialog, builder): ...
def _show_dialog(dialog, auth_url, builder): ...
def _phase2_background(meta:  Metadata, port, oauth, code_verifier, auth_url, dialog, builder): ...
def _phase2_callback(meta:  Metadata, oauth, dialog, builder): ...
