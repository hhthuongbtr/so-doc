from typing import Mapping
from django_cas_ng.backends import CASBackend
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.models import User
from accounts.models import CustomUser
from django.http import HttpRequest
import logging
import json

logger = logging.getLogger("console")
class MyCASBackend(CASBackend):
    def configure_user(self, user: User) -> User:
        """
        Configures a user after creation and returns the updated user.

        This method is called immediately after a new user is created,
        and can be used to perform custom setup actions.

        :param user: User object.

        :returns: [User] The user object. By default, returns the user unmodified.
        """
        return user
    def bad_attributes_reject(self,
                              request: HttpRequest,
                              username: str,
                              attributes: Mapping[str, str]) -> bool:
        """
        Rejects a user if the returned username/attributes are not OK.
        :returns: [boolean] ``True/False``. Default is ``False``.

        """
        try:
            cas_profile_string = attributes.get('profile')
            cas_profile = json.loads(cas_profile_string)
            logger.debug(cas_profile_string)
            uid = CustomUser.objects.get(username=username)
            change_flag = False
            if 'divisionCode' in cas_profile_string and uid.division_code != cas_profile['divisionCode']:
                uid.division_code = cas_profile['divisionCode']
                change_flag = True
                logger.info("%s change divisionCode from %s to %s"%(username, uid.division_code, cas_profile['divisionCode']))
            if 'teamCode' in cas_profile_string and uid.team_code != cas_profile['teamCode']:
                uid.team_code = cas_profile['teamCode']
                change_flag = True
                logger.info("%s change teamCode from %s to %s"%(username, uid.team_code, cas_profile['teamCode']))
            if 'departmentCode' in cas_profile_string and uid.department != cas_profile['departmentCode']:
                uid.department = cas_profile['departmentCode']
                change_flag = True
                logger.info("%s change departmentCode from %s to %s"%(username, uid.department, cas_profile['departmentCode']))
            if 'mobilePhone' in cas_profile_string and uid.mobile_phone != cas_profile['mobilePhone']:
                uid.mobile_phone = cas_profile['mobilePhone']
                change_flag = True
                logger.info("%s change mobilePhone from %s to %s"%(username, uid.mobile_phone, cas_profile['mobilePhone']))
            if change_flag:
                uid.save()
        except Exception as e:
            logger.error(e)
        return False
