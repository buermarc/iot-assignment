import os, threading

class PubSubBroker: 

    def __init__(self):
        self._topics = {}

    def sub(self, topic, methode):
        if not topic in self._topics:
            self._topics[topic] = []
        self._topics[topic].append(methode)

    def unsub(self, topic, methode):
        if not topic in self._topics:
            return
        self._topics[topic].remove(methode)

    def pub(self, topic, *args, **kwargs):
        if topic in self._topics:
            for methode in self._topics[topic]:
                thread=threading.Thread(target=methode, name=(str(topic)+" "+str(methode)), \
                        args=args, kwargs=kwargs)
                thread.start() 
