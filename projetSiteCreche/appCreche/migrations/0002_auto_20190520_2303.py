# Generated by Django 2.2.1 on 2019-05-20 21:03

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appCreche', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enfant',
            name='arriveJeudi',
            field=models.CharField(choices=[('no', 'Ne Viens pas'), ('730', '7h30'), ('800', '8h00'), ('830', '8h30'), ('900', '9h00'), ('930', '9h30')], default='', max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='enfant',
            name='arriveLundi',
            field=models.CharField(choices=[('no', 'Ne Viens pas'), ('730', '7h30'), ('800', '8h00'), ('830', '8h30'), ('900', '9h00'), ('930', '9h30')], default='', max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='enfant',
            name='arriveMardi',
            field=models.CharField(choices=[('no', 'Ne Viens pas'), ('730', '7h30'), ('800', '8h00'), ('830', '8h30'), ('900', '9h00'), ('930', '9h30')], default='', max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='enfant',
            name='arriveMercredi',
            field=models.CharField(choices=[('no', 'Ne Viens pas'), ('730', '7h30'), ('800', '8h00'), ('830', '8h30'), ('900', '9h00'), ('930', '9h30')], default='', max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='enfant',
            name='arriveVendredi',
            field=models.CharField(choices=[('no', 'Ne Viens pas'), ('730', '7h30'), ('800', '8h00'), ('830', '8h30'), ('900', '9h00'), ('930', '9h30')], default='', max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='enfant',
            name='dateDeNaissance',
            field=models.DateField(null=True, verbose_name='Date de Naissance'),
        ),
        migrations.AlterField(
            model_name='enfant',
            name='nom',
            field=models.CharField(max_length=20, null=True, verbose_name='nom'),
        ),
        migrations.AlterField(
            model_name='enfant',
            name='partJeudi',
            field=models.CharField(choices=[('no', 'Ne viens pas'), ('1630', '16h30'), ('1700', '17h00'), ('1730', '17h30'), ('1800', '18h00'), ('1830', '18h30')], default='', max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='enfant',
            name='partLundi',
            field=models.CharField(choices=[('no', 'Ne viens pas'), ('1630', '16h30'), ('1700', '17h00'), ('1730', '17h30'), ('1800', '18h00'), ('1830', '18h30')], default='', max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='enfant',
            name='partMardi',
            field=models.CharField(choices=[('no', 'Ne viens pas'), ('1630', '16h30'), ('1700', '17h00'), ('1730', '17h30'), ('1800', '18h00'), ('1830', '18h30')], default='', max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='enfant',
            name='partMercredi',
            field=models.CharField(choices=[('no', 'Ne viens pas'), ('1630', '16h30'), ('1700', '17h00'), ('1730', '17h30'), ('1800', '18h00'), ('1830', '18h30')], default='', max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='enfant',
            name='partVendredi',
            field=models.CharField(choices=[('no', 'Ne viens pas'), ('1630', '16h30'), ('1700', '17h00'), ('1730', '17h30'), ('1800', '18h00'), ('1830', '18h30')], default='', max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='enfant',
            name='prenom',
            field=models.CharField(max_length=20, null=True, verbose_name='prenom'),
        ),
        migrations.AlterField(
            model_name='parent',
            name='adresse',
            field=models.CharField(max_length=256, null=True, verbose_name='Adresse'),
        ),
        migrations.AlterField(
            model_name='parent',
            name='adresseMail_Mere',
            field=models.EmailField(max_length=254, null=True, verbose_name='Email de la Mère'),
        ),
        migrations.AlterField(
            model_name='parent',
            name='adresseMail_Pere',
            field=models.EmailField(max_length=254, null=True, verbose_name='Email du Père'),
        ),
        migrations.AlterField(
            model_name='parent',
            name='nbEnfantAuFoyer',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(20)], verbose_name="Nombre d'enfant au foyer"),
        ),
        migrations.AlterField(
            model_name='parent',
            name='nom_Mere',
            field=models.CharField(max_length=20, null=True, verbose_name='Nom de la Mère'),
        ),
        migrations.AlterField(
            model_name='parent',
            name='nom_Pere',
            field=models.CharField(max_length=20, null=True, verbose_name='Nom du Père'),
        ),
        migrations.AlterField(
            model_name='parent',
            name='num_Mere',
            field=models.DecimalField(decimal_places=0, max_digits=10, null=True, verbose_name='télephone de la Mère'),
        ),
        migrations.AlterField(
            model_name='parent',
            name='num_Pere',
            field=models.DecimalField(decimal_places=0, max_digits=10, null=True, verbose_name='télephone du Père'),
        ),
        migrations.AlterField(
            model_name='parent',
            name='parentUser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='parent',
            name='prenom_Mere',
            field=models.CharField(max_length=20, null=True, verbose_name='Prénom de la Mère'),
        ),
        migrations.AlterField(
            model_name='parent',
            name='prenom_Pere',
            field=models.CharField(max_length=20, null=True, verbose_name='Prénom du Père'),
        ),
        migrations.AlterField(
            model_name='parent',
            name='profession_Mere',
            field=models.CharField(max_length=64, null=True, verbose_name='Profession de la Mère'),
        ),
        migrations.AlterField(
            model_name='parent',
            name='profession_Pere',
            field=models.CharField(max_length=64, null=True, verbose_name='Profession du Père'),
        ),
        migrations.AlterField(
            model_name='parent',
            name='telEmployeur_Mere',
            field=models.DecimalField(decimal_places=0, max_digits=10, null=True, verbose_name="telephone de l'employeur de la Mère"),
        ),
        migrations.AlterField(
            model_name='parent',
            name='telEmployeur_Pere',
            field=models.DecimalField(decimal_places=0, max_digits=10, null=True, verbose_name="telephone de l'employeur du Père"),
        ),
    ]
