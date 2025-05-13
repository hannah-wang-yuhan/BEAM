import React, { useState } from 'react';
import axios from 'axios';
import { Loader } from 'lucide-react'; // <-- 引入 Spinner 图标
import './APIConnection.css';

const APIConnection = ({ noMakeupPhoto, makeupPhoto, makeupStyle, onResult }) => {
  const [isLoading, setIsLoading] = useState(false);
  const [isSuccess, setIsSuccess] = useState(false);

  const sendRequest = async () => {
    if (!noMakeupPhoto || !makeupPhoto || !makeupStyle) {
      alert("Please upload both photos and describe the makeup style.");
      return;
    }

    setIsLoading(true);
    setIsSuccess(false);

    const formData = new FormData();
    formData.append('noMakeupPhoto', noMakeupPhoto);
    formData.append('makeupPhoto', makeupPhoto);
    formData.append('makeupStyle', makeupStyle);

    try {
      const response = await axios.post('http://localhost:8000/makeup-check', formData, {
        headers: { 'Content-Type': 'multipart/form-data' },
      });

      if (onResult) onResult(response.data);
      setIsSuccess(true);
    } catch (error) {
      console.error("Error:", error);
      alert("An error occurred while sending the request.");
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="api-connection">
      <button
        className={`big-submit-button ${isLoading ? 'loading' : ''} ${isSuccess ? 'success' : ''}`}
        onClick={sendRequest}
        disabled={isLoading || isSuccess}
      >
        {isSuccess ? '✔' : isLoading ? <Loader className="spinner-icon" /> : 'Start'}
      </button>
    </div>
  );
};

export default APIConnection;






