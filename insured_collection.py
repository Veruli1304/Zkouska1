from insured import Insured

class InsuredCollection:
    def __init__(self):
        self.insureds = []

    def add_insured(self, insured):
        self.insureds.append(insured)

    def find_insured_by_name(self, name, surname):
        for insured in self.insureds:
            if insured.name == name and insured.surname == surname:
                return insured
        return None

    def __str__(self):
        output = ""
        for insured in self.insureds:
            output += f"{insured}\n"
        return output
