import React from "react";
import PatientForm from "./components/PatientForm";
import TrialForm from "./components/TrialForm";
import EligibilityResult from "./components/EligibilityResult";

function App() {
  return (
    <div className="min-h-screen bg-gray-100 p-6">
      <h1 className="text-3xl font-bold text-center mb-8">
        AI Clinical Trial Eligibility Engine
      </h1>

      <div className="max-w-6xl mx-auto space-y-8">
        <PatientForm />
        <TrialForm />
        <EligibilityResult />
      </div>
    </div>
  );
}

export default App;

