// 
import React, { useState, useEffect } from "react";
import { getHighlights } from "./highlightService"; // Adjust the path as needed
import "./RecentGoals.module.css";

const RecentGoals = () => {
    const [highlights, setHighlights] = useState([]);
    const [currentPage, setCurrentPage] = useState(1);
    const [totalPages, setTotalPages] = useState(0);

    useEffect(() => {
        const fetchHighlights = async () => {
            try {
                const data = await getHighlights(currentPage);
                setHighlights(data.highlights);
                setTotalPages(data.total_pages);
            } catch (error) {
                console.error("Error fetching highlights:", error);
            }
        };

        fetchHighlights();
    }, [currentPage]);

    const handleNext = () => {
        if (currentPage < totalPages) {
            setCurrentPage(currentPage + 1);
        }
    };

    const handlePrevious = () => {
        if (currentPage > 1) {
            setCurrentPage(currentPage - 1);
        }
    };

    return (
        <div className="recent-goals">
            {highlights.map((highlight) => (
                <div key={highlight.id} className="card">
                    <h3>{highlight.title}</h3>
                    <p><strong>Competition:</strong> {highlight.competition}</p>
                    <p><strong>Date:</strong> {highlight.date}</p>
                    <div
                        className="video-container"
                        dangerouslySetInnerHTML={{ __html: highlight.embed_video }}
                    />
                </div>
            ))}
            <div className="pagination">
                <button onClick={handlePrevious} disabled={currentPage === 1}>
                    Previous
                </button>
                <span>Page {currentPage} of {totalPages}</span>
                <button onClick={handleNext} disabled={currentPage === totalPages}>
                    Next
                </button>
            </div>
        </div>
    );
};

export default RecentGoals;
