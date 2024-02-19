import React, { useState } from 'react';
import _data from './data.json';

import './App.css';

const App = () => {
  const [data, setData] = useState(_data);

  const headers = data.length > 0 ? Object.keys(data[0]) : [];

  const reset = () => setData(_data);
  const filter = (fn) => setData(data.filter(fn));
  const reverse = () => setData(data.slice().reverse());
  const random = () => setData(data.sort(() => Math.random() - 0.5));
  const map = () => setData(data.map((row) => ({
    ...row,
    age: row.age + 1,
    name: row.name.toLowerCase()
  })));

  return (
    <div className="App">
      <h1>React App</h1>

      <div className="buttons">
        <button onClick={reset} className="reset">
          Reset
        </button>

        <button onClick={() => filter((row) => row.id < 90)} className="filter-id">
          Filter ID
        </button>

        <button onClick={() => filter((row) => row.name.toLowerCase().includes('k'))} className="filter-name">
          Filter Name
        </button>

        <button onClick={() => filter((row) => row.age > 20)} className="filter-age">
          Filter Age
        </button>

        <button onClick={() => filter((row) => row.hobbies.includes('swimming'))} className="filter-hobbies">
          Filter Hobbies
        </button>

        <button onClick={reverse} className="reverse">
          Reverse
        </button>

        <button onClick={random} className="random">
          Random
        </button>

        <button onClick={map} className="map">
          Map
        </button>
      </div>

      <h4>Table ({data.length} rows)</h4>

      <table>
        <thead>
          {headers.map((header, index) => (
            <th key={index}>{header}</th>
          ))}
        </thead>

        <tbody>
          {data.map((row, index) => (
            <tr key={index}>
              {headers.map((header, index) => (
                <td key={index}>{row[header]}</td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;