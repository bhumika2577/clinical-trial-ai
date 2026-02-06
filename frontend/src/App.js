import { useState } from "react";
import PatientForm from "./components/PatientForm";

function App() {
  const [patient, setPatient] = useState(null);

  return (
    <div style={{ padding: "20px" }}>
      <h1>Clinical Trial Eligibility</h1>

      {!patient ? (
        <PatientForm onPatientCreated={setPatient} />
      ) : (
        <pre>{JSON.stringify(patient, null, 2)}</pre>
      )}
    </div>
  );
}

export default App;
