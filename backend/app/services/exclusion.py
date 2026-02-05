def check_egfr(eGFR):
    if eGFR < 30:
        return {"rule": "eGFR < 30", "status": "FAIL"}
    return {"rule": "eGFR < 30", "status": "PASS"}
