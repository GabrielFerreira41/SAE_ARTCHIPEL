import React, {useEffect, useState } from 'react';
import '../style/styleHeader.css';

import { Link } from 'react-router-dom';
/**
 * Le composant Header est une barre de navigation avec une barre de recherche.
 * @returns Le composant Header renvoie un élément d'en-tête avec une barre de navigation et une barre
 * de recherche.
 */

const Header = () => {

  const [isLoggedIn, setIsLoggedIn] = useState(false);

  useEffect(() => {
    // Vérifier si l'utilisateur est déjà connecté en vérifiant la présence du token dans le localStorage
    const storedToken = localStorage.getItem('token');
    setIsLoggedIn(!!storedToken); // Mise à jour de l'état en fonction de la présence du token
  }, []);

  const handleLogout = () => {
    // Supprimer le token du localStorage ou effectuer toute autre logique de déconnexion
    localStorage.removeItem('token');
    localStorage.removeItem('tokenrefresh');
    setIsLoggedIn(false); // Mettre à jour l'état pour refléter la déconnexion
  };

  return (
    <header className='d-flex'>
      <nav class="navbar navbar-expand-lg navbar-light navHeader">
        <div class="collapse navbar-collapse navbarNav">
          <ul class="navbar-nav">
            <li class="nav-item">
              <a href={`/`} class="nav-link fs-5">Accueil</a>
            </li>
            <li class="nav-item">
              <a href={`/Decouverte`} class="nav-link fs-5">Découverte</a>
            </li>
            <li class="nav-item">
              <a href={`/Parcours`} class="nav-link fs-5">Parcours</a>
            </li>
          </ul>
          <div className='Bleu'></div>
          <div className='Blanc'></div>
          <div className='Rouge'></div>
        </div>

        <form class="form-inline mr-4">
          <input class="form-control me-sm-2" type="search" placeholder="Lieux / Parcours / Oeuvres"></input>
          <button class="btn btn-secondary my-2 my-sm-0" type="submit">Search</button>
        </form>


        {isLoggedIn ? (
        
        <div class="col-1">
          <a href={'/Accueil'} onClick={handleLogout}>Déconnexion</a>
        </div>
      ) : (
        <div class="col-1">
          <a href={`/Connexion`}>Connexion</a>
        </div>
      )}
        

      </nav>




    </header>
  );
};

export default Header;
