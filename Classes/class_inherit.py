# inherit from a List class
class TestModules(list):
    def __init__(self, *args, **kwargs):
        super(TestModules, self).__init__(args[0])

    def __contains__(self, item):
        return list.__contains__(self, 'test_' + item)
