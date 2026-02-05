def check_age(patient_age):
    if 18 <= patient_age <= 70:
        return {"rule": "Age 18–70", "status": "PASS"}
    return {"rule": "Age 18–70", "status": "FAIL"}
