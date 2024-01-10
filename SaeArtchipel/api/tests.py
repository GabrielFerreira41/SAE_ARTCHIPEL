import json
from time import timezone
from django.test import TestCase, Client
from django.urls import reverse
from django.http import JsonResponse
from .models import Utilisateur, PreferenceLieu, FavorisParcours, Parcours, Etape, Lieu, Horaire, TypeLieu, Tarif, Ville, Departement, Region, Evenement, LnkLieuHoraire
import os
from django.conf import settings


def create_user_admin():
    Utilisateur.objects.create(
        username="Admin",
        first_name="Admin",
        last_name="Admin",
        password="Admin",
        is_staff = True,
        is_active = True,
        is_superuser = True,
        email = "admin@admin.com",
        date_joined = "2024-01-01 00:00:00",
        ddn = "12/12/2000"
    )


def create_test_data():
    # Créer un utilisateur
    utilisateur = Utilisateur.objects.create(
        username="Test",
        first_name="Test",
        last_name="Test",
        password="Test",
        is_staff = False,
        is_active = True,
        is_superuser = False,
        email = "test@test.com",
        date_joined = "2024-01-01 00:00:00",
    )

    # Créer des données de test pour différents modèles
    parcours = Parcours.objects.create(
        nomParcours="Parcours de test",
        idUtilisateur=utilisateur,
        typeParcours="Randonnée",
        difficulteParcours="Facile",
        distanceParcours=10
    )
    ville = Ville.objects.create(
        idVille=1,
        nomVille="Civry",
        codePostal=12345,
        idDepartement=Departement.objects.create(
            idDepartement=1,
            nomDepartement="Eure-et-Loir",
            numeroDepartement=28,
            idRegion=Region.objects.create(
                idRegion=1,
                nomRegion="Centre-Val de Loire",
            )
        )
    )

    tarif = Tarif.objects.create(
        idTarif = 1,
        payant=True,
        reservation=True
    )

    type_lieu = TypeLieu.objects.create(idTypeLieu=1, nomTypeLieu='Bar')
    lieu = Lieu.objects.create(
        nomLieu="CivryBar",
        descriptionLieu="Pour boire un cannon",
        imageLieu = None,
        boolPompidouLieu=False,
        boolAccessibilite=True,
        boolParking=True,
        boolShopping=True,
        boolRepas=True,
        boolJaujeLieux=True,
        nombreMaxVisiteur=10,
        adresseLieu="1 rue de la soif",
        latitudeLieu=48.123456,
        longitudeLieu=2.123456,
        telLieu = 123456789,
        mailLieu = "civrybar@soif.com",
        webLieu="https://www.civrybar.com",
        observationLieu="Observation pour lieu de test",
        idVille=ville,
        idTarif=tarif, 
        idTypeLieu=type_lieu
    )

    etape = Etape.objects.create(
        idParcours=parcours,
        idLieu=lieu,
        numEtape=1
    )

    utilisateur_pref = PreferenceLieu.objects.create(
        idUtilisateur=utilisateur,
        idLieu=lieu
    )

    favoris_parcours = FavorisParcours.objects.create(
        idUtilisateur=utilisateur,
        idParcours=parcours
    )

    horaire = Horaire.objects.create(
        observationHoraire="Observation pour horaire de test",
        horaireOuverture="08:00:00",
        horaireFermeture="18:00:00",
        intervalHoraire=True,
        lienReservationHoraire="https://exemple.com/reservation"
    )

    evenement = Evenement.objects.create(
        nomEvenement="Evenement de test",
        descriptionEvenement="Description de l\"événement de test",
        prixEvenement=20.0,
        dateEvenement="2023-01-01",
        heureEvenement="15:00:00",
        infoEvenement="Informations supplémentaires sur l\"événement",
        adresseEvenement="Adresse de l\"événement",
        lienreservationEvenement="https://exemple.com/reservation_evenement",
        idLieu=lieu
    )

    lnk_lieu_horaire = LnkLieuHoraire.objects.create(
        idLieu=lieu,
        idHoraire=horaire,
        dateDebut="2023-01-01",
        dateFin="2023-12-31"
    )

    return {
        "utilisateur": utilisateur,
        "parcours": parcours,
        "lieu": lieu,
        "etape": etape,
        "utilisateur_pref": utilisateur_pref,
        "favoris_parcours": favoris_parcours,
        "horaire": horaire,
        "type_lieu": type_lieu,
        "tarif": tarif,
        "ville": ville,
        "evenement": evenement,
        "lnk": lnk_lieu_horaire,
    }

