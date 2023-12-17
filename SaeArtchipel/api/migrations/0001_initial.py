# Generated by Django 4.2.5 on 2023-12-14 10:34

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
                ('nomDepartement', models.CharField(max_length=200, unique=True)),
                ('numeroDepartement', models.IntegerField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Horaire',
            fields=[
                ('idHoraire', models.AutoField(primary_key=True, serialize=False)),
                ('listJour', models.CharField(max_length=300, null=True)),
                ('horaireOuverture', models.TimeField()),
                ('horaireFermeture', models.TimeField()),
                ('intervalHoraire', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Lieu',
            fields=[
                ('idLieu', models.AutoField(primary_key=True, serialize=False)),
                ('nomLieu', models.CharField(max_length=150, unique=True)),
                ('descriptionLieu', models.CharField(max_length=10000)),
                ('imageLieu', models.CharField(max_length=250)),
                ('boolAccessibilite', models.BooleanField()),
                ('boolParking', models.BooleanField()),
                ('boolShopping', models.BooleanField()),
                ('boolRepas', models.BooleanField()),
                ('boolTable', models.BooleanField()),
                ('boolJaujeLieux', models.BooleanField()),
                ('nombreMaxVisiteur', models.IntegerField()),
                ('adresseLieu', models.CharField(max_length=250)),
                ('longitudeLieu', models.FloatField()),
                ('latitudeLieu', models.FloatField()),
                ('telLieu', models.IntegerField(max_length=10, null=True)),
                ('mailLieu', models.CharField(max_length=150, null=True)),
                ('webLieu', models.CharField(max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('idRegion', models.AutoField(primary_key=True, serialize=False)),
                ('nomRegion', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tarif',
            fields=[
                ('idTarif', models.AutoField(primary_key=True, serialize=False)),
                ('payant', models.BooleanField()),
                ('reservation', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='TypeLieu',
            fields=[
                ('idTypeLieu', models.AutoField(primary_key=True, serialize=False)),
                ('nomTypeLieu', models.CharField(max_length=150, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('idUtilisateur', models.AutoField(primary_key=True, serialize=False)),
                ('nomUtilisateur', models.CharField(max_length=250, unique=True)),
                ('prenomUtilisateur', models.CharField(max_length=250)),
                ('mdpUtilisateur', models.CharField(max_length=15)),
                ('emailUtilisateur', models.CharField(max_length=150, unique=True)),
                ('typeUtilisateur', models.BooleanField()),
                ('ddnUtilisateur', models.DateField(verbose_name='%d/%m/%Y')),
            ],
        ),
        migrations.CreateModel(
            name='Ville',
            fields=[
                ('idVille', models.AutoField(primary_key=True, serialize=False)),
                ('nomVille', models.CharField(max_length=200, unique=True)),
                ('codePostal', models.IntegerField(max_length=5)),
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
                ('nomParcours', models.CharField(max_length=200)),
                ('typeParcours', models.CharField(max_length=200)),
                ('difficulteParcours', models.CharField(max_length=100)),
                ('distanceParcours', models.IntegerField()),
                ('idUtilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.utilisateur')),
            ],
        ),
        migrations.CreateModel(
            name='Oeuvre',
            fields=[
                ('idOeuvre', models.AutoField(primary_key=True, serialize=False)),
                ('nomOeuvre', models.CharField(max_length=200)),
                ('descriptionOeuvre', models.CharField(max_length=200)),
                ('image_oeuvre', models.CharField(max_length=250)),
                ('idLieu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.lieu')),
            ],
        ),
        migrations.CreateModel(
            name='LnkLieuHoraire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateDebut', models.DateField(null=True)),
                ('dateFin', models.DateField(null=True)),
                ('idHoraire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.horaire')),
                ('idLieu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.lieu')),
            ],
        ),
        migrations.AddField(
            model_name='lieu',
            name='idTarif',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.tarif'),
        ),
        migrations.AddField(
            model_name='lieu',
            name='idTypeLieu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.typelieu'),
        ),
        migrations.AddField(
            model_name='lieu',
            name='idVille',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.ville'),
        ),
        migrations.CreateModel(
            name='FavorisParcours',
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
                ('nomEvenement', models.CharField(max_length=200, unique=True)),
                ('descriptionEvenement', models.CharField(max_length=200)),
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
