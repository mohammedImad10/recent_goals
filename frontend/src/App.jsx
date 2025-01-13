import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Navbar from './components/Navbar';
import News from './components/News';
import Matches from './components/Matches';
import RecentGoals from './components/RecentGoals'
import ScorebatEmbed from './components/embed_live_score'


const App = () => {
  return (
    <Router>
      <Navbar />
      <div>
        <Routes>
          <Route path="/news" element={<News />} />
          <Route path="/matches" element={<Matches />} />
          <Route path="/recent-goals" element={<RecentGoals />} />
          <Route path="/games-results" element={<ScorebatEmbed />} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;