class ParcoursDetailsViewTest(TestCase):

    @classmethod # Permet de créer des données de test avant l"exécution des tests
    def setUpTestData(cls):
        cls.test_data = create_test_data()
            
    def test_details_parcours(self):
        url = reverse("detail_Parcours", args=[self.test_data["parcours"].idParcours])
        response = self.client.get(url)

        self.maxDiff = None
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response, JsonResponse)
        data_voulu = {
            "parcours": {
                "idParcours": self.test_data["parcours"].idParcours,
                "nomParcours": self.test_data["parcours"].nomParcours,
                "idUtilisateur": self.test_data["parcours"].idUtilisateur.id,
                "typeParcours": self.test_data["parcours"].typeParcours,
                "difficulteParcours": self.test_data["parcours"].difficulteParcours,
                "distanceParcours": self.test_data["parcours"].distanceParcours,
                "etapes": [
                {
                    "numEtape": self.test_data["etape"].numEtape,
                    "lieu": 
                    {
                        "idLieu": self.test_data["lieu"].idLieu,
                        "nomLieu": self.test_data["lieu"].nomLieu,
                        "descriptionLieu": self.test_data["lieu"].descriptionLieu,
                        "imageLieu": os.path.relpath(str(self.test_data["lieu"].imageLieu.path), settings.BASE_DIR) if self.test_data["lieu"].imageLieu else None,                   
                        "boolPompidouLieu": self.test_data["lieu"].boolPompidouLieu,
                        "boolAccessibilite": self.test_data["lieu"].boolAccessibilite,
                        "boolParking": self.test_data["lieu"].boolParking,
                        "boolShopping": self.test_data["lieu"].boolShopping,
                        "boolRepas": self.test_data["lieu"].boolRepas,
                        "boolJaujeLieux": self.test_data["lieu"].boolJaujeLieux,
                        "observationLieu": self.test_data["lieu"].observationLieu,
                        "nombreMaxVisiteur": self.test_data["lieu"].nombreMaxVisiteur,
                        "adresseLieu": self.test_data["lieu"].adresseLieu,
                        "telLieu": self.test_data["lieu"].telLieu,
                        "mailLieu": self.test_data["lieu"].mailLieu,
                        "webLieu": self.test_data["lieu"].webLieu,
                        "latitudeLieu": self.test_data["lieu"].latitudeLieu,
                        "longitudeLieu": self.test_data["lieu"].longitudeLieu,
                        "tarif": {
                            "idTarif": self.test_data["tarif"].idTarif,
                            "payant": self.test_data["tarif"].payant,
                            "reservation": self.test_data["tarif"].reservation
                        },
                        "typelieu": {
                            "idTypeLieu": self.test_data["type_lieu"].idTypeLieu,
                            "nomTypeLieu": self.test_data["type_lieu"].nomTypeLieu
                        },
                        "ville": {
                            "idVille": self.test_data["ville"].idVille,
                            "nomVille": self.test_data["ville"].nomVille,
                            "codePostal": self.test_data["ville"].codePostal,
                            "departement": {
                                "idDepartement": self.test_data["ville"].idDepartement.idDepartement,
                                "nomDepartement": self.test_data["ville"].idDepartement.nomDepartement,
                                "numeroDepartement": self.test_data["ville"].idDepartement.numeroDepartement,
                                "region": {
                                    "idRegion": self.test_data["ville"].idDepartement.idRegion.idRegion,
                                    "nomRegion": self.test_data["ville"].idDepartement.idRegion.nomRegion
                                }
                            }
                        },
                        "horaire": [
                            {
                                "idHoraire": self.test_data["lnk"].idHoraire.idHoraire,
                                "dateDebut": self.test_data["lnk"].dateDebut,
                                "dateFin": self.test_data["lnk"].dateFin,
                                "heures": {
                                    "idHoraire": self.test_data["horaire"].idHoraire,
                                    "observationHoraire": self.test_data["horaire"].observationHoraire,
                                    "horaireOuverture": self.test_data["horaire"].horaireOuverture,
                                    "horaireFermeture": self.test_data["horaire"].horaireFermeture,
                                    "intervalHoraire": self.test_data["horaire"].intervalHoraire,
                                    "lienReservationHoraire": self.test_data["horaire"].lienReservationHoraire
                                }
                            }
                        ],
                        "evenement": [
                            {
                                "idEvenement": self.test_data["evenement"].idEvenement,
                                "nomEvenement": self.test_data["evenement"].nomEvenement,
                                "descriptionEvenement": self.test_data["evenement"].descriptionEvenement,
                                "prixEvenement": self.test_data["evenement"].prixEvenement,
                                "dateEvenement": self.test_data["evenement"].dateEvenement,
                                "heureEvenement": self.test_data["evenement"].heureEvenement,
                                "infoEvenement": self.test_data["evenement"].infoEvenement,
                                "adresseEvenement": self.test_data["evenement"].adresseEvenement,
                                "lienreservationEvenement": self.test_data["evenement"].lienreservationEvenement
                                }
                            ]
                        }
                    }
                ],
            }
        }     

        # print(data_voulu == response.content)
        self.assertJSONEqual(response.content.decode("utf-8"), data_voulu)

