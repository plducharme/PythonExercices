import csv


class StationComptage:

    def __init__(self, id, emplacement, nom, latitude, longitude):
        self.id = id
        self.emplacement = emplacement
        self.nom = nom
        self.latitude = latitude
        self.longitude = longitude
        self.comptage = []

    @classmethod
    def from_csv(cls):
        stations = {}
        with open('liste_des_stations_de_comptage.csv') as station_csv:
            reader = csv.DictReader(station_csv)

            for line in reader:
                id = line['id_station']
                if line['id_station'].startswith('P'):
                    stations[id] = cls(line['id_station'], line['nom_station'], line['nom_vas'],
                                                   line['latitude'], line['longitude'])

        with open('comptages_pietons_vas.csv') as pietons_csv:
            reader = csv.DictReader(pietons_csv)

            for line in reader:
                station = line['id_station']
                comptage = Comptage(line['timestamp_local'], line['compte_total'])
                stations[station].comptage.append(comptage)
        return stations


class Comptage:

    def __init__(self, date, total):
        self.date = date
        self.total = total










