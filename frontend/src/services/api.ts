import axios from 'axios';

const API_BASE_URL = 'http://localhost:5000';

export interface ContentRecommendation {
  title: string;
  description: string;
  similarity: number;
}

interface RecommendationResponse {
  recommendations: ContentRecommendation[];
}

export const getRecommendations = async (
  title: string,
  contentType: string = 'movies',
  count: number = 5
): Promise<ContentRecommendation[]> => {
  try {
    const response = await axios.post(`${API_BASE_URL}/recommend`, {
      title,
      content_type: contentType,
      count,
    });

    if (response.data.error) {
      throw new Error(response.data.error);
    }

    return response.data.recommendations;
  } catch (error) {
    if (axios.isAxiosError(error)) {
      if (error.response?.data?.error) {
        throw new Error(error.response.data.error);
      }
      throw new Error('Failed to fetch recommendations. Please try again.');
    }
    throw new Error('An unexpected error occurred');
  }
}
