import { useState } from "react";
import { createPatient } from "../api/patient";

function PatientForm({ onPatientCreated }) {
  const [age, setAge] = useState("");
  const [egfr, setEgfr] = useState("");
  const [conditions, setConditions] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    const payload = {
      age: Number(age),
      egfr: Number(egfr), // ✅ MUST be `egfr` (lowercase) to match backend schema
      conditions: conditions
        .split(",")
        .map((c) => c.trim())
        .filter(Boolean),
    };

    try {
      const res = await createPatient(payload);
      alert("Patient created successfully");

      if (onPatientCreated) {
        onPatientCreated(res.data);
      }

      // optional: reset form
      setAge("");
      setEgfr("");
      setConditions("");
    } catch (err) {
      console.error("Create patient failed:", err);
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
        value={egfr}
        onChange={(e) => setEgfr(e.target.value)}
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
