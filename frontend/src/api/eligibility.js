import api from "./client";

export const analyzeEligibility = (patientId, trialId, patientData) => {
  return api.post(
    `/eligibility/analyze?patient_id=${patientId}&trial_id=${trialId}`,
    {
      patient: {
        age: Number(patientData.age),
        eGFR: Number(patientData.eGFR),
      },
    }
  );
};
