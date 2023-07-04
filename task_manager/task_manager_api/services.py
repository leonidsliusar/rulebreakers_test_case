from django.db.models import QuerySet
from django.shortcuts import get_object_or_404

from .models import Task


def retrieve_posts_list(filter_str: str = 'all') -> QuerySet:
    match filter_str:
        case 'done':
            query = Task.objects.filter(completed=True)
        case 'undone':
            query = Task.objects.filter(completed=False)
        case _:
            query = Task.objects.all()
    return query


def create_post(data: dict) -> Task:
    task = Task.objects.create(**data)
    return task


def retrieve_post(task_id: int) -> Task:
    task = get_object_or_404(Task, pk=task_id)
    return task


def update_post(task_id: int, data: dict) -> int:
    update_count = Task.objects.filter(pk=task_id).update(**data)
    return update_count


def remove_post(task_id: int) -> tuple:
    delete_count = Task.objects.filter(pk=task_id).delete()
    return delete_count
