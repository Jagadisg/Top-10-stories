import axios from 'axios';


const apiServer = `${process.env.REACT_APP_CONFIG_API_SERVER}/api/hacker_news/top_10_stories/`;

export const fetchTopStories = async () => {
    try {
        const res = await axios.get(apiServer);
        console.log(res.data)
        return res.data;
    } catch (error) {
        console.error("Error with top stories api:", error);
        throw error;
    }
};
