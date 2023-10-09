import React, { useState, useEffect } from "react";
import axios from "axios"; // Utilisez axios ou une autre bibliothèque pour récupérer des données depuis une base de données

import "../style/styleEvenement.css";

const Accueil = () => {
  return (
    <div className="indexAccueil">
      <div className="bandeauRose"><h1 className="titreBlanc p-5">Evenement</h1></div>
      <div className="container mt-3 pt-3">
        <div className="row">
          <div className="col-sm-3">
          </div>
          <div className="col-sm-9">
            <ul>
              {/* {lieux.map((lieu) => (
                <li key={lieu.id}>{lieu.nom}</li>
              ))} */}
              <li>Lieux 1</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Accueil;
