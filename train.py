from abc import ABC, abstractmethod


class AbstractBaseClass(ABC):

    def __init__(self, data):
        self.data = data
        self.class_name = self.__class__.__name__.lower()

    @abstractmethod
    def generate_report(self):
        if self.data["type"] == self.class_name:
            self.generate_some_report()

    @abstractmethod
    def generate_some_report(self):
        print(f"Generating {self.class_name.upper()} report...")

    @abstractmethod
    def save_report(self):
        if self.data["type"] == self.class_name:
            self.save_some_report()

    @abstractmethod
    def save_some_report(self):
        print(f"Saving {self.class_name.upper()} report...")


class CSV(AbstractBaseClass):

    def __init__(self, data):
        super().__init__(data)

    def generate_some_report(self):
        super().generate_some_report()

    def generate_report(self):
        super().generate_report()

    def save_some_report(self):
        super().save_some_report()

    def save_report(self):
        super().save_report()


class PDF(AbstractBaseClass):

    def __init__(self, data):
        super().__init__(data)

    def generate_some_report(self):
        super().generate_some_report()

    def generate_report(self):
        super().generate_report()

    def save_some_report(self):
        super().save_some_report()

    def save_report(self):
        super().save_report()


class Excel(AbstractBaseClass):

    def __init__(self, data):
        super().__init__(data)

    def generate_some_report(self):
        super().generate_some_report()

    def generate_report(self):
        super().generate_report()

    def save_some_report(self):
        super().save_some_report()

    def save_report(self):
        super().save_report()


class Yaml(AbstractBaseClass):

    def __init__(self, data):
        super().__init__(data)

    def generate_yaml_report(self):
        super().generate_some_report()

    def generate_report(self):
        super().generate_report()

    def save_yaml_report(self):
        super().save_some_report()

    def save_report(self):
        super().save_report()


data1 = {"type": "csv"}
report = CSV(data1)
report.generate_report()
report.save_report()
