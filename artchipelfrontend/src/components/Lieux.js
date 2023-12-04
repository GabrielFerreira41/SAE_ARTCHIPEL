import React, { useState, useEffect } from "react";
import axios from "axios";
import { Link } from "react-router-dom";

import "../style/styleLieux.css";

const Lieux = () => {
  const [lieux, setLieux] = useState([]);

  useEffect(() => {
    axios.get("http://localhost:8000/api/Lieu/")
      .then((response) => {
        const data = response.data;
        setLieux(data);
      })
      .catch((error) => {
        console.error("Erreur lors de la récupération des lieux :", error);
      });
  }, []);

  return (
    <div className="indexAccueil">
      <div className="">
        <h1 className="titreBlanc p-5">Lieux</h1>
      </div>

      <div className="container mt-3 pt-3">
        <div className="row">
          <div className="col-sm-3">
            <ul className="list-unstyled" style={{ display: 'grid', gridTemplateColumns: 'repeat(5, 1fr)', gap: '10px' }}>
              {lieux.map((lieu) => (
                <li key={lieu.idLieu}>
                  <div className="card mb-3 bg-info" style={{ width: '220px', minHeight: '200px' }}>
                    <div className="card-body text-white">
                      <Link
                        to={{
                          pathname: `/lieux/${lieu.idLieu}`,
                          state: { lieuData: lieu.nomLieu }  // Passer le dictionnaire du lieu via le state
                        }}
                        className="text-white"
                      >
                        {lieu.nomLieu}
                      </Link>
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
