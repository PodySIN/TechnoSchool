def get_base_context(Title: str) -> dict:
    context = {
        "Title": Title,
    }
    return context


def get_all_objects_from_model(Model):
    return Model.objects.all()


def get_objects_from_model_by_filter(Model, *args, **kwargs):
    return Model.objects.filter(*args, **kwargs)
