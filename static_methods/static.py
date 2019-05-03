class test_class:
    @classmethod
    def test_print(self):
        self.__print_sth(self)

    def __print_sth(self):
        print ('xxxxx')

if __name__ == "__main__":

    c = test_class()
    c.__print_sth()
