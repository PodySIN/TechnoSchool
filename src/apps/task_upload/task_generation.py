import string
import time
import mpmath
import numpy as np

from apps.task_upload.models import PrototypeTasks

from apps.task_upload.models import PrototypeAnswers


def get_alphabet() -> str:
    return string.ascii_uppercase + "0123456789"


class GenerateTask:
    def __init__(self, task):
        self.task = task
        self.all_conditions = self.get_all_conditions()
        self.max_tasks = 50

    def get_all_conditions(self):
        raw_all_conditions = PrototypeTasks.objects.values_list("Condition")
        all_conditions = []
        for condition in raw_all_conditions:
            all_conditions.append(condition[0])
        return all_conditions

    def get_start_limitations(self):
        start_limitations = [i.Limitation for i in self.task.start_limitations.all()]
        new_limitations = []
        for limit in start_limitations:
            limit = (
                limit.replace("^", "**")
                .replace("log", "math.log")
                .replace("cos", "mpmath.cos")
                .replace("ctg", "mpmath.cot")
                .replace("tg", "mpmath.tan")
                .replace("sin", "mpmath.sin")
            )
            new_limitations.append(limit)
        if len(new_limitations) == 0:
            return "True"
        return " and ".join(new_limitations)

    def get_following_limitations(self):
        following_limitations = [i.Limitation for i in self.task.following_limitations.all()]
        new_limitations = []
        for limit in following_limitations:
            limit = (
                limit.replace("^", "**")
                .replace("log", "math.log")
                .replace("cos", "mpmath.cos")
                .replace("ctg", "mpmath.cot")
                .replace("tg", "mpmath.tan")
                .replace("sin", "mpmath.sin")
            )
            new_limitations.append(limit)
        if len(new_limitations) == 0:
            return "True"
        return " and ".join(new_limitations)

    def get_amount_of_tasks(self):
        return len(PrototypeTasks.objects.filter(SourceTask_id=self.task.id))

    def get_condition(self):
        return self.task.Condition

    def get_variables_data(self):
        return [[i.Start, i.End, i.Step] for i in self.task.variables.all()]

    def get_all_formulas(self):
        formulas = [i.Formula for i in self.task.formulas.all()]
        new_formulas = []
        for formula in formulas:
            formula = (
                formula.replace("^", "**")
                .replace("log", "math.log")
                .replace("cos", "mpmath.cos")
                .replace("ctg", "mpmath.cot")
                .replace("tg", "mpmath.tan")
                .replace("sin", "mpmath.sin")
            )
            new_formulas.append(formula)
        return new_formulas

    def get_formulas(self):
        formulas = self.get_all_formulas()[0 : len(self.get_all_formulas()) - 1]
        formulas = "\n".join(formulas)
        return formulas

    def get_answer_formula(self):
        return self.get_all_formulas()[-1]

    def get_variables(self):
        variables = []
        split_condition = self.get_condition().split("@")
        for sentence in split_condition:
            k = 0
            available_symbols = get_alphabet()
            for symbol in sentence:
                if symbol in available_symbols:
                    k += 1
            if k == len(sentence):
                variables.append(sentence)
        return variables

    def choose_generate(self):
        if self.get_amount_of_tasks() < self.max_tasks:
            variables = self.get_variables()
            if len(variables) == 1:
                self.generate_with_one_variable()
            elif len(variables) == 2:
                self.generate_with_two_variables()
            elif len(variables) == 3:
                self.generate_with_three_variables()
            elif len(variables) == 4:
                self.generate_with_four_variables()
            elif len(variables) == 5:
                self.generate_with_five_variables()
        else:
            return 0

    def generate_with_one_variable(self):
        variables = self.get_variables()
        task_variables = self.get_variables_data()
        amount_of_tasks = self.get_amount_of_tasks()
        for i in np.arange(task_variables[0][0], task_variables[0][1], task_variables[0][2]):
            i = round(i, 4)
            if amount_of_tasks >= self.max_tasks:
                break
            exec(variables[0] + "=" + str(i))
            if eval(self.get_start_limitations()):
                try:
                    exec(self.get_formulas())
                    ANSWER = eval(self.get_answer_formula())
                    ANSWER = round(ANSWER, 4)
                except:
                    ANSWER = "ERROR"
                if ANSWER != "ERROR":
                    if eval(self.get_following_limitations()):
                        if isinstance(ANSWER, float):
                            if len(str(ANSWER).split(".")[-1]) <= 4:
                                amount_of_tasks += 1
                                self.add_task_to_db(i, ANSWER)
                        else:
                            amount_of_tasks += 1
                            self.add_task_to_db(i, ANSWER)

    def generate_with_two_variables(self):
        variables = self.get_variables()
        task_variables = self.get_variables_data()
        amount_of_tasks = self.get_amount_of_tasks()
        for i in np.arange(task_variables[0][0], task_variables[0][1], task_variables[0][2]):
            i = round(i, 4)
            if amount_of_tasks >= self.max_tasks:
                break
            exec(variables[0] + "=" + str(i))
            for j in np.arange(task_variables[1][0], task_variables[1][1], task_variables[1][2]):
                j = round(j, 4)
                if amount_of_tasks >= self.max_tasks:
                    break
                exec(variables[1] + "=" + str(j))
                if eval(self.get_start_limitations()):
                    try:
                        exec(self.get_formulas())
                        ANSWER = eval(self.get_answer_formula())
                        ANSWER = round(ANSWER, 4)
                    except:
                        ANSWER = "ERROR"
                    if ANSWER != "ERROR":
                        if eval(self.get_following_limitations()):
                            if isinstance(ANSWER, float):
                                if len(str(ANSWER).split(".")[-1]) <= 4:
                                    amount_of_tasks += 1
                                    self.add_task_to_db(i, j, ANSWER)
                            else:
                                amount_of_tasks += 1
                                self.add_task_to_db(i, j, ANSWER)

    def generate_with_three_variables(self):
        variables = self.get_variables()
        task_variables = self.get_variables_data()
        amount_of_tasks = self.get_amount_of_tasks()
        for i in np.arange(task_variables[0][0], task_variables[0][1], task_variables[0][2]):
            i = round(i, 4)
            if amount_of_tasks >= self.max_tasks:
                break
            exec(variables[0] + "=" + str(i))
            for j in np.arange(task_variables[1][0], task_variables[1][1], task_variables[1][2]):
                j = round(j, 4)
                if amount_of_tasks >= self.max_tasks:
                    break
                exec(variables[1] + "=" + str(j))
                for k in np.arange(
                    task_variables[2][0], task_variables[2][1], task_variables[2][2]
                ):
                    k = round(k, 4)
                    if amount_of_tasks >= self.max_tasks:
                        break
                    exec(variables[2] + "=" + str(k))
                    if eval(self.get_start_limitations()):
                        try:
                            exec(self.get_formulas())
                            ANSWER = eval(self.get_answer_formula())
                            ANSWER = round(ANSWER, 4)
                        except:
                            ANSWER = "ERROR"
                        if ANSWER != "ERROR":
                            if eval(self.get_following_limitations()):
                                if isinstance(ANSWER, float):
                                    if len(str(ANSWER).split(".")[-1]) <= 4:
                                        amount_of_tasks += 1
                                        self.add_task_to_db(i, j, k, ANSWER)
                                else:
                                    amount_of_tasks += 1
                                    self.add_task_to_db(i, j, k, ANSWER)

    def generate_with_four_variables(self):
        variables = self.get_variables()
        task_variables = self.get_variables_data()
        amount_of_tasks = self.get_amount_of_tasks()
        for i in np.arange(task_variables[0][0], task_variables[0][1], task_variables[0][2]):
            i = round(i, 4)
            if amount_of_tasks >= self.max_tasks:
                break
            exec(variables[0] + "=" + str(i))
            for j in np.arange(task_variables[1][0], task_variables[1][1], task_variables[1][2]):
                j = round(j, 4)
                if amount_of_tasks >= self.max_tasks:
                    break
                exec(variables[1] + "=" + str(j))
                for k in np.arange(
                    task_variables[2][0], task_variables[2][1], task_variables[2][2]
                ):
                    k = round(k, 4)
                    if amount_of_tasks >= self.max_tasks:
                        break
                    exec(variables[2] + "=" + str(k))
                    for l in np.arange(
                        task_variables[3][0], task_variables[3][1], task_variables[3][2]
                    ):
                        l = round(l, 4)
                        if amount_of_tasks >= self.max_tasks:
                            break
                        exec(variables[3] + "=" + str(l))
                        if eval(self.get_start_limitations()):
                            try:
                                exec(self.get_formulas())
                                ANSWER = eval(self.get_answer_formula())
                                ANSWER = round(ANSWER, 4)
                            except:
                                ANSWER = "ERROR"
                            if ANSWER != "ERROR":
                                if eval(self.get_following_limitations()):
                                    if isinstance(ANSWER, float):
                                        if len(str(ANSWER).split(".")[-1]) <= 4:
                                            amount_of_tasks += 1
                                            self.add_task_to_db(i, j, k, l, ANSWER)
                                    else:
                                        amount_of_tasks += 1
                                        self.add_task_to_db(i, j, k, l, ANSWER)

    def generate_with_five_variables(self):
        variables = self.get_variables()
        task_variables = self.get_variables_data()
        amount_of_tasks = self.get_amount_of_tasks()
        for i in np.arange(task_variables[0][0], task_variables[0][1], task_variables[0][2]):
            i = round(i, 4)
            if amount_of_tasks >= self.max_tasks:
                break
            exec(variables[0] + "=" + str(i))
            for j in np.arange(task_variables[1][0], task_variables[1][1], task_variables[1][2]):
                j = round(j, 4)
                if amount_of_tasks >= self.max_tasks:
                    break
                exec(variables[1] + "=" + str(j))
                for k in np.arange(
                    task_variables[2][0], task_variables[2][1], task_variables[2][2]
                ):
                    k = round(k, 4)
                    if amount_of_tasks >= self.max_tasks:
                        break
                    exec(variables[2] + "=" + str(k))
                    for l in np.arange(
                        task_variables[3][0], task_variables[3][1], task_variables[3][2]
                    ):
                        l = round(l, 4)
                        if amount_of_tasks >= self.max_tasks:
                            break
                        exec(variables[3] + "=" + str(l))
                        for m in np.arange(
                            task_variables[4][0], task_variables[4][1], task_variables[4][2]
                        ):
                            m = round(m, 4)
                            if amount_of_tasks >= self.max_tasks:
                                break
                            exec(variables[4] + "=" + str(m))
                            if eval(self.get_start_limitations()):
                                try:
                                    exec(self.get_formulas())
                                    ANSWER = eval(self.get_answer_formula())
                                    ANSWER = round(ANSWER, 4)
                                except:
                                    ANSWER = "ERROR"
                                if ANSWER != "ERROR":
                                    if eval(self.get_following_limitations()):
                                        if isinstance(ANSWER, float):
                                            if len(str(ANSWER).split(".")[-1]) <= 4:
                                                amount_of_tasks += 1
                                                self.add_task_to_db(i, j, k, l, m, ANSWER)
                                        else:
                                            amount_of_tasks += 1
                                            self.add_task_to_db(i, j, k, l, m, ANSWER)

    def add_task_to_db(self, *args):
        old_condition = self.get_condition()
        variables = self.get_variables()
        split_condition = old_condition.split("@")
        variables_value_dict = {}
        index = 0
        for variable in variables:
            variables_value_dict[variable] = float(args[index])
            index += 1
        for i in range(len(split_condition)):
            sentence = split_condition[i]
            if sentence in variables_value_dict:
                value = str(variables_value_dict[sentence])
                if value.split(".")[-1] == "0":
                    value = value.split(".")[0]
                split_condition[i] = value
        answer = float(args[-1])
        if str(answer).split(".")[-1] == "0":
            answer = int(str(answer).split(".")[0])
        new_condition = " ".join(split_condition)
        if new_condition not in self.all_conditions:
            new_task = PrototypeTasks.objects.create(
                Number_id=self.task.Number_id,
                Topic_id=self.task.Topic_id,
                Condition=new_condition,
                SourceTask_id=self.task.id,
                Image=self.task.Image,
            )
            new_task.save()
            answer = PrototypeAnswers.objects.create(Answer=answer, Task_id=new_task.pk)
            answer.save()


def task_generation(QuerySet):
    for task in QuerySet:
        task_instance = GenerateTask(task)
        task_instance.choose_generate()
