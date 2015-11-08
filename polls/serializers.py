__author__ = 'zhangle0013'
from polls.models import OUsers
from rest_framework import serializers


class OUsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OUsers
        fields = ('uLogName',
                  'uPassword',
                  'uRealName',
                  'uAcronyName',
                  'uSpellName',
                  'uFirstName',
                  'uLastName',
                  'uIsDel',
                  'uThumbnailSmall',
                  'uThumbnail',
                  'uIsFirst',
                  'uEmail',
                  'uPhone',
                  'uQQ',
                  'uBirthday',
                  'uEntryDate',
                  'uLeaveDate',
                  'uIdentity',
                  'uGender',
                  'uDepartment',
                  'uDuty',
                  'uLevel',
                  'uDutyStatus',
                  'uWage',
                  'uRemark',)