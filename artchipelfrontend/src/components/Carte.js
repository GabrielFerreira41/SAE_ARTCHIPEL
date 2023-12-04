import React, { useEffect, useState } from 'react';
import { loadModules } from 'esri-loader';
import "../style/styleCarte.css";

const Carte = () => {
  const [selectedMonument, setSelectedMonument] = useState(null);
  const [monumentsList, setMonumentsList] = useState([]);
  let view;

  useEffect(() => {
    loadModules(['esri/Map', 'esri/views/MapView', 'esri/layers/GraphicsLayer', 'esri/Graphic', 'esri/widgets/Directions', 'esri/widgets/Popup'], { css: true })
      .then(([Map, MapView, GraphicsLayer, Graphic, Directions, Popup]) => {
        const map = new Map({
          basemap: 'streets-navigation-vector'
        });

        view = new MapView({
          container: 'map-view',
          map: map,
          center: [1.32, 47.75],
          zoom: 8
        });

        const monumentsLayer = new GraphicsLayer();
        map.add(monumentsLayer);

        const monuments = [
          { name: 'Château de Chambord', location: [1.515, 47.616] },
          { name: 'Cathédrale de Chartres', location: [1.485, 48.447] },
          { name: 'Château de Chenonceau', location: [1.0707, 47.3244] },
          { name: 'Château d\'Amboise', location: [0.9845, 47.4108] },
          { name: 'Château de Villandry', location: [0.5110, 47.3423] },
          { name: 'Château d\'Azay-le-Rideau', location: [0.4725, 47.2613] },
          { name: 'Château de Blois', location: [1.3307, 47.5861] },
          { name: 'Château de Cheverny', location: [1.4552, 47.5077] },
          { name: 'Château de Loches', location: [1.0041, 47.1284] },
          { name: 'Château de Chinon', location: [0.2454, 47.1676] },
          { name: 'Château de Montpoupon', location: [0.9833, 47.2167] },
          { name: 'Château de Chaumont-sur-Loire', location: [0.9760, 47.4826] },
          { name: 'Château de Valençay', location: [1.5736, 47.1624] },
          { name: 'Château de Langeais', location: [0.4045, 47.3307] },
          { name: 'Château de Sully-sur-Loire', location: [2.3832, 47.7803] },
          { name: 'Château de Gien', location: [2.6340, 47.6876] },
          { name: 'Château de Meung-sur-Loire', location: [1.6947, 47.8202] },
          { name: 'Château de La Ferté-Saint-Aubin', location: [1.9583, 47.8151] },
          { name: 'Château de Saumur', location: [-0.2458, 47.2623] },
          { name: 'Château de Brissac', location: [-0.5520, 47.3590] },
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

          const popupTemplate = {
            title: '{name}',
            content: 'Détails du monument'
          };

          pointGraphic.popupTemplate = popupTemplate;

          monumentsLayer.add(pointGraphic);
        });

        monumentsLayer.on('click', event => {
          setSelectedMonument(event.graphic.attributes);
          // Centrer et zoomer sur le monument sélectionné
          view.goTo({
            target: event.graphic.geometry,
            zoom: 12
          });
        });

        setMonumentsList(monuments);

        const directionsWidget = new Directions({
          view: view
        });

        view.ui.add(directionsWidget, 'top-right');

        return () => {
          if (view) {
            view.destroy();
          }
        };
      })
      .catch(err => console.error(err));
  }, []);

  useEffect(() => {
    if (selectedMonument && view) {
      // Ouvrir le popup lorsque le monument est sélectionné
      view.popup.open({
        title: selectedMonument.name,
        content: 'Détails du monument'
      });
    }
  }, [selectedMonument]);

  return (
    <div className='main'>
      <div className='d-flex mt-5'>
        <div id="map-view" style={{ height: '65vh', width: '75vw' }}></div>
        <h1 className='d-flex titreCarte justify-content-center align-items-center'>Carte</h1>
      </div>
      <section className='d-flex'>
        <h1 className='d-flex titreListeLieux justify-content-center align-items-center'>Liste des monuments</h1>
        <ul className="list-group d-flex flex-wrap listeLieu">
          {monumentsList.map((monument, index) => (
            <li key={index} className="list-group-item" onClick={() => setSelectedMonument(monument)}>
              <div className="card monument-card border-primary mb-3" style={{ width: '14rem' }}>
                {/* Ajoutez la classe "text-center" pour centrer le contenu de la carte */}
                <div className="card-body text-center">
                  <h5 className="card-title text-primary">{monument.name}</h5>
                  <p className="card-text text-muted">
                    {/* Vous pouvez ajouter d'autres détails du monument ici */}
                  </p>
                </div>
              </div>
            </li>
          ))}
        </ul>

      </section>
    </div>
  );
};

export default Carte;
