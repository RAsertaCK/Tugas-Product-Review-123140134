import React, { useState } from 'react';
import ReviewForm from './components/ReviewForm';
import ReviewList from './components/ReviewList';
import './App.css'; 

function App() {
  const [newAnalysisResult, setNewAnalysisResult] = useState(null);
  const [refreshTrigger, setRefreshTrigger] = useState(0);

  const handleAnalysisComplete = (result) => {
    setNewAnalysisResult(result);
    setRefreshTrigger(prev => prev + 1); 
  };

  return (
    <div className="app-container">
      <h1>Product Review Analyzer</h1>
      <p className="subtitle">Menganalisis sentimen dengan Hugging Face dan mengekstrak poin utama dengan Gemini.</p>
      
      <div className="content-wrapper">
        <ReviewForm onAnalysisComplete={handleAnalysisComplete} />
        
        <hr className="divider" />

        <ReviewList 
          newResult={newAnalysisResult} 
          triggerRefresh={refreshTrigger} 
        />
      </div>
    </div>
  );
}

export default App;