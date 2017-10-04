# python-eduvpn-client - The GNU/Linux eduVPN client and Python API
#
# Copyright: 2017, The Commons Conservancy eduVPN Programme
# SPDX-License-Identifier: GPL-3.0+

from nacl.signing import VerifyKey


def translate_display_name(display_name): ...
def get_instances(discovery_uri, verifier: VerifyKey): ...
def get_instance_info(instance_uri, verifier: VerifyKey): ...
def create_keypair(oauth, api_base_uri): ...
def list_profiles(oauth, api_base_uri): ...
def user_info(oauth, api_base_uri): ...
def user_messages(oauth, api_base_uri): ...
def system_messages(oauth, api_base_uri): ...
def create_config(oauth, api_base_uri, display_name, profile_id): ...
def get_profile_config(oauth, api_base_uri, profile_id): ...
def get_auth_url(oauth, code_verifier, auth_endpoint): ...
