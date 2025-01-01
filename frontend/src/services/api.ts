import axios, { AxiosError } from 'axios';

const API_URL = 'http://localhost:5000';

export const getRecommendations = async (title: string) => {
  try {
    const response = await axios.post(`${API_URL}/recommend`, {
      title,
      count: 5
    });
    return response.data;
  } catch (error: unknown) {
    if (error instanceof AxiosError && error.response?.data?.error) {
      throw new Error(error.response.data.error);
    }
    throw new Error('Failed to get recommendations');
  }
};
