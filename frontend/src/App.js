import PatientForm from "./components/PatientForm";
import EligibilityCheck from "./components/EligibilityCheck";

function App() {
  return (
    <div style={{ padding: "30px" }}>
      <h1>Clinical Trial Eligibility System</h1>

      <PatientForm onPatientCreated={() => {}} />

      <EligibilityCheck />
    </div>
  );
}

export default App;
