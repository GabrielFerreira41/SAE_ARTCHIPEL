import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link, Navigate } from 'react-router-dom';

import Accueil from './components/Accueil';
import Lieux from './components/Lieux';
import Info from './components/Info';
import Decouverte from './components/Decouverte';
import Evenement from './components/Evenement';
import Carte from './components/Carte';
import Lieu from './components/Lieu';
import Connexion from './components/Connexion';

function PageNotFound() {
  return (
    <div>
      <h1>404 - Page Not Found</h1>
      {/* Ajoutez un lien pour rediriger vers la page d'accueil */}
      <Link to="/">Retour à l'accueil</Link>
    </div>
  );
}

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Accueil />} />
        <Route path="/Lieux" element={<Lieux />} />
        <Route path="/lieux/:id" element={<Lieu />} />
        <Route path="/Info" element={<Info />} />
        <Route path="/Decouverte" element={<Decouverte />} />
        <Route path="/Evenement" element={<Evenement />} />
        <Route path="/Carte" element={<Carte />} />
        <Route path="/Connexion" element={<Connexion />} />
        {/* Ajoutez la route de secours */}
        <Route path="*" element={<PageNotFound />} />
      </Routes>
    </Router>
  );
}

export default App;
