// DiseaseForm.tsx
import React, { useState } from 'react';
import axios from 'axios';

const DiseaseForm = ({ onResult }) => {
  const [symptoms, setSymptoms] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('/api/predict', { symptoms });
      onResult(response.data);
    } catch (error) {
      console.error('Prediction error:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="disease-form p-4 rounded-lg shadow-lg bg-white">
      <h2 className="text-xl font-bold mb-2">Disease Predictor</h2>
      <textarea
        value={symptoms}
        onChange={(e) => setSymptoms(e.target.value)}
        placeholder="Enter symptoms (comma separated)"
        className="w-full p-2 border rounded mb-2"
      />
      <button type="submit" className="w-full bg-green-500 text-white p-2 rounded">
        Predict Disease
      </button>
    </form>
  );
};

export default DiseaseForm;
