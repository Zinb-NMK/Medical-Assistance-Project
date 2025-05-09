import axios from 'axios';

const API_BASE_URL = 'http://127.0.0.1:8000';

export const predictDisease = async (symptoms: string[]) => {
  try {
    const response = await axios.post(`${API_BASE_URL}/predict_general_disease`, { symptoms });
    return response.data;
  } catch (error) {
    console.error('Error predicting disease:', error);
  }
};

export const predictCancer = async (symptoms: string[]) => {
  try {
    const response = await axios.post(`${API_BASE_URL}/predict_cancer`, { symptoms });
    return response.data;
  } catch (error) {
    console.error('Error predicting cancer:', error);
  }
};

export const fetchNearbyHospitals = async (location: string) => {
  try {
    const response = await axios.get(`${API_BASE_URL}/find_hospitals?location=${location}`);
    return response.data;
  } catch (error) {
    console.error('Error fetching hospitals:', error);
  }
};

export const sendMessageToChatbot = async (message: string) => {
  try {
    const response = await axios.post(`${API_BASE_URL}/chatbot_response`, { message });
    return response.data;
  } catch (error) {
    console.error('Error communicating with chatbot:', error);
  }
};