class ParcoursListViewTest(TestCase):

    @classmethod 
    def setUpTestData(cls):
        cls.test_data = create_test_data()
    
            
    def test_list_parcours(self):
        url = reverse("list_Parcours")
        response = self.client.get(url)

        self.maxDiff = None
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response, JsonResponse)
        data_voulu = [
                    {
                        "idParcours": self.test_data["parcours"].idParcours,
                        "nomParcours": self.test_data["parcours"].nomParcours,
                        "idUtilisateur_id": self.test_data["parcours"].idUtilisateur.id,
                        "typeParcours": self.test_data["parcours"].typeParcours,
                        "difficulteParcours": self.test_data["parcours"].difficulteParcours,
                        "distanceParcours": self.test_data["parcours"].distanceParcours,
                    }
                ]
    
        self.assertJSONEqual(response.content.decode("utf-8"), data_voulu)

class LieuDetailsViewTest(TestCase):
    
        @classmethod 
        def setUpTestData(cls):
            cls.test_data = create_test_data()    
                
        def test_details_lieu(self):
            url = reverse("detail_Lieu", args=[self.test_data["lieu"].idLieu])
            response = self.client.get(url)
    
            self.maxDiff = None
            self.assertEqual(response.status_code, 200)
            self.assertIsInstance(response, JsonResponse)
            data_voulu = {
                "lieu": {
                    "idLieu": self.test_data["lieu"].idLieu,
                    "nomLieu": self.test_data["lieu"].nomLieu,
                    "descriptionLieu": self.test_data["lieu"].descriptionLieu,
                    "imageLieu": os.path.relpath(str(self.test_data["lieu"].imageLieu.path), settings.BASE_DIR) if self.test_data["lieu"].imageLieu else None,                   
                    "boolPompidouLieu": self.test_data["lieu"].boolPompidouLieu,
                    "boolAccessibilite": self.test_data["lieu"].boolAccessibilite,
                    "boolParking": self.test_data["lieu"].boolParking,
                    "boolShopping": self.test_data["lieu"].boolShopping,
                    "boolRepas": self.test_data["lieu"].boolRepas,
                    "boolJaujeLieux": self.test_data["lieu"].boolJaujeLieux,
                    "observationLieu": self.test_data["lieu"].observationLieu,
                    "nombreMaxVisiteur": self.test_data["lieu"].nombreMaxVisiteur,
                    "adresseLieu": self.test_data["lieu"].adresseLieu,
                    "telLieu": self.test_data["lieu"].telLieu,
                    "mailLieu": self.test_data["lieu"].mailLieu,
                    "webLieu": self.test_data["lieu"].webLieu,
                    "latitudeLieu": self.test_data["lieu"].latitudeLieu,
                    "longitudeLieu": self.test_data["lieu"].longitudeLieu,
                    "tarif": {
                        "idTarif": self.test_data["tarif"].idTarif,
                        "payant": self.test_data["tarif"].payant,
                        "reservation": self.test_data["tarif"].reservation
                    },
                    "typelieu": {
                        "idTypeLieu": self.test_data["type_lieu"].idTypeLieu,
                        "nomTypeLieu": self.test_data["type_lieu"].nomTypeLieu
                    },
                    "ville": {
                        "idVille": self.test_data["ville"].idVille,
                        "nomVille": self.test_data["ville"].nomVille,
                        "codePostal": self.test_data["ville"].codePostal,
                        "departement": {
                            "idDepartement": self.test_data["ville"].idDepartement.idDepartement,
                            "nomDepartement": self.test_data["ville"].idDepartement.nomDepartement,
                            "numeroDepartement": self.test_data["ville"].idDepartement.numeroDepartement,
                            "region": {
                                "idRegion": self.test_data["ville"].idDepartement.idRegion.idRegion,
                                "nomRegion": self.test_data["ville"].idDepartement.idRegion.nomRegion
                            }
                        }
                    },
                    "horaire": [
                        {
                            "idHoraire": self.test_data["lnk"].idHoraire.idHoraire,
                            "dateDebut": self.test_data["lnk"].dateDebut,
                            "dateFin": self.test_data["lnk"].dateFin,
                            "heures": {
                                "idHoraire": self.test_data["horaire"].idHoraire,
                                "observationHoraire": self.test_data["horaire"].observationHoraire,
                                "horaireOuverture": self.test_data["horaire"].horaireOuverture,
                                "horaireFermeture": self.test_data["horaire"].horaireFermeture,
                                "intervalHoraire": self.test_data["horaire"].intervalHoraire,
                                "lienReservationHoraire": self.test_data["horaire"].lienReservationHoraire
                            }
                        }
                    ],
                    "evenement": [
                        {
                            "idEvenement": self.test_data["evenement"].idEvenement,
                            "nomEvenement": self.test_data["evenement"].nomEvenement,
                            "descriptionEvenement": self.test_data["evenement"].descriptionEvenement,
                            "prixEvenement": self.test_data["evenement"].prixEvenement,
                            "dateEvenement": self.test_data["evenement"].dateEvenement,
                            "heureEvenement": self.test_data["evenement"].heureEvenement,
                            "infoEvenement": self.test_data["evenement"].infoEvenement,
                            "adresseEvenement": self.test_data["evenement"].adresseEvenement,
                            "lienreservationEvenement": self.test_data["evenement"].lienreservationEvenement
                        }
                    ]
                }
            }

            # print(data_voulu == response.content)
            self.assertJSONEqual(response.content.decode("utf-8"), data_voulu)


