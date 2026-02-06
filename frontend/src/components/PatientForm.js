import { useState } from "react";
import { createPatient } from "../api/patient";

function PatientForm({ onPatientCreated }) {
  const [age, setAge] = useState("");
  const [eGFR, setEGFR] = useState("");
  const [conditions, setConditions] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    const payload = {
      age: Number(age),
      eGFR: Number(eGFR),
      conditions: conditions
        .split(",")
        .map((c) => c.trim())
        .filter(Boolean),
    };

    try {
      const res = await createPatient(payload);
      alert("Patient created successfully");
      onPatientCreated(res.data);
    } catch (err) {
      console.error(err);
      alert("Failed to create patient");
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Create Patient</h2>

      <input
        type="number"
        placeholder="Age"
        value={age}
        onChange={(e) => setAge(e.target.value)}
        required
      />

      <input
        type="number"
        placeholder="eGFR"
        value={eGFR}
        onChange={(e) => setEGFR(e.target.value)}
        required
      />

      <input
        type="text"
        placeholder="Conditions (comma separated)"
        value={conditions}
        onChange={(e) => setConditions(e.target.value)}
      />

      <button type="submit">Save Patient</button>
    </form>
  );
}

export default PatientForm;
