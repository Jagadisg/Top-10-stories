import React, { useEffect, useState } from 'react';
import { fetchTopStories } from '../../api/api';
import './TopStories.css';

const TopStories = () => {
    const [stories, setStories] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const getStories = async () => {
            try {
                const data = await fetchTopStories();
                console.log(data)
                setStories(data);
            } catch (err) {
                setError(err.message);
            } finally {
                setLoading(false);
            }
        };

        getStories();
    }, []);

    if (loading) return <div>Loading...</div>;
    if (error) return <div>Error: {error}</div>;

    return (
        <div>
            <h1>Top 10 Stories</h1>
            <ul className="story-list">
                {stories.map((story, index) => (
                    <React.Fragment key={index}>
                        <li className="story-item">
                            URL: <a href={story.URL} target="_blank" rel="noopener noreferrer">
                                {story.URL} 
                            </a> <span className="star">*</span> Title: {story.Title} <span className="star">*</span> Author: {story.Author} <span className="star">*</span> Score: {story.Score} <span className="star">*</span> Time: {story.Time}
                        </li>
                        <hr />
                    </React.Fragment>
                ))}
            </ul>
        </div>
    );
};

export default TopStories;
