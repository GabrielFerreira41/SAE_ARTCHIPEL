# Generated by Django 4.2.5 on 2023-09-28 07:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departement',
            fields=[
                ('idDepartement', models.AutoField(primary_key=True, serialize=False)),
                ('nomDepartement', models.CharField(max_length=50)),
                ('numeroDepartement', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Horaire',
            fields=[
                ('idHoraire', models.AutoField(primary_key=True, serialize=False)),
                ('jourHoraire', models.CharField(max_length=50)),
                ('horaireOuverture', models.TimeField()),
                ('horaireFermeture', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='JourFerie',
            fields=[
                ('idJourFerie', models.AutoField(primary_key=True, serialize=False)),
                ('dateJourFerie', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Lieu',
            fields=[
                ('idLieu', models.AutoField(primary_key=True, serialize=False)),
                ('nomLieu', models.CharField(max_length=50)),
                ('boolAccessibilite', models.BooleanField()),
                ('boolParking', models.BooleanField()),
                ('boolShopping', models.BooleanField()),
                ('boolRepas', models.BooleanField()),
                ('boolTable', models.BooleanField()),
                ('boolJaujeLieux', models.BooleanField()),
                ('nombreMaxVisiteur', models.IntegerField()),
                ('adresse', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('idRegion', models.AutoField(primary_key=True, serialize=False)),
                ('nomRegion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tarif',
            fields=[
                ('idTarif', models.AutoField(primary_key=True, serialize=False)),
                ('typeTarif', models.CharField(max_length=50)),
                ('prixUnitaire', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TypeLieu',
            fields=[
                ('idTypeLieu', models.AutoField(primary_key=True, serialize=False)),
                ('nomTypeLieu', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('idUtilisateur', models.AutoField(primary_key=True, serialize=False)),
                ('nomUtilisateur', models.CharField(max_length=50)),
                ('prenomUtilisateur', models.CharField(max_length=50)),
                ('mdpUtilisateur', models.CharField(max_length=50)),
                ('emailUtilisateur', models.CharField(max_length=50)),
                ('typeUtilisateur', models.CharField(max_length=50)),
                ('ddnUtilisateur', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Ville',
            fields=[
                ('idVille', models.AutoField(primary_key=True, serialize=False)),
                ('nomVille', models.CharField(max_length=50)),
                ('codePostal', models.IntegerField()),
                ('idDepartement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.departement')),
            ],
        ),
        migrations.CreateModel(
            name='PreferenceLieu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idLieu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.lieu')),
                ('idUtilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.utilisateur')),
            ],
        ),
        migrations.CreateModel(
            name='Parcours',
            fields=[
                ('idParcours', models.AutoField(primary_key=True, serialize=False)),
                ('nomParcours', models.CharField(max_length=50)),
                ('typeParcours', models.CharField(max_length=50)),
                ('difficulteParcours', models.CharField(max_length=50)),
                ('distanceParcours', models.IntegerField()),
                ('idUtilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.utilisateur')),
            ],
        ),
        migrations.CreateModel(
            name='Oeuvre',
            fields=[
                ('idOeuvre', models.AutoField(primary_key=True, serialize=False)),
                ('nomOeuvre', models.CharField(max_length=50)),
                ('descriptionOeuvre', models.CharField(max_length=50)),
                ('idLieu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.lieu')),
            ],
        ),
        migrations.CreateModel(
            name='LnkLieuTarif',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idLieu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.lieu')),
                ('idTarif', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.tarif')),
            ],
        ),
        migrations.CreateModel(
            name='LnkLieuJourFerie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idJourFerie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.jourferie')),
                ('idLieu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.lieu')),
            ],
        ),
        migrations.CreateModel(
            name='LnkLieuHoraire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idHoraire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.horaire')),
                ('idLieu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.lieu')),
            ],
        ),
        migrations.AddField(
            model_name='lieu',
            name='idVille',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.ville'),
        ),
        migrations.AddField(
            model_name='lieu',
            name='refTarif',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.tarif'),
        ),
        migrations.CreateModel(
            name='FavorieParcours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idParcours', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.parcours')),
                ('idUtilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.utilisateur')),
            ],
        ),
        migrations.CreateModel(
            name='Evenement',
            fields=[
                ('idEvenement', models.AutoField(primary_key=True, serialize=False)),
                ('nomEvenement', models.CharField(max_length=50)),
                ('descriptionEvenement', models.CharField(max_length=50)),
                ('idLieu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.lieu')),
            ],
        ),
        migrations.CreateModel(
            name='Etape',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numEtape', models.IntegerField()),
                ('idLieu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.lieu')),
                ('idParcours', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.parcours')),
            ],
        ),
        migrations.AddField(
            model_name='departement',
            name='idRegion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.region'),
        ),
    ]
