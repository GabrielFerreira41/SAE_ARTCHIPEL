/* Le code importe divers composants et modules de la bibliothèque « react-router-dom » et des fichiers
locaux. */
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
import Parcours from './components/Parcours';

/**
 * La fonction renvoie un élément JSX pour un message d'erreur 404 page introuvable avec un lien pour
 * revenir à la page d'accueil.
 * @returns un élément JSX.
 */
function PageNotFound() {
  return (
    <div className="container d-flex justify-content-center bg-success  p-5">
      <div className="text-center">
        <h1>404 - Page Not Found</h1>
        <p>Sorry, the page you are looking for might be in another castle.</p>
        <Link className="btn btn-primary" to="/">
          Retour à l'accueil
        </Link>
      </div>
    </div>
  );
}

/**
 * La fonction configure le routage pour différents chemins dans une application React.
 * @returns Le composant App renvoie un composant Router de React Router. À l'intérieur du composant
 * Routeur, il existe plusieurs composants Route qui définissent les différents chemins et leurs
 * composants correspondants à restituer. Les composants rendus pour chaque chemin incluent Accueil,
 * Lieux, Lieu, Info, Découverte, Evenement, Carte, Connexion et Parcours. De plus, il existe un
 * composant Route avec un
 */
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
        <Route path="/Parcours" element={<Parcours />} />
        {/* Ajoutez la route de secours */}
        <Route path="*" element={<PageNotFound />} />
      </Routes>
    </Router>
  );
}

export default App;
