from abc import ABC, abstractmethod


# The methods that our classes gonna have
class Iterator(ABC):

    @abstractmethod
    def current(self):
        pass

    @abstractmethod
    def next(self):
        pass

    @abstractmethod
    def hasNext(self):
        pass


# We are creating this class to get the inputs from the user
# Then we save them in a list
class BrowseHistory:
    urls = []

    def push_single(self, url):
        self.urls.append(url)

    def push_multiple(self, *urls):
        self.urls.append(urls)

    def remove(self):
        self.urls.pop()

        return self.urls[-1]

    def get_list(self):
        return self.urls

    # This is called an inner class and we use it to iterate the items
    # In our list
    class ListIterator(Iterator):
        _history = ""
        index = 0

        # We are inherting everything from the parent class
        def __init__(self):
            self._history = BrowseHistory

        # We return the current item
        def current(self):
            url = self._history.urls[self.index]
            return url

        # We check if there is more items to iterate over
        def hasNext(self):
            return (self.index < len(self._history.urls))

        # After we got the item we increase the index to get the next item
        def next(self):
            self.index += 1
            return self.index


browser = BrowseHistory()
browser.push_single("a")
browser.push_single('b')
browser.push_single('c')
browser.push_multiple(1, 2, 3)

iterate = browser.ListIterator()


while iterate.hasNext:
    try:
        url = iterate.current()
        print(url)
        iterate.next()
    except:
        pass

print(browser.get_list())

# my = [1, 2, 3, 4, 5]

# index = 0

# while index < len(my):
#     print(1)
#     index += 1
