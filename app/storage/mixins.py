from rest_framework import mixins


class CreateRetrieveDestroyModelMixin(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.DestroyModelMixin):
    """
    Custom mixin for Creating, Retrieving and Destroying instances
    """
    pass
