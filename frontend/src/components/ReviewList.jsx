import React, { useEffect, useState } from 'react';
import LoadingSpinner from './LoadingSpinner';

const API_BASE_URL = import.meta.env.VITE_API_URL || "http://localhost:8000";

const ReviewList = ({ newResult, triggerRefresh }) => {
    const [reviews, setReviews] = useState([]);
    const [isLoading, setIsLoading] = useState(false);
    const [error, setError] = useState(null);

    const fetchReviews = async () => {
        setIsLoading(true);
        setError(null);
        try {
            const response = await fetch(`${API_BASE_URL}/api/reviews`);
            if (!response.ok) {
                throw new Error("Failed to fetch reviews.");
            }
            const data = await response.json();
            setReviews(data);
        } catch (err) {
            console.error('Fetch Error:', err);
            setError(`Koneksi Error: ${err.message}. Pastikan Backend berjalan.`);
        } finally {
            setIsLoading(false);
        }
    };

    useEffect(() => {
        fetchReviews();
    }, [triggerRefresh]); 

    useEffect(() => {
        if (newResult && newResult.id) {
            setReviews(prev => {
                if (prev.some(r => r.id === newResult.id)) {
                    return prev;
                }
                return [newResult, ...prev];
            });
        }
    }, [newResult]);


    const getSentimentClass = (sentiment) => {
        if (!sentiment) return 'sentiment-neutral';
        const lowerSent = sentiment.toLowerCase();
        if (lowerSent.includes('positive')) return 'sentiment-positive';
        if (lowerSent.includes('negative')) return 'sentiment-negative';
        return 'sentiment-neutral';
    };

    return (
        <div className="review-list-container">
            <h3>Hasil Analisis Review Tersimpan ({reviews.length})</h3>
            {isLoading && <LoadingSpinner />}
            {error && <p className="error-message"> {error}</p>}
            
            <div className="reviews-grid">
                {reviews.map((review) => (
                    <div key={review.id} className="review-card">
                        <div className={`sentiment-badge ${getSentimentClass(review.sentiment)}`}>
                            {review.sentiment}
                        </div>
                        
                        <p className="review-text">"{review.review_text}"</p>
                        
                        <h4>Poin Utama (Gemini):</h4>
                        <ul className="key-points-list">
                            {review.key_points && review.key_points.length > 0 ? (
                                review.key_points.map((point, index) => (
                                    <li key={index}>**{point}**</li>
                                ))
                            ) : (
                                <li>Tidak ada poin utama yang terekstraksi.</li>
                            )}
                        </ul>
                        <small>ID: {review.id} | {new Date(review.created_at).toLocaleString()}</small>
                    </div>
                ))}
            </div>

            {reviews.length === 0 && !isLoading && !error && (
                <p>Belum ada hasil analisis. Kirimkan ulasan pertama Anda!</p>
            )}
        </div>
    );
};

export default ReviewList;