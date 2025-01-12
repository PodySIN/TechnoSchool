from uuid import uuid4
from django.db import models


class Questions(models.Model):
    Number = models.IntegerField(
        default=1,
        help_text="Номер задания.",
        verbose_name="Номер",
    )
    Topic = models.CharField(
        default="Разное",
        max_length=512,
        help_text="Название задания.",
        verbose_name="Название задания",
    )

    def __str__(self):
        return f"№{self.Number}. {self.Topic}"

    class Meta:
        db_table = "Questions"
        verbose_name = "Номер задания"
        verbose_name_plural = "Номера заданий"
        ordering = ["Number", "id"]


class Topics(models.Model):
    question = models.ForeignKey(
        "Questions",
        on_delete=models.CASCADE,
        default=None,
        related_name="topics",
        help_text="К какому номеру задания эта тема принадлежит.",
        verbose_name="Тема какого задания",
    )
    Topic = models.CharField(
        default="Разное",
        max_length=512,
        help_text="Тема задания.",
        verbose_name="Тема",
    )

    def __str__(self):
        return f"{self.question}. {self.Topic}."

    class Meta:
        db_table = "Topics"
        verbose_name = "Тема задания"
        verbose_name_plural = "Темы заданий"
        ordering = ["question", "id"]


class PrototypeTasks(models.Model):
    """
    Модель заданий
    """

    Image = models.ImageField(
        upload_to="task_images/",
        height_field=None,
        width_field=None,
        max_length=2048,
        default=None,
        help_text="Изображение прилагаемое для выполнения задания.",
        verbose_name="Изображение",
        blank=True,
    )
    Number = models.ForeignKey(
        "Questions",
        on_delete=models.CASCADE,
        help_text="Номер задания.",
        verbose_name="Номер",
        default=1,
    )
    Topic = models.ForeignKey(
        "Topics",
        on_delete=models.CASCADE,
        help_text="Тема задания.",
        verbose_name="Тема",
        default=1,
    )
    time_create = models.DateTimeField(
        blank=True,
        auto_now_add=True,
        verbose_name="Время создания",
        help_text="Время создания задания",
    )
    time_update = models.DateTimeField(
        blank=True,
        auto_now=True,
        verbose_name="Время изменения",
        help_text="Время изменения задания",
    )
    Condition = models.CharField(
        default="",
        max_length=2048,
        help_text="Условие задачи, которое видят ученики.",
        verbose_name="Условие",
    )
    SourceTask = models.ForeignKey(
        "SourceTasks",
        default=1,
        related_name="PrototypeTasks",
        on_delete=models.CASCADE,
        help_text="Указание, прототипом какого задания является эта задача.",
        verbose_name="Прототип какого задания",
    )

    def save(self, *args, **kwargs):
        if self.Image:
            ext = self.Image.name.split(".")[-1]
            filename = f"{self.Topic}_{uuid4().hex}_{uuid4().hex}.{ext}"
            self.Image.name = filename
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.Number} {self.Topic}"

    class Meta:
        db_table = "PrototypeTasks"
        verbose_name = "Прототип задания"
        verbose_name_plural = "Прототипы заданий"
        ordering = ["id"]


class SourceTasks(models.Model):
    Image = models.ImageField(
        upload_to="task_images/",
        height_field=None,
        width_field=None,
        max_length=512,
        default=None,
        help_text="Изображение прилагаемое для выполнения задания.",
        verbose_name="Изображение",
        blank=True,
    )
    Video = models.ImageField(
        upload_to="task_videos/",
        height_field=None,
        width_field=None,
        max_length=512,
        default=None,
        help_text="Видео-решение задания.",
        verbose_name="Видео-решение",
        blank=True,
    )
    Solution = models.ImageField(
        upload_to="task_solutions/",
        height_field=None,
        width_field=None,
        max_length=512,
        default=None,
        help_text="Письменное решение задания(изображение).",
        verbose_name="Письменное решение",
        blank=True,
    )
    time_create = models.DateTimeField(
        blank=True,
        auto_now_add=True,
        verbose_name="Время создания",
        help_text="Время создания задания",
    )
    time_update = models.DateTimeField(
        blank=True,
        auto_now=True,
        verbose_name="Время изменения",
        help_text="Время изменения задания",
    )
    Number = models.ForeignKey(
        "Questions",
        on_delete=models.CASCADE,
        help_text="Номер задания.",
        verbose_name="Номер",
        default=1,
    )
    Topic = models.ForeignKey(
        "Topics",
        on_delete=models.CASCADE,
        help_text="Тема задания.",
        verbose_name="Тема",
        default=1,
    )
    Condition = models.CharField(
        default="",
        max_length=2048,
        help_text="Условие задания, использующееся для генерации(выделять изменяемые числа пор типу: @A@.",
        verbose_name="Условие для генерации",
        blank=True,
    )
    Condition_for_students = models.CharField(
        default="",
        max_length=2048,
        help_text="Условие, которое будут видеть ученики.",
        verbose_name="Условие для учеников",
    )

    def save(self, *args, **kwargs):
        if self.Image:
            ext = self.Image.name.split(".")[-1]
            filename = f"{self.Topic}_{uuid4().hex}_{uuid4().hex}.{ext}"
            self.Image.name = filename
        if self.Video:
            ext = self.Video.name.split(".")[-1]
            filename = f"{self.Topic}_{uuid4().hex}_{uuid4().hex}.{ext}"
            self.Video.name = filename
        if self.Solution:
            ext = self.Solution.name.split(".")[-1]
            filename = f"{self.Topic}_{uuid4().hex}_{uuid4().hex}.{ext}"
            self.Solution.name = filename
        super().save(*args, **kwargs)

    def __str__(self):
        first_five_words = " ".join(str(self.Condition_for_students).split(" ")[:6])
        return f"{self.Topic} ({self.id}) ({first_five_words}...)."

    class Meta:
        db_table = "SourceTasks"
        verbose_name = "Шаблон задания"
        verbose_name_plural = "Шаблоны заданий"
        ordering = ["id"]


