def detect_contradiction(inclusion, exclusion, patient):
    """
    Detects silent exclusion when inclusion passes but exclusion fails.
    """

    if inclusion["status"] == "PASS" and exclusion["status"] == "FAIL":
        return {
            "silent_exclusion": True,
            "explanation": (
                f"Patient meets {inclusion['rule']} "
                f"but is excluded because {exclusion['rule']} "
                f"(patient value: {patient.get('eGFR')})."
            )
        }

    return {
        "silent_exclusion": False
    }
