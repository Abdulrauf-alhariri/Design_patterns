from abc import ABC, abstractmethod


# Stratyge pattern is very familliar with the state pattern but it has two states
# That we can change depinding in which we choice, the pattern depends on polyphenism


class MessageType(ABC):
    @abstractmethod
    def typyMessage(self):
        pass


class MessageStatus(ABC):
    @abstractmethod
    def messageStatus(self):
        pass

# This is our controlpalen


class SendingMessages():

    # Here we are passing a MassageType object and MessageStatus object
    def message(self, text, mtpye: MessageType, mstatus: MessageStatus):
        print(text)
        mtpye.typyMessage(self)
        mstatus.messageStatus(self)


class MessageImage(MessageType):
    def typyMessage(self):
        print("This is an image")


class MessageText(MessageType):
    def typyMessage(self):
        print("This is a text message")


class MessageSend(MessageStatus):
    def messageStatus(self):
        print("Send")


myMessage = SendingMessages()

myMessage.message("Hello there", MessageImage, MessageSend)
