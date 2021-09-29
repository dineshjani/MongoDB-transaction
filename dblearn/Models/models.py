class Student:
    def __init__(self, value):
        if value != None:
            self.Name = value.get("name","")
            self.Gender = value.get("gender","")
            self.Age = value.get("age", "")
            self.Address = value.get("address", "")

    @property
    def Name(self) -> str:
        return self.__type

    @Name.setter
    def Name(self, value):
        self.__type = value

    @property
    def Age(self) -> dict:
        return self.__value

    @Age.setter
    def Age(self, value):
        self.__value = value

    @property
    def Gender(self) -> str:
        return self.__Gender

    @Gender.setter
    def Gender(self, value):
        self.__condition = value

    @property
    def Address(self) -> str:
        return self.__

    @Address.setter
    def Address(self, value):
        self.__return_if = value