class LieuListViewTest(TestCase):
        
        @classmethod 
        def setUpTestData(cls):
                cls.test_data = create_test_data()
                    
                    
        def test_list_lieu(self):
            url = reverse("list_lieux")
            response = self.client.get(url)
            self.maxDiff = None
            self.assertEqual(response.status_code, 200)
            self.assertIsInstance(response, JsonResponse)
            data_voulu = [
                {
                    "idLieu": self.test_data["lieu"].idLieu,
                    "nomLieu": self.test_data["lieu"].nomLieu,
                    "descriptionLieu": self.test_data["lieu"].descriptionLieu,
                    "imageLieu": os.path.relpath(str(self.test_data["lieu"].imageLieu.path), settings.BASE_DIR) if self.test_data["lieu"].imageLieu else "",                   
                    "boolPompidouLieu": self.test_data["lieu"].boolPompidouLieu,
                    "boolAccessibilite": self.test_data["lieu"].boolAccessibilite,
                    "boolParking": self.test_data["lieu"].boolParking,
                    "boolShopping": self.test_data["lieu"].boolShopping,
                    "boolRepas": self.test_data["lieu"].boolRepas,
                    "boolJaujeLieux": self.test_data["lieu"].boolJaujeLieux,
                    "nombreMaxVisiteur": self.test_data["lieu"].nombreMaxVisiteur,
                    "adresseLieu": self.test_data["lieu"].adresseLieu,
                    "latitudeLieu": self.test_data["lieu"].latitudeLieu,
                    "longitudeLieu": self.test_data["lieu"].longitudeLieu,
                    "telLieu": self.test_data["lieu"].telLieu,
                    "mailLieu": self.test_data["lieu"].mailLieu,
                    "webLieu": self.test_data["lieu"].webLieu,
                    "observationLieu": self.test_data["lieu"].observationLieu,
                    "idVille_id": self.test_data["ville"].idVille,
                    "idTarif_id": self.test_data["tarif"].idTarif,
                    "idTypeLieu_id": self.test_data["type_lieu"].idTypeLieu,
                    "numDepartement": self.test_data["ville"].idDepartement.numeroDepartement,
                    
                    
                    
                }
            ]
            # print(data_voulu)
            # print("reponse : ", response.content.decode("utf-8"))
            self.assertJSONEqual(response.content.decode("utf-8"), data_voulu)

