clases = [{"nombre": "Functional", "coach": "Arale", "cupo": 20, "reservados": 14},{"nombre": "Hyrox Beginers", "coach": "Alex", "cupo": 20, "reservados": 20}, {"nombre": "Pilates", "coach": "Scanda", "cupo": 20, "reservados": 10}, {"nombre": "Chest&Triceps", "coach": "Leo", "cupo": 15, "reservados": 15}, {"nombre": "Running", "coach": "Alejandro", "cupo": 50, "reservados": 46}]
for c in clases:
    if c["reservados"]< c["cupo"]:
        print(c["cupo"]-c["reservados"])
