class EditorState:
    def __init__(self, content):
        self.content = content


class Editor:
    def __init__(self):
        self.content = ""

    def __str__(self):
        return f'{self.content}'

    def setContent(self, value):
        self.content = value

    def createContent(self):
        return EditorState(self.content)

    def restore(self, new_value):
        self.content = new_value

    def getcontent(self):
        return self.content


class History:
    def __init__(self):
        self.history = []

    def __repr__(self):
        return self.history

    def push(self, value):
        self.history.append(value)

    def remove(self):
        my_list = self.history
        my_list.pop()

        last_index = my_list[-1]
        return last_index

    def getvalue(self):
        my_list = self.history
        return self.history


editor = Editor()
history = History()

editor.setContent("a")
history.push(editor.createContent())

editor.setContent("b")
history.push(editor.createContent())

editor.setContent("c")
history.push(editor.createContent())

editor.setContent("D")
history.push(editor.createContent())

editor.restore(history.remove())
print(history.getvalue())
print(editor.getcontent())