class EvenementListViewTest(TestCase):

    @classmethod
    def setUp(cls):
        cls.test_data = create_test_data()

    def test_list_evenement(self):
        url = reverse("list_evenements")
        response = self.client.get(url)

        self.maxDiff = None
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response, JsonResponse)
        data_voulu = [
            {
                "idEvenement": self.test_data["evenement"].idEvenement,
                "nomEvenement": self.test_data["evenement"].nomEvenement,
                "descriptionEvenement": self.test_data["evenement"].descriptionEvenement,
                "prixEvenement": self.test_data["evenement"].prixEvenement,
                "dateEvenement": self.test_data["evenement"].dateEvenement,
                "heureEvenement": self.test_data["evenement"].heureEvenement,
                "infoEvenement": self.test_data["evenement"].infoEvenement,
                "adresseEvenement": self.test_data["evenement"].adresseEvenement,
                "lienreservationEvenement": self.test_data["evenement"].lienreservationEvenement,
                "idLieu_id": self.test_data["lieu"].idLieu
            }
        ]
        # print(data_voulu)
        # print("reponse : ", response.content.decode("utf-8"))

        self.assertJSONEqual(response.content.decode("utf-8"), data_voulu)

class EvenementDetailsViewTest(TestCase):

    @classmethod
    def setUp(cls):
        cls.test_data = create_test_data()

    def test_detail_evenement_with_lieu(self):
        url = reverse("detail_evenement", args=[self.test_data["evenement"].idEvenement])
        response = self.client.get(url)

        self.maxDiff = None
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response, JsonResponse)
        data_voulu = {
            "evenement": {
                "idEvenement": self.test_data["evenement"].idEvenement,
                "nomEvenement": self.test_data["evenement"].nomEvenement,
                "descriptionEvenement": self.test_data["evenement"].descriptionEvenement,
                "prixEvenement": self.test_data["evenement"].prixEvenement,
                "dateEvenement": self.test_data["evenement"].dateEvenement,
                "heureEvenement": self.test_data["evenement"].heureEvenement,
                "infoEvenement": self.test_data["evenement"].infoEvenement,
                "adresseEvenement": self.test_data["evenement"].adresseEvenement,
                "lienreservationEvenement": self.test_data["evenement"].lienreservationEvenement,
                "lieu": {
                    "idLieu": self.test_data["lieu"].idLieu,
                    "nomLieu": self.test_data["lieu"].nomLieu,
                    "descriptionLieu": self.test_data["lieu"].descriptionLieu,
                    "imageLieu": os.path.relpath(str(self.test_data["lieu"].imageLieu.path), settings.BASE_DIR) if self.test_data["lieu"].imageLieu else None,                   
                    "boolPompidouLieu": self.test_data["lieu"].boolPompidouLieu,
                    "boolAccessibilite": self.test_data["lieu"].boolAccessibilite,
                    "boolParking": self.test_data["lieu"].boolParking,
                    "boolShopping": self.test_data["lieu"].boolShopping,
                    "boolRepas": self.test_data["lieu"].boolRepas,
                    "boolJaujeLieux": self.test_data["lieu"].boolJaujeLieux,
                    "observationLieu": self.test_data["lieu"].observationLieu,
                    "nombreMaxVisiteur": self.test_data["lieu"].nombreMaxVisiteur,
                    "adresseLieu": self.test_data["lieu"].adresseLieu,
                    "telLieu": self.test_data["lieu"].telLieu,
                    "mailLieu": self.test_data["lieu"].mailLieu,
                    "webLieu": self.test_data["lieu"].webLieu,
                    "latitudeLieu": self.test_data["lieu"].latitudeLieu,
                    "longitudeLieu": self.test_data["lieu"].longitudeLieu,
                    "tarif": {
                        "idTarif": self.test_data["tarif"].idTarif,
                        "payant": self.test_data["tarif"].payant,
                        "reservation": self.test_data["tarif"].reservation
                    },
                    "typelieu": {
                        "idTypeLieu": self.test_data["type_lieu"].idTypeLieu,
                        "nomTypeLieu": self.test_data["type_lieu"].nomTypeLieu
                    },
                    "ville": {
                        "idVille": self.test_data["ville"].idVille,
                        "nomVille": self.test_data["ville"].nomVille,
                        "codePostal": self.test_data["ville"].codePostal,
                        "departement": {
                            "idDepartement": self.test_data["ville"].idDepartement.idDepartement,
                            "nomDepartement": self.test_data["ville"].idDepartement.nomDepartement,
                            "numeroDepartement": self.test_data["ville"].idDepartement.numeroDepartement,
                            "region": {
                                "idRegion": self.test_data["ville"].idDepartement.idRegion.idRegion,
                                "nomRegion": self.test_data["ville"].idDepartement.idRegion.nomRegion
                            }
                        }
                    },
                    "horaire": [
                        {
                            "idHoraire": self.test_data["lnk"].idHoraire.idHoraire,
                            "dateDebut": self.test_data["lnk"].dateDebut,
                            "dateFin": self.test_data["lnk"].dateFin,
                            "heures": {
                                "idHoraire": self.test_data["horaire"].idHoraire,
                                "observationHoraire": self.test_data["horaire"].observationHoraire,
                                "horaireOuverture": self.test_data["horaire"].horaireOuverture,
                                "horaireFermeture": self.test_data["horaire"].horaireFermeture,
                                "intervalHoraire": self.test_data["horaire"].intervalHoraire,
                                "lienReservationHoraire": self.test_data["horaire"].lienReservationHoraire
                            }
                        }
                    ],
                }
            }
        }
        # print(data_voulu)
        # print("reponse : ", response.content.decode("utf-8"))

        self.assertJSONEqual(response.content.decode("utf-8"), data_voulu)

                
