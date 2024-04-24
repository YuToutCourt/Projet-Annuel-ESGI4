class Train:
    def __init__(self, id, uuid, name, track, wagon, date, hour, freight, private):
        self.id = id
        self.uuid = uuid
        self.name = name
        self.track = track
        self.wagon = wagon
        self.date = date
        self.hour = hour
        self.freight = freight
        self.private = private

    def __str__(self):
        return f"Train {self.name} with {self.wagon} wagons, on track {self.track}, carrying {self.freight}."