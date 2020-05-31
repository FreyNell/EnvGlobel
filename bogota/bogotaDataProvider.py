
import mysql.connector


class BogotaDataProvider:

    def __init__(self) -> None:

        self.cnx = mysql.connector.connect(user='root', password='example',
                                           host='34.67.137.54',
                                           database='EnvGlobel')

    def saveWeatherData(self, record):
        cursor = self.cnx.cursor()
        query = ("INSERT INTO "
                 "weatherBogota(measureDate, station, temperature, windSpeed, windDirection, precipitation, pressure)"
                 "VALUES (%(date)s, %(station)s, %(temperature)s, %(windSpeed)s, %(windDirection)s, %(precipitation)s, %(pressure)s)")
        cursor.execute(query, record)
        self.cnx.commit()
        cursor.close()

    def getPollutionStationLocations(self):
        cursor = self.cnx.cursor()
        query = ("SELECT id, latitude, longitude FROM pollutionStationBogota")
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result

    def getWeatherStationNames(self):
        cursor = self.cnx.cursor()
        query = ("SELECT name, id FROM weatherStationBogota")
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result

    def saveTrafficData(self, record):
        cursor = self.cnx.cursor()
        query = ("INSERT INTO "
                 "trafficBogota(measureDate, pollutionStation, green, orange, red, darkRed)"
                 "VALUES (%(date)s, %(pollutionStation)s, %(green)s, %(orange)s, %(red)s, %(darkRed)s)")
        cursor.execute(query, record)
        self.cnx.commit()
        cursor.close()