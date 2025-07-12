class BaseClass:

    def __init__(self, data):
        self.data = data
        self.class_name = self.__class__.__name__.lower()

    def generate_report(self):
        if self.data["type"] == self.class_name:
            self.generate_some_report()

    def generate_some_report(self):
        print(f"Generating {self.class_name.upper()} report...")

    def save_report(self):
        if self.data["type"] == self.class_name:
            self.save_some_report()

    def save_some_report(self):
        print(f"Saving {self.class_name.upper()} report...")


class CSV(BaseClass):

    def __init__(self, data):
        super().__init__(data)

    def generate_csv_report(self):
        super().generate_some_report()

    def generate_report(self):
        super().generate_report()

    def save_csv_report(self):
        super().save_some_report()

    def save_report(self):
        super().save_report()


class PDF(BaseClass):

    def __init__(self, data):
        super().__init__(data)

    def generate_pdf_report(self):
        super().generate_some_report()

    def generate_report(self):
        super().generate_report()

    def save_pdf_report(self):
        super().save_some_report()

    def save_report(self):
        super().save_report()


class Excel(BaseClass):

    def __init__(self, data):
        super().__init__(data)

    def generate_excel_report(self):
        super().generate_some_report()

    def generate_report(self):
        super().generate_report()

    def save_excel_report(self):
        super().save_some_report()

    def save_report(self):
        super().save_report()


data1 = {"type": "csv"}
report = CSV(data1)
report.generate_report()
report.save_report()