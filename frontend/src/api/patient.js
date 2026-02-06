import api from "./client";

export const createPatient = (data) => {
  return api.post("/patient/", data);
};

export const getPatients = () => {
  return api.get("/patient/");
};
