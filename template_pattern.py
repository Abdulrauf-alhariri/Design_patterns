from abc import ABC, abstractmethod

# This method is used in case you're creating an application that has many tasks
# and they all have the same code but with small diffrencec so the template
# pattern is ideal instead of repeting the code


class AuditTrial(ABC):
    def save(self):
        print("Save")

    @abstractmethod
    def _doexecute(self):
        pass


# Its also fammilir to the strategy pattern
class Task():
    # Here I'm defining a method that represent the task
    taskType = ""

    def __init__(self, task: AuditTrial):
        self.taskType = task

    # Here we are excuting the task methods because it's inherting from the AuditTrial class
    def execute(self):
        self.taskType.save()

        self.taskType._doexecute()


class TransferMoney(AuditTrial):
    def _doexecute(self):
        print("Transfer Money")


class GeneratReport(AuditTrial):
    def _doexecute(self):
        print("Generate Report")


task = Task(GeneratReport())
task.execute()
