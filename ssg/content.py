import re
from yaml import load
from yaml import FullLoader
from _collections_abc import Mapping


class Content(Mapping):

    __delimeter = r"^(?:-|\+){3}\s*$"
    __regex = re.compile(__delimeter, re.MULTILINE)

    def load(self, cls, string):
        _, fm, content = self.__regex.split(string, 2)
        metadata = load(fm, Loader=FullLoader)
        return cls(metadata, content)

    def __init__(self, metadata: dict, content: str):
        self.data = metadata
        self.data['content'] = content

    @property
    def body(self):
        return self.data['content']

    @property
    def type(self):
        return self.data['type'] if 'type' in self.data else None

    @type.setter
    def type(self, type: str):
        self.data['type'] = type

    def __getitem__(self, key):
        return self.data[key]

    def __iter__(self):
        return iter(self.data)

    def __len__(self):
        return len(self.data)

    def __repr__(self):
        data = {}
        for key, value in self.data.items():
            if key != 'content':
                data[key] = value
        return str(data)
