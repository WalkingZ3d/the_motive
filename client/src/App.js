import './index.css';

import * as Pages from './pages';
import { Routes, Route } from 'react-router-dom';

function App() {
  return (
    <div id='app' className="container">
      
      <main>


        <Routes>
          <Route path="/" element={<Pages.LandingPage />} />
        </Routes>
      </main>
    </div>
  );
}

export default App;
