import React, { useEffect, useState } from 'react';
import { loadModules } from 'esri-loader';

const Carte = () => {
  const [selectedMonument, setSelectedMonument] = useState(null);
  const [monumentsList, setMonumentsList] = useState([]); // Changement du nom de la variable

  useEffect(() => {
    loadModules(['esri/Map', 'esri/views/MapView', 'esri/layers/GraphicsLayer', 'esri/Graphic', 'esri/widgets/Directions'], { css: true })
      .then(([Map, MapView, GraphicsLayer, Graphic, Directions]) => {
        const map = new Map({
          basemap: 'streets-navigation-vector'
        });

        const view = new MapView({
          container: 'map-view',
          map: map,
          center: [1.32, 47.75], // Coordonnées du Centre-Val de Loire
          zoom: 8
        });

        // Ajout de quelques monuments fictifs
        const monumentsLayer = new GraphicsLayer();
        map.add(monumentsLayer);

        const monuments = [
          { name: 'Château de Chambord', location: [1.515, 47.616] },
          { name: 'Cathédrale de Chartres', location: [1.485, 48.447] },
          // Ajoutez d'autres monuments avec leurs coordonnées
        ];

        monuments.forEach(monument => {
          const point = {
            type: 'point',
            longitude: monument.location[0],
            latitude: monument.location[1]
          };

          const markerSymbol = {
            type: 'simple-marker',
            color: [226, 119, 40],
            outline: {
              color: [255, 255, 255],
              width: 2
            }
          };

          const pointGraphic = new Graphic({
            geometry: point,
            symbol: markerSymbol,
            attributes: {
              name: monument.name
            }
          });

          monumentsLayer.add(pointGraphic);
        });

        // Mettez à jour le state des monuments avec la liste des monuments
        setMonumentsList(monuments);

        // Ajout de la fonctionnalité d'itinéraire
        const directionsWidget = new Directions({
          view: view
        });

        view.ui.add(directionsWidget, 'top-right');

        return () => {
          if (view) {
            // Do any cleanup here
            view.destroy();
          }
        };
      })
      .catch(err => console.error(err));
  }, []); // La dépendance vide assure que le code ne s'exécute qu'une fois

  return (
    <div>
      <div id="map-view" style={{ height: '65vh', width: '100vw' }}></div>
      <ul className="list-group list-group-flush">
        {monumentsList.map((monument, index) => (
          <li key={index} className="list-group-item">
            <div className="card" style={{ cursor: 'pointer' }} onClick={() => setSelectedMonument(monument)}>
              <div className="card-body">
                <h5 className="card-title">{monument.name}</h5>
                <p className="card-text">
                  {/* Vous pouvez ajouter d'autres détails du monument ici */}
                </p>
              </div>
            </div>
          </li>
        ))}
      </ul>


    </div>
  );
};

export default Carte;
