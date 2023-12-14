import React, { useState, useEffect } from "react";
import axios from "axios";
import imageChambord from './images/chambord.jpg';
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
        <h1 className="d-flex justify-content-center align-items-center titreBlanc p-5">Lieux</h1>
      </div>

      <div className="container mt-3 pt-3">
        <div className="row">
          <div className="col-sm-3">
            <ul className="list-unstyled" style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(350px, 1fr))', gap: '10px' ,width:'70vw'}}>
              {lieux.map((lieu) => (
                <li className="" key={lieu.idLieu}>
                  <div className="m-3">
                    <img className="ImageCarteLieux" src={imageChambord} alt="Carte" />
                    <Link to={{ pathname: `/lieux/${lieu.idLieu}` }} className="TitreCarteLieux d-flex justify-content-center align-items-center">{lieu.nomLieu}</Link>
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