class RegionListViewTest(TestCase):
    
    @classmethod 
    def setUpTestData(cls):
        cls.test_data = create_test_data()

    def test_list_region(self):
        url = reverse("list_regions")
        response = self.client.get(url)
        self.maxDiff = None
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response, JsonResponse)
        data_voulu = [
            {
                "idRegion": self.test_data["ville"].idDepartement.idRegion.idRegion,
                "nomRegion": self.test_data["ville"].idDepartement.idRegion.nomRegion,
            }
        ]
        # print(data_voulu)
        # print("reponse : ", response.content.decode("utf-8"))

        self.assertJSONEqual(response.content.decode("utf-8"), data_voulu)


class DepartementListViewTest(TestCase):
    
    @classmethod 
    def setUpTestData(cls):
        cls.test_data = create_test_data()
    
    def test_list_departement(self):
        url = reverse("list_departements")
        response = self.client.get(url)
        self.maxDiff = None
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response, JsonResponse)
        data_voulu = [
            {
                "idDepartement": self.test_data["ville"].idDepartement.idDepartement,
                "nomDepartement": self.test_data["ville"].idDepartement.nomDepartement,
                "numeroDepartement": self.test_data["ville"].idDepartement.numeroDepartement,
                "idRegion_id": self.test_data["ville"].idDepartement.idRegion.idRegion,
            }
        ]
        # print(data_voulu)
        # print("reponse : ", response.content.decode("utf-8"))

        self.assertJSONEqual(response.content.decode("utf-8"), data_voulu)


class VilleListViewTest(TestCase):
            
    @classmethod 
    def setUpTestData(cls):
        cls.test_data = create_test_data()
    
            
    def test_list_ville(self):
        url = reverse("list_villes")
        response = self.client.get(url)
        self.maxDiff = None
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response, JsonResponse)
        data_voulu = [
            {
                "idVille": self.test_data["ville"].idVille,
                "nomVille": self.test_data["ville"].nomVille,
                "codePostal": self.test_data["ville"].codePostal,
                "idDepartement_id": self.test_data["ville"].idDepartement.idDepartement,
            }
        ]
        # print(data_voulu)
        # print("reponse : ", response.content.decode("utf-8"))

        self.assertJSONEqual(response.content.decode("utf-8"), data_voulu)

class TypeLieuListViewTest(TestCase):
                    
    @classmethod 
    def setUpTestData(cls):
        cls.test_data = create_test_data()
    
            
    def test_list_typelieu(self):
        url = reverse("list_typelieu")
        response = self.client.get(url)
        self.maxDiff = None
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response, JsonResponse)
        data_voulu = [
            {
                "idTypeLieu": self.test_data["type_lieu"].idTypeLieu,
                "nomTypeLieu": self.test_data["type_lieu"].nomTypeLieu,
            }
        ]
        # print(data_voulu)
        # print("reponse : ", response.content.decode("utf-8"))

        self.assertJSONEqual(response.content.decode("utf-8"), data_voulu)

class TarifListViewTest(TestCase):  
     
    @classmethod 
    def setUpTestData(cls):
        cls.test_data = create_test_data()
    
    def test_list_tarif(self):
        url = reverse("list_tarifs")
        response = self.client.get(url)
        self.maxDiff = None
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response, JsonResponse)
        data_voulu = [
            {
                "idTarif": self.test_data["tarif"].idTarif,
                "payant": self.test_data["tarif"].payant,
                "reservation": self.test_data["tarif"].reservation,
            }
        ]
        # print(data_voulu)
        # print("reponse : ", response.content.decode("utf-8"))

        self.assertJSONEqual(response.content.decode("utf-8"), data_voulu)

