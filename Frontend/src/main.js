import React, { useState } from 'react';
import UploadPhoto from './components/UploadPhoto';
import UploadText from './components/UploadText';
import APIConnection from './components/APIConnection';
import APIResults from './components/APIResults';
import './main.css';

const steps = [
  { text: 'Step 1: Upload the no-makeup photo', Component: UploadPhoto, photoType: 'noMakeup' },
  { text: 'Step 2: Upload the makeup photo', Component: UploadPhoto, photoType: 'makeup' },
  { text: 'Step 3: Describe the expected makeup style', Component: UploadText },
  { text: 'Step 4: Wait for makeup check', Component: APIConnection },
  { text: 'Step 5: Basic style check', Component: APIResults, dataKey: 'makeupDescription' },
  { text: 'Step 6: Makeup detail check', Component: APIResults, dataKey: 'analyzeFacialMakeup' },
  ///{ text: 'Step 7: Makeup correction', Component: APIResults },
];

const Main = () => {
  const [step, setStep] = useState(0);

  // State to store photos and makeup style for each step
  const [noMakeupPhoto, setNoMakeupPhoto] = useState(null); // State for no-makeup photo
  const [makeupPhoto, setMakeupPhoto] = useState(null); // State for makeup photo
  const [makeupStyle, setMakeupStyle] = useState(''); // State for makeup style
  const [makeupDescription, setMakeupDescription] = useState(null);
  const [analyzeFacialMakeup, setAnalyzeFacialMakeup] = useState(null);

  // Function to handle photo upload
  const handlePhotoUpload = (photoType, file) => {
    if (photoType === 'noMakeup') {
      setNoMakeupPhoto(file);
    } else if (photoType === 'makeup') {
      setMakeupPhoto(file);
    }
  };

  // Function to handle makeup style description
  const handleMakeupStyle = (style) => {
    setMakeupStyle(style);
  };

  // Get the current step's component
  const StepUI = steps[step].Component;
  const dataKey = steps[step].dataKey;

  return (
    <div className="main">
      <div className="step-header">
        <button onClick={() => setStep((s) => Math.max(0, s - 1))} disabled={step === 0}>
          Previous
        </button>
        <h2>{steps[step].text}</h2>
        <button onClick={() => setStep((s) => Math.min(steps.length - 1, s + 1))} disabled={step === steps.length - 1}>
          Next
        </button>
      </div>

      <StepUI
        key={step}
        step={step}
        handlePhotoUpload={handlePhotoUpload}
        handleMakeupStyle={handleMakeupStyle}
        noMakeupPhoto={noMakeupPhoto}
        makeupPhoto={makeupPhoto}
        makeupStyle={makeupStyle}
        photoType={steps[step].photoType}
        onResult={(res) => {
          if (res.makeup_description) setMakeupDescription(res.makeup_description);
          if (res.analyze_facial_makeup) setAnalyzeFacialMakeup(res.analyze_facial_makeup);
        }}
        data={
          dataKey === 'makeupDescription' ? makeupDescription :
            dataKey === 'analyzeFacialMakeup' ? analyzeFacialMakeup :
              null
        }
      />
    </div>
  );
};

export default Main;
