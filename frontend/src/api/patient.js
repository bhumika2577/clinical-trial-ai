import api from "./client";

export const createPatient = (data) => {
  return api.post("/patient/", {
    age: Number(data.age),
    egfr: Number(data.egfr),
    conditions: data.conditions, // already an array
  });
};

export const getPatients = () => {
  return api.get("/patient/");
};
