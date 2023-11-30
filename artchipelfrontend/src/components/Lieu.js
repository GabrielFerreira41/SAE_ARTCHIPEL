// Lieu.js
import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";

const Lieu = () => {
  const { id } = useParams(); // Obtenez l'ID de la route
  const [lieu, setLieu] = useState(null);

  useEffect(() => {
    // Effectuez la requête HTTP pour récupérer les détails du lieu en fonction de l'ID
    // axios.get(`https://data.centrevaldeloire.fr/api/explore/v2.1/catalog/datasets/patrimoine-architectural-en-region-centre-val-de-loire/records/${id}`)
    axios.get("http://localhost:8000/api/Lieu/")
      .then((response) => {
        // Mettez à jour l'état avec les données reçues de l'API
        setLieu(response.data);
      })
      .catch((error) => {
        console.error("Erreur lors de la récupération des détails du lieu :", error);
      });
  }, [id]);

  if (lieu === null) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <h1>{lieu.nomLieu}</h1>
      {/* Affichez les détails du lieu ici */}
    </div>
  );
};

export default Lieu;
