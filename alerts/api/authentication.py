# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from events.models import DApp, Alert
from constants import DJANGO_AUTH_CODE_HEADER


class AuthCodeAuthentication(BaseAuthentication):

    def authenticate(self, request):
        auth_code = request.META.get(DJANGO_AUTH_CODE_HEADER)
        if auth_code:
            try:
                dapp = DApp.objects.get(authentication_code=auth_code)
                return dapp.user, dapp
            except DApp.DoesNotExist:
                raise AuthenticationFailed('Forbidden')
        else:
            raise AuthenticationFailed('Forbidden')


class AlertOwnerAuthentication(AuthCodeAuthentication):

    def authenticate(self, request):
        user, dapp = super(AlertOwnerAuthentication, self).authenticate(request)
        contract = request.data.get('contract')
        if contract:
            try:
                # The contract related alert must be owned by auth-code user
                alert = Alert.objects.get(dapp__authentication_code=dapp.authentication_code, contract=contract)
                return dapp.user, dapp
            except Alert.DoesNotExist:
                raise AuthenticationFailed('Forbidden')
        else:
            raise AuthenticationFailed('Forbidden')