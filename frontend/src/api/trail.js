import api from "./client";

export const uploadTrialPDF = (file) => {
  const formData = new FormData();
  formData.append("file", file);

  return api.post("/trial/upload", formData, {
    headers: {
      "Content-Type": "multipart/form-data",
    },
  });
};
