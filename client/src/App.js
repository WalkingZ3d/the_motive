import './App.css';

import * as Pages from './pages';
import { NavBar } from './components';
import { Routes, Route } from 'react-router-dom';

function App() {
  return (
    <div role='app' className="App">
      
      <main>
        <NavBar />
        
        <Routes>
          <Route path="/" element={<Pages.LandingPage />} />
          <Route path="/user" element={<Pages.UserPage />} />
        </Routes>
      </main>
    </div>
  );
}

export default App;
