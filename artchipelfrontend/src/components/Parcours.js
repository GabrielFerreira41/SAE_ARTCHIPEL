import React from 'react';
import { motion } from 'framer-motion';

const parcoursList = [
  { id: 1, title: 'Parcours A', description: 'Description du parcours A' },
  { id: 2, title: 'Parcours B', description: 'Description du parcours B' },
  { id: 3, title: 'Parcours C', description: 'Description du parcours C' },
  // Ajoutez plus de parcours au besoin
];

const Parcours = () => {
  const fadeInUp = {
    initial: { opacity: 0, y: 20 },
    animate: { opacity: 1, y: 0 },
  };

  return (
    <div className="parcours-page">
      <h1 className="page-title">Parcours</h1>
      <motion.ul className="parcours-list">
        {parcoursList.map((parcours) => (
          <motion.li
            key={parcours.id}
            className="parcours-item"
            variants={fadeInUp}
            whileHover={{ scale: 1.1 }}
          >
            <h3>{parcours.title}</h3>
            <p>{parcours.description}</p>
          </motion.li>
        ))}
      </motion.ul>
    </div>
  );
};

export default Parcours;
