import React, { useState } from 'react';
import './UploadText.css';  // 引入CSS样式

export default function UploadText({ handleMakeupStyle, makeupStyle }) {
  const [style, setStyle] = useState(makeupStyle || '');

  const handleInputChange = (event) => {
    const value = event.target.value;
    setStyle(value);
    handleMakeupStyle(value);
  };

  return (
    <div className="upload-text-container">
      <div className="style-text">
        {style && <p>Entered Style: {style}</p>}
      </div>
      <textarea
        value={style}
        onChange={handleInputChange}
        placeholder="Describe the expected makeup style"
        className="upload-text-area"
      />
    </div>
  );
}


