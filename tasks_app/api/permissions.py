from rest_framework.permissions import BasePermission

    
class IsBoardMemberOrOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        return (obj.board.owner == request.user or
                obj.board.members.filter(id=request.user.id).exists() or
                request.user.is_superuser)
    

class IsTaskOwnerOrBoardOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method == "DELETE":
            return (
                obj.owner == request.user or
                obj.board.owner == request.user or
                request.user.is_superuser
            )
        return True
    
    
class IsCommentAuthor(BasePermission):
 
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
