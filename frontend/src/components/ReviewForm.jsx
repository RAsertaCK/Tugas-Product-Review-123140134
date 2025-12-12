import React, { useState } from 'react';
import LoadingSpinner from './LoadingSpinner';

const API_BASE_URL = import.meta.env.VITE_API_URL || "http://localhost:8000";

const ReviewForm = ({ onAnalysisComplete }) => {
    const [reviewText, setReviewText] = useState('');
    const [isLoading, setIsLoading] = useState(false);
    const [error, setError] = useState(null);

    const handleSubmit = async (e) => {
        e.preventDefault();
        setError(null);
        const trimmedText = reviewText.trim();
        
        if (!trimmedText) {
            setError("Review text cannot be empty.");
            return;
        }

        setIsLoading(true);
        try {
            const response = await fetch(`${API_BASE_URL}/api/analyze-review`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ review_text: trimmedText }),
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.detail || `HTTP Error ${response.status}: Analysis failed.`);
            }

            const result = await response.json();
            onAnalysisComplete(result);
            setReviewText('');
        } catch (err) {
            console.error('API Error:', err);
            setError(`Koneksi/API Error: ${err.message}. Pastikan Backend (port 8000) dan Gemini API Key sudah benar.`);
        } finally {
            setIsLoading(false);
        }
    };

    return (
        <div className="review-form-container">
            <h3>Input Review Produk Baru</h3>
            <form onSubmit={handleSubmit}>
                <textarea
                    value={reviewText}
                    onChange={(e) => setReviewText(e.target.value)}
                    placeholder="Contoh: Saya suka sekali dengan sepatu ini! Bahannya sangat ringan dan nyaman dipakai lari. Hanya saja, tali sepatunya mudah lepas."
                    rows="6"
                    disabled={isLoading}
                />
                <button type="submit" disabled={isLoading}>
                    {isLoading ? 'Menganalisis...' : ' Analisis Review & Simpan'}
                </button>
            </form>
            {isLoading && <LoadingSpinner />}
            {error && <p className="error-message"> {error}</p>}
        </div>
    );
};

export default ReviewForm;