# Migration to fix database schema - delete and recreate tables with correct naming

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_telemetria', '0002_alter_veiculo_ano_alter_veiculo_horimetro'),
    ]

    operations = [
        # Delete existing models to clear the problematic schema
        migrations.DeleteModel(
            name='MedicaoVeiculo',
        ),
        migrations.DeleteModel(
            name='Medicao',
        ),
        migrations.DeleteModel(
            name='Veiculo',
        ),
        
        # Recreate Veiculo with correct field names
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Descricao', models.CharField(max_length=255)),
                ('Ano', models.IntegerField()),
                ('Horimetro', models.IntegerField()),
                ('Marca', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api_telemetria.marca')),
                ('Modelo', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api_telemetria.modelo')),
            ],
        ),
        
        # Recreate Medicao with correct field names
        migrations.CreateModel(
            name='Medicao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tipo', models.CharField(max_length=30)),
                ('UnidadeMedida', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api_telemetria.unidademedida')),
            ],
        ),
        
        # Recreate MedicaoVeiculo with correct field names
        migrations.CreateModel(
            name='MedicaoVeiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Data', models.DateTimeField()),
                ('Valor', models.FloatField()),
                ('Medicao', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api_telemetria.medicao')),
                ('Veiculo', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api_telemetria.veiculo')),
            ],
        ),
    ]
