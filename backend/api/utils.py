from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from api.serializers import RecipeShowSerializer
from recipes.models import Recipe


def add_or_delete_object_model(self, model, pk, serializer, errors):
    recipe = get_object_or_404(Recipe, id=pk)
    serializer = serializer(
        data={
            'user': self.request.user.id,
            'recipe': recipe.id
        }
    )
    if self.request.method == 'POST':
        serializer.is_valid(raise_exception=True)
        serializer.save()
        serializer = RecipeShowSerializer(recipe)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    objects = model.objects.filter(user=self.request.user, recipe=recipe)
    if not objects.exists():
        return Response(
            {'errors': errors},
            status=status.HTTP_400_BAD_REQUEST
        )
    objects.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
