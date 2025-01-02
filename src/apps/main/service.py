"""
Модуль, который отвечает за базовые функции, которые используются во всех приложениях на сайте.
"""

from apps.main.configure import configure_logging

logger = configure_logging()


def get_base_context(Title: str) -> dict:
    """
    Позволяет вернуть словарь с информацией.
    :param Title: Заголовок сайта.
    :return: словарь с информацией.
    """
    context = {
        "Title": Title,
    }
    return context


def get_all_objects_from_model(Model):
    """
    Позволяет получить все объекты из модели.
    """
    logger.info(f"Получаем все объекты из модели: {Model}")
    return Model.objects.all()


def get_objects_from_model_by_filter(Model, *args, **kwargs):
    """
    Позволяет получить все объекты которые удовлетворяют фильтрам
    """
    logger.info(f"Получаем все объекты по фильтрам из модели: {Model}")
    return Model.objects.filter(*args, **kwargs)


def get_object_from_model_by_info(Model, *args, **kwargs):
    """
    позволяет получить конкретный объект из модели по определенной информации.
    """
    logger.info(f"Получаем объект по информации из модели: {Model}")
    return Model.objects.get(*args, **kwargs)
