from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        # Make sure that the current user is the owner (only the owner can change the post)
        return request.user == obj.user


class AllowAny(BasePermission):
    def has_obj_permission(self, request, view, obj):
        pass


class AllowedToLikePost(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Make sure that the current user is not the object(post) owner (One cann't like her own post)
        return request.user != obj.user
    