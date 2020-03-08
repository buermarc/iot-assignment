class AlertService: # Service Reagiert auf Messwerte

    #  Initialisierung
    def __init__(self):
        pass

    #  value:  Neuer Schwellwert als einfache Zahl in der Einheit cm wird hier übergeben
    def set_alert_threshold (self, value):
        self.treshhold = value;

    #  value:  Aktuell gemessener Wert (siehe DistanceSensor) wird übergeben und es wird ein Alarm gesendet
    def on_distance_threshold_passed(self, value):
        # write to mqtt topic in config.json
        pass
