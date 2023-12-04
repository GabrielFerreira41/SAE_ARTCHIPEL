import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";
import imageChambord from './images/chambord.jpg';
import "../style/styleLieu.css";

const Lieu = () => {
  const { id } = useParams();
  const [lieu, setLieu] = useState(null);

  useEffect(() => {
    axios.get(`http://localhost:8000/api/Lieu/${id}/`)
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
    <div className="main">
      <div className="d-flex mt-5">
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
              <p className="mt-3">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed tincidunt diam nulla, eget laoreet tortor dignissim tincidunt. Proin nec suscipit purus, nec sodales nulla. Fusce dolor lacus, tempor ac cursus a, tempus a justo. Duis posuere augue nec lectus aliquam, ut pulvinar enim rutrum. Donec nulla tortor, viverra ac nunc vel, blandit rutrum sem. Mauris tempor sed tortor at convallis. Cras vitae ligula ultricies, porttitor odio ullamcorper, ultrices elit. In hac habitasse platea dictumst. Nulla nibh sapien, euismod tempus enim ut, volutpat efficitur arcu. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Suspendisse dapibus turpis mi, vitae congue ex iaculis ut. Quisque a semper mi. Donec sed pellentesque dolor. Nunc at scelerisque nibh. Vivamus ligula dolor, consequat non lectus sit amet, ullamcorper convallis tortor. </p>
            </div>

            <div className="row">
            <div className="d-flex justify-content-end">
              <div className="rectangleBleu2"></div>
            </div>
            </div>

          </div>
          
                  </div>
      </div>
      <div>
        <h2>Information</h2>
        <div>
          {/* ajouter les cartes */}
        </div>
      </div>
    </div>
  );
};

export default Lieu;
