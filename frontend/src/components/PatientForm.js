import { useState } from "react";
import { createPatient } from "../api/patient";

function PatientForm() {
  const [age, setAge] = useState("");
  const [egfr, setEgfr] = useState("");
  const [message, setMessage] = useState("");

  const submitPatient = async () => {
    try {
      const res = await createPatient({
        age: Number(age),
        egfr: Number(egfr),
        conditions: ["Type 2 Diabetes"],
      });

      setMessage(`Patient saved with ID: ${res.data.patient_id}`);
      localStorage.setItem("patient_id", res.data.patient_id);
    } catch (err) {
      console.error(err);
      setMessage("Error saving patient");
    }
  };

  return (
    <div className="bg-white p-6 rounded shadow">
      <h2 className="text-xl font-semibold mb-4">Patient Details</h2>

      <input
        type="number"
        placeholder="Age"
        className="border p-2 w-full mb-3"
        value={age}
        onChange={(e) => setAge(e.target.value)}
      />

      <input
        type="number"
        placeholder="eGFR"
        className="border p-2 w-full mb-3"
        value={egfr}
        onChange={(e) => setEgfr(e.target.value)}
      />

      <button
        onClick={submitPatient}
        className="bg-blue-600 text-white px-4 py-2 rounded"
      >
        Save Patient
      </button>

      {message && <p className="mt-3 text-sm">{message}</p>}
    </div>
  );
}

export default PatientForm;
