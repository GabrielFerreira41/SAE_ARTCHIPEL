import React from 'react';
import '../style/styleFooter.css';

/**
 * Le composant Footer est une fonction JavaScript qui renvoie un élément de pied de page avec du
 * contenu et un style.
 * @returns Le composant Footer renvoie un élément JSX représentant la section de pied de page d'une
 * page Web.
 */
const Footer = () => {
    return (
        <footer>
            <div className='d-flex justify-content-center'>
                <p className="">SAE ArtChipel étudiants 3ème année BUT Informatique (Ferreira, Farault, Corret, Kissouna)</p>
                <p className="">Contact Us : gabriel.ferreira@etu.univ-orleans.fr</p>
            </div>
            <div className='d-flex justify-content-center'>
                <div className='BleuFooter'></div>
                <div className='BlancFooter'></div>
                <div className='RougeFooter'></div>
            </div>
        </footer>
    );
};

export default Footer;
