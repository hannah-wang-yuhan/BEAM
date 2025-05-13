import React, { useState, useEffect } from 'react';
import './UploadPhoto.css'; // 引入CSS文件来进行样式调整

export default function UploadPhoto({ handlePhotoUpload, step, noMakeupPhoto, makeupPhoto, photoType }) {
  const [selectedFile, setSelectedFile] = useState(null); // State to store the selected file
  const [photoPreview, setPhotoPreview] = useState(null); // State for the photo preview

  useEffect(() => {
    // Display the existing photo preview if already uploaded
    if (photoType === 'noMakeup' && noMakeupPhoto) {
      setPhotoPreview(URL.createObjectURL(noMakeupPhoto));
    } else if (photoType === 'makeup' && makeupPhoto) {
      setPhotoPreview(URL.createObjectURL(makeupPhoto));
    }
  }, [noMakeupPhoto, makeupPhoto, photoType]);

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    if (file) {
      // Call the function passed from parent to handle file upload
      handlePhotoUpload(photoType, file);
      setPhotoPreview(URL.createObjectURL(file)); // Update the selected file preview
    }
  };

  return (
    <div className="upload-photo-container">
      {/* Show "+" icon if no file has been selected yet */}
      {!photoPreview ? (
        <label htmlFor="file-input" className="upload-button">
          <span className="plus-icon">+</span>
        </label>
      ) : (
        // Display the uploaded photo once a file is selected
        <div className="uploaded-photo">
          <img src={photoPreview} alt="Uploaded" />
        </div>
      )}
      <input
        id="file-input"
        type="file"
        accept="image/*"
        onChange={handleFileChange}
        className="file-input"
      />
    </div>
  );
}



