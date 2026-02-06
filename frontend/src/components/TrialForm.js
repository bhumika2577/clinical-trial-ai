import { useState } from "react";
import { uploadTrialPDF } from "../api/trial";

function TrialForm() {
  const [file, setFile] = useState(null);
  const [message, setMessage] = useState("");

  const uploadTrial = async () => {
    if (!file) return;

    try {
      const res = await uploadTrialPDF(file);
      setMessage("Trial uploaded successfully");

      localStorage.setItem("trial_id", res.data.trial_id);
    } catch (err) {
      console.error(err);
      setMessage("Error uploading trial");
    }
  };

  return (
    <div className="bg-white p-6 rounded shadow">
      <h2 className="text-xl font-semibold mb-4">Trial Protocol</h2>

      <input
        type="file"
        className="mb-3"
        onChange={(e) => setFile(e.target.files[0])}
      />

      <button
        onClick={uploadTrial}
        className="bg-green-600 text-white px-4 py-2 rounded"
      >
        Upload Trial
      </button>

      {message && <p className="mt-3 text-sm">{message}</p>}
    </div>
  );
}

export default TrialForm;
