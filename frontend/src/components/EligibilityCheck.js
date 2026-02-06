import { useState } from "react";
import { analyzeEligibility } from "../api/eligibility";

function EligibilityCheck() {
  const [patientId, setPatientId] = useState("");
  const [trialId, setTrialId] = useState("");
  const [age, setAge] = useState("");
  const [eGFR, setEGFR] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleCheck = async (e) => {
    e.preventDefault();
    setLoading(true);
    setResult(null);

    try {
      const res = await analyzeEligibility(
        patientId,
        trialId,
        { age, eGFR }
      );
      setResult(res.data);
    } catch (err) {
      console.error(err);
      alert("Eligibility check failed");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ marginTop: "30px" }}>
      <h2>Eligibility Check</h2>

      <form onSubmit={handleCheck}>
        <input
          type="number"
          placeholder="Patient ID"
          value={patientId}
          onChange={(e) => setPatientId(e.target.value)}
          required
        />

        <input
          type="number"
          placeholder="Trial ID"
          value={trialId}
          onChange={(e) => setTrialId(e.target.value)}
          required
        />

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

        <button type="submit" disabled={loading}>
          {loading ? "Checking..." : "Analyze Eligibility"}
        </button>
      </form>

      {result && (
        <div style={{ marginTop: "20px", border: "1px solid #ccc", padding: "15px" }}>
          <h3>Status: {result.status}</h3>

          <p>
            <strong>Inclusion:</strong> {result.inclusion.rule} —{" "}
            {result.inclusion.status}
          </p>

          <p>
            <strong>Exclusion:</strong> {result.exclusion.rule} —{" "}
            {result.exclusion.status}
          </p>

          <p>
            <strong>Explanation:</strong> {result.explanation}
          </p>
        </div>
      )}
    </div>
  );
}

export default EligibilityCheck;