class Formulas(models.Model):
    Formula = models.CharField(
        default="",
        max_length=2048,
        help_text="Формула для генерации задания (шаг решения, если их несколько, добавьте поля).",
        verbose_name="Шаг решения",
    )
    Task = models.ForeignKey(
        "SourceTasks",
        on_delete=models.CASCADE,
        default=None,
        related_name="formulas",
        help_text="Указание, для какого задания используется эта формула.",
        verbose_name="Для какого дания формула",
    )

    def __str__(self):
        return f"{self.Formula} | ({self.Task})."

    class Meta:
        db_table = "Formulas"
        verbose_name = "Шаги решения заданий"
        verbose_name_plural = "Шаги решения"
        ordering = ["id"]


class SourceAnswers(models.Model):
    Answer = models.CharField(
        default="",
        max_length=2048,
        help_text="Ответ на задание(если ответов несколько, добавьте поля).",
        verbose_name="Ответ",
    )
    Task = models.ForeignKey(
        "SourceTasks",
        on_delete=models.CASCADE,
        default=None,
        related_name="answers",
        help_text="Указание, к какому заданию относится этот ответ.",
        verbose_name="Ответ задания",
    )

    def __str__(self):
        return f"{self.Answer} | ({self.Task})."

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    class Meta:
        db_table = "SourceAnswers"
        verbose_name = "Ответы для шаблонов"
        verbose_name_plural = "Ответы для шаблонов"
        ordering = ["id"]


class PrototypeAnswers(models.Model):
    Answer = models.CharField(
        default="",
        max_length=2048,
        help_text="Ответ на задание(если ответов несколько, добавьте поля).",
        verbose_name="Ответ",
    )
    Task = models.ForeignKey(
        "PrototypeTasks",
        on_delete=models.CASCADE,
        default=None,
        related_name="answers",
        help_text="Указание, к какому заданию относится этот ответ.",
        verbose_name="Ответ задания",
    )

    def __str__(self):
        return f"{self.Answer} | ({self.Task})."

    class Meta:
        db_table = "PrototypeAnswers"
        verbose_name = "Ответы для задания"
        verbose_name_plural = "Ответы для заданий"
        ordering = ["id"]


class SourceTasksVariables(models.Model):
    Task = models.ForeignKey(
        "SourceTasks",
        on_delete=models.CASCADE,
        default=None,
        related_name="variables",
        help_text="Указание, к какому заданию относится этот ответ.",
        verbose_name="Ответ задания",
    )
    Start = models.FloatField(
        default=1,
        help_text="Начало диапазона, в котором будут перебираться числа",
        verbose_name="Начало диапазона",
    )
    End = models.FloatField(
        default=1,
        help_text="Конец диапазона, в котором будут перебираться числа (включительно)",
        verbose_name="Конец диапазона",
    )
    Step = models.FloatField(
        default=1,
        help_text="Шаг, который будет перебираться для генерации заданий.",
        verbose_name="Шаг",
    )

    def __str__(self):
        return f"{self.Start}, {self.End}, {self.Step} | ({self.Task})."

    class Meta:
        db_table = "SourceTasksVariables"
        verbose_name = "Переменная для задания"
        verbose_name_plural = "Переменная для заданий"
        ordering = ["id"]


class StartVariablesLimitations(models.Model):
    Limitation = models.CharField(
        default="",
        max_length=2048,
        help_text="Ограничения задания, которое помогает генерировать задания(если ограничений несколько, добавьте поля).",
        verbose_name="Ограничения для начальных переменных.",
    )
    Task = models.ForeignKey(
        "SourceTasks",
        on_delete=models.CASCADE,
        default=None,
        related_name="start_limitations",
        help_text="Указание, к какому заданию относится это ограничение.",
        verbose_name="Ограничение задания",
    )

    def __str__(self):
        return f"{self.Limitation} | ({self.Task})."

    class Meta:
        db_table = "StartVariablesLimitations"
        verbose_name = "Ограничение для изменяемых переменных задания"
        verbose_name_plural = "Ограничения для изменяемых переменных заданий"
        ordering = ["id"]


class FollowingVariablesLimitations(models.Model):
    Limitation = models.CharField(
        default="",
        max_length=2048,
        help_text="Ограничения переменных, использующихся в ходе решения задания, а также ограничения для ответа.",
        verbose_name="Ограничения для переменных в шагах решения, а также для ответа.",
    )
    Task = models.ForeignKey(
        "SourceTasks",
        on_delete=models.CASCADE,
        default=None,
        related_name="following_limitations",
        help_text="Указание, к какому заданию относится это ограничение.",
        verbose_name="Ограничение задания",
    )

    def __str__(self):
        return f"{self.Limitation} | ({self.Task})."

    class Meta:
        db_table = "FollowingVariablesLimitations"
        verbose_name = "Ограничение для последующих переменных задания"
        verbose_name_plural = "Ограничения для последующих переменных заданий"
        ordering = ["id"]