class FavorisParcoursView(TestCase):

    @classmethod
    def setUp(cls):
        cls.test_data = create_test_data()

    def test_list_favorisparcours(self):
        url = reverse("list_favorisparcours")
        response = self.client.get(url)

        self.maxDiff = None
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response, JsonResponse)
        data_voulu = [
            {
                "id": self.test_data["favoris_parcours"].id,
                "idUtilisateur_id": self.test_data["utilisateur"].id,
                "idParcours_id": self.test_data["parcours"].idParcours
            }
        ]
        # print(data_voulu)
        # print("reponse : ", response.content.decode("utf-8"))

        self.assertJSONEqual(response.content.decode("utf-8"), data_voulu)

class PreferenceLieuView(TestCase):
    
    @classmethod
    def setUp(self):
        self.test_data = create_test_data()

    def test_list_preference_lieu(self):
        url = reverse("list_preferencelieu")
        response = self.client.get(url)

        self.maxDiff = None
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response, JsonResponse)
        data_voulu = [
            {
                "id" : self.test_data["utilisateur_pref"].id,
                "idLieu_id": self.test_data["lieu"].idLieu,
                "idUtilisateur_id": self.test_data["utilisateur"].id
            }
        ]
        # print(data_voulu)
        # print("reponse : ", response.content.decode("utf-8"))

        self.assertJSONEqual(response.content.decode("utf-8"), data_voulu)

