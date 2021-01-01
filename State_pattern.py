from abc import ABC, abstractmethod


# This class is to create the methods that each class
# Is going to have
class State(ABC):

    @abstractmethod
    def time(self):
        pass

    @abstractmethod
    def direction(self):
        pass


# Here we are handling the process and printing the results
class ControllCenter():
    _state = None

    # Here we are creating an inhertince to our abstract class
    # and calling our which_dire function
    def __init__(self, state: State):
        self.which_dire(state)

    def which_dire(self, state: State):
        print("Holding whith calculating the time to arrive")
        self._state = state

    # After we creating an object to our abstract class
    # So we could access its methods
    def get_info(self):
        self._state.time()

# Here are the mwthods that our Controll class is going to have
# After we were done with the first direction so we are calling the second class


class FirstDirection(State):
    def time(self):
        print("Whitin two hours you will be at your direction:", self.direction())
        ControllCenter.which_dire(self, SecondDirection())
        ControllCenter.get_info(self)

    def direction(self):
        return "San fransisco"


class SecondDirection(State):
    def time(self):
        print("Whithin four hours you will be at your direction:", self.direction())
        ControllCenter.which_dire(self, FirstDirection())

    def direction(self):
        return "New York"


drive = ControllCenter(FirstDirection())
drive.get_info()
