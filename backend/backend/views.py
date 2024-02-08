from rest_framework import generics, response, status


class HomeAPIView(generics.GenericAPIView):
    """
    An endpoint for Home page
    """
    
    def post(self, request, *args, **kwargs):
        return response.Response(data=request.data, status=status.HTTP_200_OK)
    
    def get(self, request, *args, **kwargs):
        return response.Response(data=request.data, status=status.HTTP_200_OK)
