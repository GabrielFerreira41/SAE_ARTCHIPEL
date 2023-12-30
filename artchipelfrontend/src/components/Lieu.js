import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";
import imageChambord from './images/chambord.jpg';
import "../style/styleLieu.css";

/**
 * La fonction ci-dessus est un composant React qui récupère et affiche les détails d'un emplacement
 * spécifique, y compris son nom, sa description et diverses commodités.
 * @returns Le composant renvoie une structure JSX qui représente les détails d'un emplacement
 * spécifique. Il comprend des informations sur l'emplacement, telles que son nom, sa description et
 * diverses commodités telles que le stationnement, les magasins et l'accessibilité. Le composant
 * comprend également une image de l'emplacement et un message de chargement si les données sont
 * toujours en cours de récupération.
 */
const Lieu = () => {
  const { id } = useParams();
  const [lieu, setLieu] = useState(null);

  const oeuvres = [
    {'name':'Pot en verres'},
    {'name':'Status en Bronze'},
    {'name':'Toile'},
    {'name':'Picasso'},
    {'name':'Guernika'},
    {'name':'aefzefazf'},
  ]

  /* Le hook `useEffect` est utilisé pour effectuer des effets secondaires dans les composants
  fonctionnels. Dans ce cas, il est utilisé pour effectuer une requête HTTP GET pour récupérer les
  détails d'un lieu spécifique à l'aide de la bibliothèque `axios`. */
  useEffect(() => {
    axios.get(`http://localhost:8000/api/lieu/${id}/`)
      .then((response) => {
        const data = response.data;
        console.log(data);
        setLieu(data.lieu);
      })
      .catch((error) => {
        console.error("Erreur lors de la récupération des détails du lieu :", error);
      });
  }, [id]);

  if (lieu === null) {
    return <div>Loading...</div>;
  }

  return (
    <div className="main">
      <div className="d-flex mt-5 fondBleu">
        <img src={imageChambord} alt="Château de Chambord" />
        <div className="d-flex align-items-center">
          <div className="container">
            <div className="row">
              <div className="d-flex justify-content-inline">
                <div className="rectangleBleu1"></div>
                <h1>{lieu.nomLieu}</h1>
              </div>

            </div>
            <div className="row">
              <p className="mt-3">{lieu.descriptionLieu}</p>
            </div>

            <div className="row">
              <div className="d-flex justify-content-end">
                <div className="rectangleBleu2"></div>
              </div>
            </div>

          </div>

        </div>
      </div>
      <div className="fondVert">
        <h2 className="titreInformation d-flex justify-content-center">Information</h2>
        <div>
          <ul className="d-flex list-unstyled ulInformation justify-content-center">
            <li className="carteVerte">
              <h4>Tarif Lieu</h4>
              <p>{lieu.tarif.payant === false ? 'Aucun' : lieu.tarif.payant}</p>
            </li>

            <li className="carteVerte">
              <h4>Magasin</h4>
              <p>{lieu.boolShopping === false ? 'Indisponible' : 'Disponible'}</p>
            </li>

            <li className="carteVerte">
              <h4>Restaurant</h4>
              <p>{lieu.boolRepas === false ? 'Indisponible' : 'Disponible'}</p>
            </li>

            <li className="carteVerte">
              <h4>Parking</h4>
              <p>{lieu.boolParking === false ? 'Indisponible' : 'Disponible'}</p>
            </li>

            <li className="carteVerte">
              <h4>Acces Handicapé</h4>
              <p>{lieu.boolAccessibilite === false ? 'Indisponible' : 'Disponible'}</p>
            </li>
          </ul>

        </div>
      </div>
    <div>  
    </div>
    </div>
  );
};

export default Lieu;
