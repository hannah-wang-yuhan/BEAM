import React, { useState } from 'react';
import './APIResults.css';

const APIResults = ({ data }) => {
  const keys = data ? Object.keys(data) : [];
  const [activeIndex, setActiveIndex] = useState(0);
  const activeKey = keys[activeIndex];
  const activeData = data ? data[activeKey] : null;

  if (!data) {
    return <div className="api-results">No result data yet.</div>;
  }

  return (
    <div className="api-results">
      {/* 激活卡片内容 */}
      <div className="result-card">
        <h3 className="card-title">{activeKey}</h3>
        <div className="result-content">
          {typeof activeData === 'object' ? (
            Object.entries(activeData).map(([subKey, subVal], idx) => (
              <div key={idx} className="result-item">
                <strong>{subKey}:</strong> <span>{subVal}</span>
              </div>
            ))
          ) : (
            <p>{activeData}</p>
          )}
        </div>
      </div>

      {/* 卡片选择器移到底部 */}
      <div className="card-tabs-bottom">
        {keys.map((key, index) => (
          <button
            key={key}
            className={`card-tab ${index === activeIndex ? 'active' : ''}`}
            onClick={() => setActiveIndex(index)}
          >
            {key}
          </button>
        ))}
      </div>
    </div>
  );
};

export default APIResults;


