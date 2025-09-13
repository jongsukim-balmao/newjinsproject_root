import React from 'react';
import { createRoot } from 'react-dom/client';

function App() {
  return (
    <div style={{padding:20}}>
      <h1>newjins Frontend</h1>
      <p>React 개발 서버가 동작 중입니다.</p>
    </div>
  );
}

const container = document.getElementById('root');
const root = createRoot(container);
root.render(<App />);
