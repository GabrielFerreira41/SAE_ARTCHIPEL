import React, { useEffect, useState } from 'react';
import { loadModules } from 'esri-loader';
import 'slick-carousel/slick/slick.css';
import 'slick-carousel/slick/slick-theme.css';
import '../style/styleCarte.css';
import loupe from './images/loupeBlanc.png';


const Carte = () => {
  const [selectedMonument, setSelectedMonument] = useState(null);
  const [monumentsList, setMonumentsList] = useState([]);
  const [currentPage, setCurrentPage] = useState(1);
  const [selectedMap, viewMonumentOnMap] = useState(null);
  const [searchTerm, setSearchTerm] = useState('');
  const [showInfoPanel, setShowInfoPanel] = useState(false);
  const itemsPerPage = 6;
  let view;

  useEffect(() => {
    loadModules([
      'esri/Map',
      'esri/views/MapView',
      'esri/layers/GraphicsLayer',
      'esri/Graphic',
      'esri/widgets/Directions',
      'esri/widgets/Search',
      'esri/widgets/Popup',
    ], { css: true })
      .then(([Map, MapView, GraphicsLayer, Graphic, Directions, Search]) => {
        const map = new Map({
          basemap: 'streets-navigation-vector',
        });

        view = new MapView({
          container: 'map-view',
          map: map,
          center: [1.32, 47.75],
          zoom: 8,
        });

        const monumentsLayer = new GraphicsLayer();
        map.add(monumentsLayer);

        const monuments = [
          { id: 1, name: 'Château de Chambord', location: [1.515, 47.616] },
          { id: 2, name: 'Cathédrale de Chartres', location: [1.485, 48.447] },
          { id: 3, name: 'Château de Chenonceau', location: [1.0707, 47.3244] },
          { id: 4, name: 'Château d\'Amboise', location: [0.9845, 47.4108] },
          { id: 5, name: 'Château de Villandry', location: [0.5110, 47.3423] },
          { id: 6, name: 'Château d\'Azay-le-Rideau', location: [0.4725, 47.2613] },
          { id: 7, name: 'Château de Blois', location: [1.3307, 47.5861] },
          { id: 8, name: 'Château de Cheverny', location: [1.4552, 47.5077] },
          { id: 9, name: 'Château de Loches', location: [1.0041, 47.1284] },
          { id: 10, name: 'Château de Chinon', location: [0.2454, 47.1676] },
          { id: 11, name: 'Château de Montpoupon', location: [0.9833, 47.2167] },
          { id: 12, name: 'Château de Chaumont-sur-Loire', location: [0.9760, 47.4826] },
          { id: 13, name: 'Château de Valençay', location: [1.5736, 47.1624] },
          { id: 14, name: 'Château de Langeais', location: [0.4045, 47.3307] },
          { id: 15, name: 'Château de Sully-sur-Loire', location: [2.3832, 47.7803] },
          { id: 16, name: 'Château de Gien', location: [2.6340, 47.6876] },
          { id: 17, name: 'Château de Meung-sur-Loire', location: [1.6947, 47.8202] },
          { id: 18, name: 'Château de La Ferté-Saint-Aubin', location: [1.9583, 47.8151] },
          { id: 19, name: 'Château de Saumur', location: [-0.2458, 47.2623] },
          { id: 20, name: 'Château de Brissac', location: [-0.5520, 47.3590] },
        ];

        monuments.forEach(monument => {
          const point = {
            type: 'point',
            longitude: monument.location[0],
            latitude: monument.location[1],
          };

          const markerSymbol = {
            type: 'simple-marker',
            color: [18, 170, 54],
            outline: {
              color: [255, 255, 255],
              width: 2,
            },
          };

          const pointGraphic = new Graphic({
            geometry: point,
            symbol: markerSymbol,
            attributes: {
              name: monument.name,
              id: monument.id,
            },
          });

          const popupTemplate = {
            title: '{name}',
            content: `<a href="/lieux/${monument.id}">Voir le détail de '${monument.name}'</a>`,
          };

          pointGraphic.popupTemplate = popupTemplate;

          monumentsLayer.add(pointGraphic);
        });

        monumentsLayer.on('click', event => {
          setSelectedMonument(event.graphic.attributes);
          view.goTo({
            target: event.graphic.geometry,
            zoom: 12,
          });
        });

        setMonumentsList(monuments);

        const viewMonumentOnMap = (location) => {
          if (view) {
            view.goTo({
              center: location,
              zoom: 12,
            });
          } else {
            console.error("View is undefined.");
          }
        };

        const directionsWidget = new Directions({
          view: view,
        });

        view.ui.add(directionsWidget, 'top-right');

        const searchWidget = new Search({
          view: view,
          resultGraphicEnabled: false,
          popupEnabled: false,
        });

        view.ui.add(searchWidget, 'top-left');

        return () => {
          if (view) {
            view.destroy();
          }
        };
      })
      .catch(err => console.error(err));
  }, [selectedMap]);

  const handleSearch = (term) => {
    setSearchTerm(term);
  };

  const handleMarkerClick = (monument) => {
    setSelectedMonument(monument);
    setShowInfoPanel(true);
  };

  const changePage = (page) => {
    setCurrentPage(page);
  };

  const startIndex = (currentPage - 1) * itemsPerPage;
  const endIndex = startIndex + itemsPerPage;
  const currentMonuments = monumentsList
    .filter(monument => monument.name.toLowerCase().includes(searchTerm.toLowerCase()))
    .slice(startIndex, endIndex);

  return (
    <div className='main'>
      <h1 className='d-flex titreCarte justify-content-center'>Carte</h1>
      <div className='d-flex justify-content-center fondVertLieux'>
        <div id="map-view" style={{ height: '75vh', width: '75vw' }}></div>
      </div>
      <section className=''>
        <div className='d-flex justify-content-center'>
          <h1 className='d-flex titreCarteListeLieux justify-content-center mt-5'>Liste des monuments</h1>
        </div>
        {/* Barre de Recherche */}
        <div className="d-flex searchBarDiv justify-content-center align-items-center">
          <div className='divImageLoupe'>
            <img className='ImageLoupe' src={loupe}></img>
          </div>
          <input
            className='searchBar'
            type="text"
            placeholder="Rechercher un monument..."
            value={searchTerm}
            onChange={(e) => handleSearch(e.target.value)}
          />
        </div>
        {/* Liste des Monuments */}
        <div className="row">
          {currentMonuments.map((monument, index) => (
            <div key={index} className=" col-md-6 mb-4">
              <div className="card" onClick={() => handleMarkerClick(monument)}>
                <div className="card-body">
                  <h5 className="card-title titleMonument">{monument.name}</h5>
                  <div>
                    <a href={`/lieux/${monument.id}`}>Détails</a>
                    <a onClick={() => viewMonumentOnMap(monument.location)}>Voir sur la carte</a>
                  </div>
                </div>
              </div>
            </div>
          ))}
        </div>
        {/* Panneau d'Informations */}
        {showInfoPanel && (
          <div className="info-panel">
            <h2>{selectedMonument.name}</h2>
            {/* Ajoutez plus de détails au besoin */}
          </div>
        )}
        {/* Contrôles de Pagination */}
        <nav aria-label="Page navigation example">
          <ul className="pagination justify-content-center">
            {Array.from({ length: Math.ceil(monumentsList.length / itemsPerPage) }, (_, index) => (
              <li key={index} className={`page-item ${currentPage === index + 1 ? 'active' : ''}`}>
                <a
                  className="page-link"
                  onClick={() => changePage(index + 1)}
                  style={{ cursor: 'pointer' }}
                >
                  {index + 1}
                </a>
              </li>
            ))}
          </ul>
        </nav>
      </section>
    </div>
  );
};

export default Carte;





