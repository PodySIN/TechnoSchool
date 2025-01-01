let formulaFieldCount = 0;
let variableFieldCount = 0;
function addFormulaField() {
    formulaFieldCount++;
    let container = document.getElementById('dynamicFormulaFieldsContainer');
    let newField = document.createElement('textarea');
    newField.name = `Formula_${formulaFieldCount}`;
    newField.placeholder = `Шаг ${formulaFieldCount}`;
    container.appendChild(newField);
    container.appendChild(document.createElement('br'));
    container.appendChild(document.createElement('br'));
}

function addVariableField() {
    variableFieldCount++;
    let container = document.getElementById('dynamicVariableFieldsContainer');
    let newField = document.createElement('textarea');
    newField.name = `Limitation_${variableFieldCount}`;
    newField.placeholder = `Ограничения ${variableFieldCount}`;
    container.appendChild(newField);
    container.appendChild(document.createElement('br'));
    container.appendChild(document.createElement('br'));
}

function newSelectedNumber(){
    let selectNumberElement = document.getElementById('id_Number');
    let selectedValue = Number(selectNumberElement.value);
    let selectTopicElement = document.getElementById('id_Topic');
    let topics = All_topics[selectedValue.toString()]
    length_of_options = selectTopicElement.options.length
    for (let i = 0; i <= length_of_options; i++){
        selectTopicElement.remove(0)
    }
    for (let i = 0; i < topics.length; i++) {
        option_add = new Option(topics[i])
        option_add.value = topics[i]
        selectTopicElement.add(option_add)
    }
}

function IsTaskSourceChanged(){OldTaskSelect
    let selectIsTaskSource = document.getElementById('id_IsTaskSource')
    let selectSourcesTaskId = document.getElementById('OldTaskSelect')
    let newTaskForms = document.getElementById('new_task_forms')
    let selectTopicElement = document.getElementById('id_Topic');
    let selectNumberElement = document.getElementById('id_Number');
    val = selectIsTaskSource.value
    if (val == 'Да'){
        selectSourcesTaskId.hidden = false
        selectSourcesTaskId.required = true
        newTaskForms.hidden = true
        let TaskNumber = selectNumberElement.value
        let TaskTopic = selectTopicElement.value
        let prototypes = All_SourceTasks[TaskNumber.toString()]
        let res = []
        for (let i =0;i < prototypes.length;i++){
            if (prototypes[i][1] == TaskTopic){
                res.push(prototypes[i][0])
            }
        }
        length_of_options = selectSourcesTaskId.options.length
        for (let i = 0; i <= length_of_options; i++){
            selectSourcesTaskId.remove(0)
        }
        for (let i = 0; i < res.length; i++) {
            option_add = new Option(res[i])
            option_add.value = res[i]
            option_add.text = 'Код задания: ' + res[i].toString()
            selectSourcesTaskId.add(option_add)
        }
    }
    else if (val == 'Нет'){
        newTaskForms.hidden = false
        selectSourcesTaskId.hidden = true
        selectSourcesTaskId.required = false
        len = selectSourcesTaskId.options.length
        for (let i = 0; i <= len; i++){
            selectSourcesTaskId.remove(0)
        }
    }
}
