import React, { useState } from 'react';

export default function MarketResearchForm() {
  const [investmentSector, setInvestmentSector] = useState('');
  const [newsSite, setNewsSite] = useState('');
  const [articleText, setArticleText] = useState('');
  const [marketData, setMarketData] = useState([]);
  const [chartUrl, setChartUrl] = useState('');
  const [insights, setInsights] = useState([]);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    if (name === 'investmentSector') {
      setInvestmentSector(value);
    } else if (name === 'newsSite') {
      setNewsSite(value);
    }
  };


  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch('http://localhost:5000/generate-insights', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          newsSite,
        }),
      });
  
      if (!response.ok) {
        throw new Error('Failed to fetch insights from the backend.');
      }
  
      const data = await response.json();
      setMarketData(data.market_data);
  
    } catch (error) {
      console.error(error);
      alert('Error: Failed to fetch insights from the backend.');
    }
  };
  

  return (
    <div>
      <h2>Generate Market Research Insights</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="investmentSector">Investment Sector:</label>
          <input
            type="text"
            id="investmentSector"
            name="investmentSector"
            value={investmentSector}
            onChange={handleInputChange}
            required
          />
        </div>
        <div>
          <label htmlFor="newsSite">News Site URL:</label>
          <input
            type="text"
            id="newsSite"
            name="newsSite"
            value={newsSite}
            onChange={handleInputChange}
            required
          />
        </div>
        <button type="submit">Generate Insights</button>
      </form>

      {articleText && (
        <div>
          <h3>Article Text:</h3>
          <p>{articleText}</p>
        </div>
      )}

      {marketData && marketData.length > 0 && (
        <div>
          <h3>Market Data:</h3>
          <ul>
            {marketData.map((item, index) => (
              <li key={index}>{item}</li>
            ))}
          </ul>
        </div>
      )}

      {chartUrl && (
        <div>
          <h3>Chart:</h3>
          <img src={chartUrl} alt="S&P 500 Performance" />
        </div>
      )}

      <div>
        <h3>Insights:</h3>
        <ul>
          {insights && insights.length > 0 ? (
            insights.map((insight, index) => (
              <li key={index}>{insight}</li>
            ))
          ) : (
            <li>No insights found.</li>
          )}
        </ul>
      </div>
    </div>
  );
}
