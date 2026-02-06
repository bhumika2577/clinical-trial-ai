import PatientForm from "./components/PatientForm";
import TrialForm from "./components/TrialForm";
import EligibilityResult from "./components/EligibilityResult";

function App() {
  return (
    <div className="max-w-4xl mx-auto p-6 space-y-8">
      <h1 className="text-2xl font-bold">
        Clinical Trial Eligibility System
      </h1>

      
      <PatientForm />

      
      <TrialForm />

      
      <EligibilityResult />
    </div>
  );
}

export default App;
