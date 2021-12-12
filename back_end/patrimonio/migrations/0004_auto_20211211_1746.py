# Generated by Django 3.2.7 on 2021-12-11 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patrimonio', '0003_estadobem_situacoesusobem_alter_bens_valor_aquisicao_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='itensnotafiscal',
            name='produto_servico',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='estadobem',
            name='estado_bem',
            field=models.CharField(choices=[('Bom', 'Bom'), ('Regular', 'Regular'), ('AntiEconomico', 'AntiEconomico'), ('Precario', 'Precario'), ('Insersivel', 'Insersivel')], max_length=80),
        ),
        migrations.AlterField(
            model_name='situacoesusobem',
            name='situacao_uso_bem',
            field=models.CharField(choices=[('Em usos', 'Em usos'), ('Em cautela', 'Em cautela'), ('Em manutencao', 'Em manutencao'), ('Em disponibilidade', 'Em disponibilidade'), ('Aguardando recolhimento', 'Aguardando recolhimento'), ('Recolhido', 'Recolhido')], max_length=80),
        ),
    ]