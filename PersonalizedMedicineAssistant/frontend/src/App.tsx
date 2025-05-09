// src/App.tsx
import React from 'react';
import ChatbotWidget from './components/ChatbotWidget';
import HospitalMap from './components/HospitalMap';
import DiseaseForm from './components/DiseaseForm';
import ResultDisplay from './components/ResultDisplay';

const App: React.FC = () => {
  const [result, setResult] = React.useState(null);

  return (
    <div className="p-4 bg-gray-100 min-h-screen">
      <h1 className="text-3xl font-bold text-center mb-6">Personalized Medicine Assistant</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <DiseaseForm setResult={setResult} />
        <ResultDisplay result={result} />
      </div>
      <div className="mt-8">
        <HospitalMap />
      </div>
      <ChatbotWidget />
    </div>
  );
};

export default App;