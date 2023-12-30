import React from "react";
import "../style/styleDecouverte.css";
import CentrePompidou from "../components/images/pompidouLogo.jpg"


const Decouverte = () => {
  return (
    <div>
      <div>
        <div className="d-flex justify-content-center align-items-center containerDflexPresCVDL">
          <div className="containerPresCVDL">
            <div className="TitreCVDL d-flex justify-content-center align-items-center">
              <h1>Centre val de loire</h1>
            </div>
            <div className="presentationCVDLDEC d-flex justify-content-center align-items-center p-4">
              <p>Bienvenue dans la région Centre-Val de Loire, un joyau au cœur de la France où l'histoire, la nature et la culture s'entremêlent harmonieusement. Nichée entre les vallées pittoresques de la Loire, cette région évoque un charme intemporel et offre une diversité de trésors à explorer.
              </p>
            </div>
          </div>
        </div>
      </div>
      <div>
        <div className="d-flex justify-content-center mt-5">
          <div className="divPresCVDL m-3">
            <h3>Patrimoine Historique</h3>
            <p>Explorez un patrimoine historique riche qui témoigne des siècles passés. Les châteaux majestueux, tels que Chambord, Chenonceau et Amboise, transportent les visiteurs dans l'époque des rois et des reines. Les villages médiévaux préservés, avec leurs ruelles pavées et leurs maisons à colombages, offrent une immersion authentique dans le passé.</p>
          </div>
          <div className="divPresCVDL m-3">
            <h3>La Vallée de la Loire, joyau naturel</h3>
            <p>Surnommée "le Jardin de la France", la région abrite la vallée de la Loire, classée au patrimoine mondial de l'UNESCO. Les paysages verdoyants, les vignobles renommés et les jardins somptueux font de cette région un écrin naturel exceptionnel. Les balades à vélo le long de la Loire ou les croisières tranquilles sur le fleuve offrent des expériences inoubliables.</p>
          </div>
        </div>
        <div className="d-flex justify-content-center">
          <div className="divPresCVDL m-3">
            <h3>Art et Culture</h3>
            <p>Le Centre-Val de Loire est également un berceau artistique et culturel. Des festivals dynamiques et des événements culturels animent la région tout au long de l'année. Les amateurs d'art peuvent se régaler dans les musées renommés et les galeries d'art qui mettent en valeur la créativité locale.</p>
          </div>
          <div className="divPresCVDL m-3">
            <h3>Gastronomie</h3>
            <p>La cuisine du Centre-Val de Loire est un délice pour les papilles. Savourez des plats délicieux mettant en avant des produits locaux de qualité, accompagnés des vins prestigieux de la région. Des marchés animés aux restaurants étoilés, la gastronomie de la région est une célébration des saveurs authentiques.</p>
          </div>
        </div>
      </div>
      <div>
        <div className="ContainerEndCVDL d-flex justify-content-center p-5">
          <div>
            <h2 className="mb-3 titreEndCVDLPhrase text-center">Visitez le Centre-Val de Loire</h2>
            <div className="ContainerEndCVDLPhrase">
              <p>Que vous soyez passionné d'histoire, amoureux de la nature, amateur d'art ou gourmand invétéré, le Centre-Val de Loire offre une expérience unique à chaque visite. Venez découvrir cette région pleine de charme et laissez-vous envoûter par son ambiance exceptionnelle.</p>
            </div>
            <div className="d-flex justify-content-center">
              <a className="btn btn-primary" href="https://www.centre-valdeloire.fr/" target="_blank">
                Site Centre-Val de Loire
              </a>
            </div>
          </div>
        </div>
      </div>
      <div>
        <div className="d-flex justify-content-center align-items-center containerDflexPresPompidou">
          <div className="containerPresPompidou">
            <div className="TitrePompidou d-flex justify-content-center align-items-center">
              <h1>Centre Pompidou</h1>
              <img className="pompidouLogo" src={CentrePompidou}></img>
            </div>
            
        </div>
      </div>
    </div>

    </div >
  );
};
export default Decouverte;
