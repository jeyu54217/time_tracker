import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'https://your-api-base-url.com',
  // You can add more default settings here
});

export default apiClient;
 