"""class OeuvreProximiteView(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.test_data = create_test_data()

    def test_list_oeuvre_proximite(self):
        url = reverse("list_oeuvres_proximite")
        response = self.client.get(url)

        self.maxDiff = None
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response, JsonResponse)
        data_voulu = [
        {
        "oeuvre à proximité": [
            {
                "lieu": {
                    "idLieu": self.test_data["lieu"].idLieu,
                    "nomLieu": self.test_data["lieu"].nomLieu,
                    "descriptionLieu": self.test_data["lieu"].descriptionLieu,
                    "imageLieu": os.path.relpath(str(self.test_data["lieu"].imageLieu.path), settings.BASE_DIR) if self.test_data["lieu"].imageLieu else None,
                    "boolPompidouLieu": self.test_data["lieu"].boolPompidouLieu,
                    "boolAccessibilite": self.test_data["lieu"].boolAccessibilite,
                    "boolParking": self.test_data["lieu"].boolParking,
                    "boolShopping": self.test_data["lieu"].boolShopping,
                    "boolRepas": self.test_data["lieu"].boolRepas,
                    "boolJaujeLieux": self.test_data["lieu"].boolJaujeLieux,
                    "observationLieu": self.test_data["lieu"].observationLieu,
                    "nombreMaxVisiteur": self.test_data["lieu"].nombreMaxVisiteur,
                    "adresseLieu": self.test_data["lieu"].adresseLieu,
                    "telLieu": self.test_data["lieu"].telLieu,
                    "mailLieu": self.test_data["lieu"].mailLieu,
                    "webLieu": self.test_data["lieu"].webLieu,
                    "latitudeLieu": self.test_data["lieu"].latitudeLieu,
                    "longitudeLieu": self.test_data["lieu"].longitudeLieu,
                    "tarif": {
                        "idTarif": self.test_data["tarif"].idTarif,
                        "payant": self.test_data["tarif"].payant,
                        "reservation": self.test_data["tarif"].reservation
                    },
                    "typelieu": {
                        "idTypeLieu": self.test_data["type_lieu"].idTypeLieu,
                        "nomTypeLieu": self.test_data["type_lieu"].nomTypeLieu
                    },
                    "ville": {
                        "idVille": self.test_data["ville"].idVille,
                        "nomVille": self.test_data["ville"].nomVille,
                        "codePostal": self.test_data["ville"].codePostal,
                        "departement": {
                            "idDepartement": self.test_data["ville"].idDepartement.idDepartement,
                            "nomDepartement": self.test_data["ville"].idDepartement.nomDepartement,
                            "numeroDepartement": self.test_data["ville"].idDepartement.numeroDepartement,
                            "region": {
                                "idRegion": self.test_data["ville"].idDepartement.idRegion.idRegion,
                                "nomRegion": self.test_data["ville"].idDepartement.idRegion.nomRegion
                            }
                        }
                    },
                    "horaire": [
                        {
                            "idHoraire": self.test_data["lnk"].idHoraire.idHoraire,
                            "dateDebut": self.test_data["lnk"].dateDebut,
                            "dateFin": self.test_data["lnk"].dateFin,
                            "heures": {
                                "idHoraire": self.test_data["horaire"].idHoraire,
                                "observationHoraire": self.test_data["horaire"].observationHoraire,
                                "horaireOuverture": self.test_data["horaire"].horaireOuverture,
                                "horaireFermeture": self.test_data["horaire"].horaireFermeture,
                                "intervalHoraire": self.test_data["horaire"].intervalHoraire,
                                "lienReservationHoraire": self.test_data["horaire"].lienReservationHoraire
                            }
                        }
                    ],
                    "evenement": [
                        {
                            "idEvenement": self.test_data["evenement"].idEvenement,
                            "nomEvenement": self.test_data["evenement"].nomEvenement,
                            "descriptionEvenement": self.test_data["evenement"].descriptionEvenement,
                            "prixEvenement": self.test_data["evenement"].prixEvenement,
                            "dateEvenement": self.test_data["evenement"].dateEvenement,
                            "heureEvenement": self.test_data["evenement"].heureEvenement,
                            "infoEvenement": self.test_data["evenement"].infoEvenement,
                            "adresseEvenement": self.test_data["evenement"].adresseEvenement,
                            "lienreservationEvenement": self.test_data["evenement"].lienreservationEvenement
                                }
                            ]
                        }
                    }
                ]
            }
        ]
        self.assertJSONEqual(response.content.decode("utf-8"), data_voulu)
"""
"""class OeuvreProximitesDepartement(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        cls.test_data = create_test_data()
    
    def test_list_oeuvre_proximite_departement(self):
        print("departement : ", self.test_data["ville"].idDepartement.idDepartement)
        url = reverse("get_all_oeuvres_proximites_departement", args=[self.test_data["ville"].idDepartement.idDepartement])
        response = self.client.get(url)
        self.maxDiff = None
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response, JsonResponse)
        data_voulu = [
            {
                "idLieu": self.test_data["lieu"].idLieu,
                "nomLieu": self.test_data["lieu"].nomLieu,
                "descriptionLieu": self.test_data["lieu"].descriptionLieu,
                "imageLieu": os.path.relpath(str(self.test_data["lieu"].imageLieu.path), settings.BASE_DIR) if self.test_data["lieu"].imageLieu else None,                   
                "boolPompidouLieu": self.test_data["lieu"].boolPompidouLieu,
                "boolAccessibilite": self.test_data["lieu"].boolAccessibilite,
                "boolParking": self.test_data["lieu"].boolParking,
                "boolShopping": self.test_data["lieu"].boolShopping,
                "boolRepas": self.test_data["lieu"].boolRepas,
                "boolJaujeLieux": self.test_data["lieu"].boolJaujeLieux,
                "observationLieu": self.test_data["lieu"].observationLieu,
                "nombreMaxVisiteur": self.test_data["lieu"].nombreMaxVisiteur,
                "adresseLieu": self.test_data["lieu"].adresseLieu,
                "telLieu": self.test_data["lieu"].telLieu,
                "mailLieu": self.test_data["lieu"].mailLieu,
                "webLieu": self.test_data["lieu"].webLieu,
                "latitudeLieu": self.test_data["lieu"].latitudeLieu,
                "longitudeLieu": self.test_data["lieu"].longitudeLieu,
                "tarif": {
                    "idTarif": self.test_data["tarif"].idTarif,
                    "payant": self.test_data["tarif"].payant,
                    "reservation": self.test_data["tarif"].reservation
                },
                "typelieu": {
                    "idTypeLieu": self.test_data["type_lieu"].idTypeLieu,

                }
            }
        
        ]
    
        self.assertJSONEqual(response.content.decode("utf-8"), data_voulu)
 """

class AuthRegister(TestCase):
    def test_register(self):
        url = reverse("auth_register")
        response = self.client.post(url,{
        "username": "feur",
        "password": "Feur54321",
        "password2": "Feur54321",
        "email": "feur@feur.com",
        "first_name": "feur",
        "last_name": "feur",
        "ddnUtilisateur": "2021-01-01"
        }
        )

        self.assertEqual(response.status_code, 201)
        
        # Vérification que l'utilisateur a été créé
        created_user = Utilisateur.objects.get(username="feur")
        self.assertEqual(created_user.username, "feur")
        self.assertEqual(created_user.first_name, "feur")
        self.assertEqual(created_user.last_name, "feur")
        self.assertEqual(created_user.email, "feur@feur.com")
        self.assertEqual(str(created_user.ddnUtilisateur), "2021-01-01")
        self.assertEqual(created_user.is_active, True)
        self.assertEqual(created_user.is_staff, False)
        self.assertEqual(created_user.is_superuser, False)