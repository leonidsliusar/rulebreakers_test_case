from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import TaskSerializer, TaskResponseSerializer, TaskUpdateSerializer
from .services import retrieve_posts_list, retrieve_post, update_post, remove_post, create_post


class ListTaskView(APIView):
    serializer_class = TaskSerializer, TaskResponseSerializer

    @swagger_auto_schema(responses={200: TaskResponseSerializer})
    def get(self, request):
        task_list = retrieve_posts_list()
        if not task_list:
            return Response({'error': 'Tasks doesn\'t exists'}, status=status.HTTP_404_NOT_FOUND)
        serializer = TaskResponseSerializer(task_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=TaskSerializer, responses={200: TaskResponseSerializer})
    def post(self, request):
        serializer = TaskSerializer(data=request.data, many=False)
        if serializer.is_valid():
            task = create_post(request.data)
            TaskResponseSerializer(task, many=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.get_example, status=status.HTTP_400_BAD_REQUEST)


class ListTaskViewFilter(APIView):
    serializer_class = TaskSerializer, TaskResponseSerializer

    @swagger_auto_schema(responses={200: TaskResponseSerializer})
    def get(self, request, filter_str: str = 'all'):
        task_list = retrieve_posts_list(filter_str)
        if not task_list:
            return Response({'error': 'Tasks doesn\'t exists'}, status=status.HTTP_404_NOT_FOUND)
        serializer = TaskResponseSerializer(task_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DetailTaskView(APIView):
    serializer_class = TaskSerializer, TaskResponseSerializer, TaskUpdateSerializer

    @swagger_auto_schema(responses={200: TaskResponseSerializer})
    def get(self, request, task_id: int):
        task = retrieve_post(task_id)
        if not task:
            return Response({'error': 'Task doesn\'t exists'}, status=status.HTTP_404_NOT_FOUND)
        serializer = TaskResponseSerializer(task, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=TaskUpdateSerializer)
    def put(self, request, task_id: int):
        update_count = update_post(task_id, request.data)
        if not update_count:
            return Response({'error': 'Task doesn\'t exists'}, status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_200_OK)

    def delete(self, request, task_id):
        delete_count = remove_post(task_id)
        if not delete_count[0]:
            return Response({'error': 'Task doesn\'t exists'}, status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)
