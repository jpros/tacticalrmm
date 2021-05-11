from rest_framework import permissions

from tacticalrmm.permissions import _has_perm


class ManageWinSvcsPerms(permissions.BasePermission):
    def has_permission(self, r, view):
        return _has_perm(r, "can_manage_winsvcs")
