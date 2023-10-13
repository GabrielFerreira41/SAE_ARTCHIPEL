import React, { useState, useEffect } from "react";
import axios from "axios";
import { Link } from "react-router-dom";

import "../style/styleLieux.css";

const Lieux = () => {
  const [lieux, setLieux] = useState([]);

  useEffect(() => {
    axios.get("https://data.centrevaldeloire.fr/api/explore/v2.1/catalog/datasets/patrimoine-architectural-en-region-centre-val-de-loire/records?limit=20")
      .then((response) => {
        const data = response.data.results;
        setLieux(data);
      })
      .catch((error) => {
        console.error("Erreur lors de la récupération des lieux :", error);
      });
  }, []);

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
              {lieux.map((lieu) => (
                <li key={lieu.id}>
                  <div className="card mb-3">
                    <div className="card-body">
                       <Link to={`/lieux/${lieu}`}>{lieu.appelation}</Link> {/*CHANGER ET METTRE L'ID DU LIEU CORRETC EN FONCTION DE L'API */}
                    </div>
                  </div>
                </li>
              ))}
            </ul>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Lieux;
