#coding:utf-8
#date:2020/5/1110:25
#author:CQ_Liu

from rest_framework import permissions

class IsUserOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
    # Read permissions are allowed to any request,
#   so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
    # Instance must have an attribute named `owner`.
    # obj相当于数据库中的model，这里要把owner改为我们数据库中的user
        return obj.user == request.user