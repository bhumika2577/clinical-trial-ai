import api from "./client";

export const checkEligibility = (data) => {
  return api.post("/eligibility/check", data);
};
