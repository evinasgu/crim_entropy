class Street:
    def __init__(self, first_house, second_house, street_id):
        self.street_id = street_id
        self.first_house = first_house
        self.second_house = second_house

    def build_friendly(self):
        return {
            "id": self.street_id,
            "first_house": self.first_house,
            "second_house": self.second_house
        }


class StreetResponse:
    def __init__(self, street_list):
        self.street_list = street_list

    def build_friendly(self):
        return [x.build_friendly() for x in self.street_list]


class CriminalDanger:
    def __init__(self, criminal_danger_id, criminal_danger_value):
        self.criminal_danger_id = criminal_danger_id
        self.criminal_danger_value = criminal_danger_value

    def build_friendly(self):
        return {
            "street_name": "street_" + str(self.criminal_danger_id),
            "criminal_danger": self.criminal_danger_value
        }


class CriminalDangerResponse:
    def __init__(self, criminal_danger_list):
        self.criminal_danger_list = criminal_danger_list

    def build_friendly(self):
        return [x.build_friendly() for x in self]
