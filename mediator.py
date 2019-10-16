class Mediator:
    """
    Implement cooperative behavior by coordinating Colleague objects.
    Know and maintains its colleagues.
    """

    def __init__(self):
        self.elements = {}
        self.tasks = {}
        self.linkTable = {}

    def SetElement(self, element):
        if self.elements.get(element.guid) is None:
            self.elements[element.guid] = element
        self.SetLinks(element.guid, element.taskid)

    def SetTasks(self,task):
        if self.tasks.get(task.taskid) is None:
            self.tasks[task.taskid] = task
        self.SetLinks(task.taskid, task.guid)

    def SetLinks(self, key, value):
        # Set dual 
        if self.linkTable.get(key) is None:
            self.linkTable[key] = value
        if self.linkTable.get(value) is None:
            self.linkTable[value] = key

    def GetElement(self, id):
        guid = self.linkTable[id]
        return self.elements[guid].do()

    def GetTask(self, id):
        taskid = self.linkTable[id]
        return self.tasks[taskid].do()


class Element:
    """
    Know its Mediator object.
    Communicate with its mediator whenever it would have otherwise
    communicated with another colleague.
    """

    def __init__(self, mediator, guid, taskid):
        self.mediator = mediator
        self.guid = guid
        self.taskid = taskid

    def do(self):
        print("element guid: ", self.guid)

class Task:
    """
    Know its Mediator object.
    Communicate with its mediator whenever it would have otherwise
    communicated with another colleague.
    """

    def __init__(self, mediator, taskid, guid):
        self.mediator = mediator
        self.taskid = taskid
        self.guid = guid

    def do(self):
        print("taskid: ",self.taskid)


def main():
    # init objects
    mediator = Mediator()
    element1 = Element(mediator,1,5)
    element2 = Element(mediator,2,6)
    task5 = Task(mediator,5,1)
    task6 = Task(mediator,6,2)
    # init mediator
    mediator.SetElement(element1)
    mediator.SetElement(element2)
    mediator.SetTasks(task5)
    mediator.SetTasks(task6)

    #element1 find corresponding task id
    element1.mediator.GetTask(1)

    #element2 find corresponding task id
    element2.mediator.GetTask(2)

    #task5 find corresponding element id
    task5.mediator.GetElement(5)

    #task6 find corresponding element id
    task6.mediator.GetElement(6)
    print("done")

if __name__ == "__main__":
    main()