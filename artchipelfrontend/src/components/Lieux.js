import React, { useState, useEffect } from "react";
import axios from "axios";
import { Link } from "react-router-dom";

import "../style/styleLieux.css";

const Lieux = () => {
  const [lieux, setLieux] = useState([]);
  const [totalLieux,setTotalLieux]= useState([]);
  useEffect(() => {
    axios.get("https://data.centrevaldeloire.fr/api/explore/v2.1/catalog/datasets/patrimoine-architectural-en-region-centre-val-de-loire/records")
      .then((response) => {
        const data = response.data.results;
        console.log(data)
        setLieux(data);

        const total = response.data.total_count
        console.log(total)
        setTotalLieux(total);

      })
      .catch((error) => {
        console.error("Erreur lors de la récupération des lieux :", error);
      });
  }, []);

  return (
    <div className="indexAccueil">
      <div className="bandeauBleue">
        <h1 className="titreBlanc p-5">Lieux</h1>
        <h2>{totalLieux}</h2>
      </div>

      <div className="container mt-3 pt-3">
        <div className="row">
          <div className="col-sm-3">
            <h2>Départements</h2>
            <ul className="list-unstyled" style={{ display: 'grid', gridTemplateColumns: 'repeat(5, 1fr)', gap: '10px' }}>
  {lieux.map((lieu) => (
    <li key={lieu.id}>
      <div className="card mb-3" style={{ width: '220px', minHeight: '200px' }}>
        <div className="card-body">
          <Link to={`/lieux/${lieu.id}`}>{lieu.appelation}</Link>
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
