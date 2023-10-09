import React, { useState, useEffect } from "react";
import axios from "axios";

import "../style/styleLieux.css";

const Lieux = () => {
  const [lieux, setLieux] = useState([]);

  useEffect(() => {
    // Effectuez la requête HTTP pour récupérer les lieux depuis l'API
    axios.get("https://data.centrevaldeloire.fr/api/explore/v2.1/catalog/datasets/patrimoine-architectural-en-region-centre-val-de-loire/records?limit=20")
      .then((response) => {
        // Mettez à jour l'état avec les données reçues de l'API
        setLieux(response.data.results);
      })
      .catch((error) => {
        console.error("Erreur lors de la récupération des lieux :", error);
      });
  }, []); // Le tableau vide en second argument garantit que cet effet ne se déclenche qu'une seule fois lors du montage du composant.

  return (
    <div className="indexAccueil">
      <div className="bandeauBleue">
        <h1 className="titreBlanc p-5">Monument</h1>
      </div>

      <div className="container mt-3 pt-3">
        <div className="row">
          <div className="col-sm-3">
            <h2>Départements</h2>
            <ul className="list-unstyled">
              {Object.keys(lieux).map((key) => (
                <li key={key}>
                  <div className="card mb-3">
                    <div className="card-body">
                      {lieux[key]['appelation']}
                    </div>
                  </div>
                </li>
              ))}
            </ul>
          </div>
          <div className="col-sm-9">
            <ul>
              {/* Affichez d'autres détails sur les lieux ici */}
            </ul>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Lieux;
