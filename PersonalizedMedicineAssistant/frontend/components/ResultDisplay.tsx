// ResultDisplay.tsx
import React from 'react';

const ResultDisplay = ({ result }) => {
  if (!result) return null;
  return (
    <div className="result-display p-4 rounded-lg shadow-lg bg-white">
      <h2 className="text-xl font-bold mb-2">Diagnosis Result</h2>
      <p><strong>Disease:</strong> {result.disease}</p>
      <p><strong>Precautions:</strong> {result.precautions.join(', ')}</p>
      <p><strong>Medications:</strong> {result.medications.join(', ')}</p>
    </div>
  );
};

export default ResultDisplay;