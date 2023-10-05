
class SapGuiEnum:
    """ GuiEnum é a classe base para alguns enumeradores usados em scripts SAP GUI.
    """

    class_attrs: list[str]
    component: object

    def __init__(self, component: object):
        self.class_attrs = ['component']
        self.component = component

    def __getattr__(self, attr):
        return getattr(self.component, attr)

    def __setattr__(self, attr, value):
        if attr in self.__dict__ or attr == 'class_attrs' or attr in self.class_attrs:
            super().__setattr__(attr, value)
        else:
            setattr(self.component, attr, value)

    # noinspection PyUnresolvedReferences
    def next(self, celt: int, rgvar, pcelt_fetched: int):
        return self.component.Next(celt, rgvar, pcelt_fetched)

    # noinspection PyUnresolvedReferences
    def reset(self):
        return self.component.Reset()

    # noinspection PyUnresolvedReferences
    def skip(self, celt: int):
        return self.component.Skip(celt)