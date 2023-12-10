import React from 'react';
import '../style/styleFooter.css';

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
