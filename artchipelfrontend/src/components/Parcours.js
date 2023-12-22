import React from 'react';
import { motion } from 'framer-motion';
import "../style/styleParcours.css";


const parcoursList = [
  { id: 1, title: 'Parcours A', description: 'Description du parcours A' },
  { id: 2, title: 'Parcours B', description: 'Description du parcours B' },
  { id: 3, title: 'Parcours C', description: 'Description du parcours C' },
  { id: 4, title: 'Parcours D', description: 'Description du parcours D' },
  { id: 5, title: 'Parcours E', description: 'Description du parcours E' },
  { id: 6, title: 'Parcours F', description: 'Description du parcours F' },
  { id: 7, title: 'Parcours G', description: 'Description du parcours G' },
  { id: 8, title: 'Parcours H', description: 'Description du parcours H' },
  { id: 9, title: 'Parcours I', description: 'Description du parcours I' },
  { id: 10, title: 'Parcours J', description: 'Description du parcours J' },
  { id: 11, title: 'Parcours K', description: 'Description du parcours K' },
  { id: 12, title: 'Parcours L', description: 'Description du parcours L' },
  { id: 13, title: 'Parcours M', description: 'Description du parcours M' },
  { id: 14, title: 'Parcours N', description: 'Description du parcours N' },
  { id: 15, title: 'Parcours O', description: 'Description du parcours O' },
  { id: 16, title: 'Parcours P', description: 'Description du parcours P' },
  { id: 17, title: 'Parcours Q', description: 'Description du parcours Q' },
  { id: 18, title: 'Parcours R', description: 'Description du parcours R' },
  { id: 19, title: 'Parcours S', description: 'Description du parcours S' },
  { id: 20, title: 'Parcours T', description: 'Description du parcours T' },
  { id: 21, title: 'Parcours U', description: 'Description du parcours U' },
  { id: 22, title: 'Parcours V', description: 'Description du parcours V' },
  { id: 23, title: 'Parcours W', description: 'Description du parcours W' },
  { id: 24, title: 'Parcours X', description: 'Description du parcours X' },
  { id: 25, title: 'Parcours Y', description: 'Description du parcours Y' },
  { id: 26, title: 'Parcours Z', description: 'Description du parcours Z' },
  { id: 27, title: 'Parcours AA', description: 'Description du parcours AA' },
  { id: 28, title: 'Parcours BB', description: 'Description du parcours BB' },
  { id: 29, title: 'Parcours CC', description: 'Description du parcours CC' },
  { id: 30, title: 'Parcours DD', description: 'Description du parcours DD' },
];

const Parcours = () => {
  const fadeInUp = {
    initial: { opacity: 0, y: 20 },
    animate: { opacity: 1, y: 0 },
  };

  const minSize = 10;
  const maxSize = 30;
  const itemsPerRow = 4;

  const getRandomColor = () => {
    const startColor = [0, 159, 227];
    const endColor = [18, 170, 54];
    const randomColor = startColor.map((start, index) => {
      const end = endColor[index];
      return Math.floor(Math.random() * (end - start + 1)) + start;
    });
    return `rgb(${randomColor.join(', ')})`;
  };

  const calculateSize = () => {
    const totalItems = parcoursList.length;
    const rows = Math.ceil(totalItems / itemsPerRow);
    const width = Math.floor(window.innerWidth / itemsPerRow);
    const height = Math.floor(window.innerHeight / rows);

    return {
      width: Math.min(width, maxSize),
      height: Math.min(height, maxSize),
    };
  };

  return (
    <div>
      <h1 className='d-flex titreParcours justify-content-center'>"Parcours Mosaïque"</h1>
      <div className='d-flex titreParcours justify-content-center containerRectangleVert'>
        <div className='rectangleVert'></div>
      </div>
      <motion.ul
        className="parcours-list list-unstyled"
        style={{
          display: 'grid',
          gridTemplateColumns: `repeat(${itemsPerRow}, 1fr)`,
          gap: '0', 
          margin: '0',
          padding: '0',
        }}
      >
        {parcoursList.map((parcours, index) => (
          <motion.li
            key={parcours.id}
            className="parcours-item d-flex justify-content-center align-items-center"
            variants={fadeInUp}
            whileHover={{ scale: 1.1 }}
            style={{
              width: `${calculateSize().width}rem`,
              height: `${calculateSize().height}rem`,
              backgroundColor: getRandomColor(),
              margin: '0',
            }}
          >
            <div className='text-center'>
              <h3 style={{ fontSize: '90%', margin: '0' }}>{parcours.title}</h3>
              <p style={{ fontSize: '80%', margin: '0' }}>{parcours.description}</p>
            </div>
          </motion.li>
        ))}
      </motion.ul>
    </div>
  );
};

export default Parcours;
