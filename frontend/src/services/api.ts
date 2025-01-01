import axios from 'axios';

const API_BASE_URL = 'http://localhost:5000';

interface RecommendationResponse {
  recommendations: string[];
}

export async function getRecommendations(title: string, recommendationCount: number): Promise<RecommendationResponse> {
  try {
    const response = await axios.post<RecommendationResponse>(`${API_BASE_URL}/recommend`, {
      title: title,
      count: recommendationCount
    });
    return response.data;
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
