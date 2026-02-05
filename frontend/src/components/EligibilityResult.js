import React, { useState } from "react";
import axios from "axios";

function EligibilityResult() {
  const [result, setResult] = useState(null);

  const checkEligibility = async () => {
    const patient_id = localStorage.getItem("patient_id");
    const trial_id = localStorage.getItem("trial_id");

    if (!patient_id || !trial_id) {
      alert("Please upload patient and trial first");
      return;
    }

    const res = await axios.post(
      `http://127.0.0.1:8000/eligibility/analyze?patient_id=${patient_id}&trial_id=${trial_id}`,
      {
        patient: {
          age: 69,
          eGFR: 28
        }
      }
    );

    setResult(res.data);
  };

  return (
    <div className="bg-white p-6 rounded shadow">
      <h2 className="text-xl font-semibold mb-4">Eligibility Result</h2>

      <button
        onClick={checkEligibility}
        className="bg-purple-600 text-white px-4 py-2 rounded mb-4"
      >
        Check Eligibility
      </button>

      {result && (
        <div className="space-y-2">
          <p>
            <strong>Status:</strong>{" "}
            <span className="font-bold text-red-600">
              {result.status}
            </span>
          </p>

          <p>
            <strong>Inclusion:</strong> {result.inclusion.rule} →{" "}
            {result.inclusion.status}
          </p>

          <p>
            <strong>Exclusion:</strong> {result.exclusion.rule} →{" "}
            {result.exclusion.status}
          </p>

          <div className="bg-red-100 p-3 rounded border border-red-400">
            ⚠️ <strong>Silent Exclusion Triggered</strong>
            <p className="text-sm mt-1">{result.explanation}</p>
          </div>
        </div>
      )}
    </div>
  );
}

export default EligibilityResult;
