import React, { useState, useEffect } from "react";
import axios from "axios";
import imageChambord from './images/chambord.jpg';
import { Link } from "react-router-dom";

import "../style/styleLieux.css";

/**
 * La fonction `Lieux` est un composant React qui récupère les données d'une API et affiche une liste
 * de lieux avec une option de filtre pour sélectionner un département.
 * @returns Le composant `Lieux` renvoie un élément JSX. Il restitue un div avec la classe
 * "indexAccueil" et contient plusieurs éléments imbriqués. Ceux-ci incluent un en-tête, un formulaire
 * avec des boutons radio et un conteneur avec une liste d'éléments. Les éléments de liste sont générés
 * dynamiquement en fonction des données extraites d'un point de terminaison d'API. Chaque élément de
 * la liste contient une image, un lien et du texte.
 */
const Lieux = () => {
  const [lieux, setLieux] = useState([]);
  const [selectedDepartment, setSelectedDepartment] = useState(null);


  const lieuxFiltres = lieux.filter((lieu) => {
    console.log(lieu)
    return selectedDepartment ? lieu.numDepartement === parseInt(selectedDepartment) : true;
  });
  /* Le hook `useEffect` est utilisé pour effectuer des effets secondaires dans les composants
  fonctionnels. Dans ce cas, il est utilisé pour récupérer les données d'un point de terminaison
  d'API lors du montage du composant. */
  useEffect(() => {
    axios.get("http://localhost:8000/api/lieu/")
      .then((response) => {
        const data = response.data;
        setLieux(data);
      })
      .catch((error) => {
        console.error("Erreur lors de la récupération des lieux :", error);
      });
  }, []);

  const departments = ["18", "28", "36", "37", "41", "45"];

  return (
    <div className="indexAccueil">
      <div className="">
        <h1 className="titreLieuxe2e itreBlancLieux d-flex justify-content-center align-items-center p-5">Lieux</h1>
        <div className="filtreLieux d-flex justify-content-center align-items-center">
          <form className="d-flex justify-content-center">
            {departments.map((department) => (
              <div key={department} className="form-check">
                <input
                  type="radio"
                  id={`department${department}`}
                  name="department"
                  value={department}
                  checked={selectedDepartment === department}
                  onChange={() => setSelectedDepartment(department)}
                  className="radioButtonDepLieux"
                />
                <label htmlFor={`department${department}`} className="form-check-label large-number">{department}</label>
              </div>
            ))}
          </form>
        </div>
      </div>

      <div className="container mt-3 pt-3">
        <div className="row">
          <div className="col-sm-3 ">
            <ul className="list-unstyled " style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(350px, 1fr))', gap: '10px', width: '70vw' }}>
              {lieuxFiltres.map((lieu) => (
                <li className="m-3" key={lieu.idLieu}>
                  <Link to={{ pathname: `/lieux/${lieu.idLieu}` }} className="m-3 d-flex flex-column align-items-center">
                    {lieu.imageLieu ? (
                      <img className="ImageCarteLieux" src={process.env.PUBLIC_URL + `/${lieu.imageLieu}`} alt="Carte" />
                    ) : (
                      <img className="ImageCarteLieux" src={process.env.PUBLIC_URL + `/images/artchipelDefault.png`} alt="Carte" />
                    )}
                    <div className="TitreCarteLieux d-flex justify-content-center align-items-center">{lieu.nomLieu}</div>
                  </Link>

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