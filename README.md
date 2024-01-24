# Task Scheduler App

## Introdução

Este script Python implementa um aplicativo de agendamento de tarefas utilizando a biblioteca schedule para agendamento, a biblioteca tkinter para a GUI e a PySimpleGUI para a barra de progresso e interação do usuário.

## Funcionalidades

O aplicativo permite agendar tarefas para horários específicos do dia e exibe uma barra de progresso para cada tarefa, indicando o tempo restante para a execução da próxima tarefa. As tarefas são executadas em uma thread separada, garantindo que a interface do usuário não seja bloqueada durante a execução.

## Estrutura do Script

O script é dividido em uma classe principal TaskSchedulerApp e inclui os seguintes métodos:

### **__init__(self, root, task_list)**

    Inicializa a interface gráfica.
    Configura a janela principal (root) e a lista de tarefas (task_list).
    Define o layout da interface gráfica com o uso da biblioteca PySimpleGUI.
    Chama o método schedule_tasks() para agendar as tarefas.

### **schedule_tasks(self)**

    Utiliza a biblioteca schedule para agendar a execução das tarefas diariamente nos horários especificados na lista de tarefas.

### **run_schedule()**

    Executa a verificação contínua das tarefas agendadas em uma thread separada.

### **execute_task(self, horario)**

    Calcula o tempo restante para a execução da próxima tarefa.
    Chama o método update_progress() para exibir a barra de progresso e atualizar o status da tarefa.

### **update_progress(self, horario, remaining_time)**

    Atualiza a barra de progresso simulando o avanço da tarefa.
    Chama o método update_next_task() quando a tarefa é concluída.

### **update_next_task(self, next_task)**

    Atualiza o status da tarefa concluída na interface gráfica.

### **get_remaining_time(self, task_time)**

    Calcula o tempo restante até a próxima execução da tarefa.

### **format_time(self, remaining_time)**

    Formata o tempo restante em minutos e segundos para exibição.

## Utilização

No bloco final do script, são definidos os horários para execução das tarefas (horarios). Um objeto da classe TaskSchedulerApp é criado, iniciando assim a execução do aplicativo.

O loop principal (while True) mantém a aplicação em execução, permitindo a interação do usuário e encerrando o aplicativo quando a janela é fechada ou o botão "Fechar" é pressionado.

Ao fechar a janela, o script encerra a execução, finalizando todas as threads em segundo plano.
