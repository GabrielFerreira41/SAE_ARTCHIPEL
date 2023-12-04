import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";

const Lieu = () => {
  const { id } = useParams();
  const [lieu, setLieu] = useState(null);

  useEffect(() => {
    axios.get(`http://localhost:8000/api/Lieu/${id}`)
      .then((response) => {
        const data = response.data;
        console.log(data);
        setLieu(data);
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
      <p>Description: {lieu.description}</p>
      <p>Ville: {lieu.ville}</p>
      {/* Ajoutez d'autres détails selon la structure de votre objet lieu */}
    </div>
  );
};

export default Lieu;
