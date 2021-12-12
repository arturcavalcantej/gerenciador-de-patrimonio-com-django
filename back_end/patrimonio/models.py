from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import AutoField

class DadosCadModel(models.Model):
    id_user_cad = models.ForeignKey(
        User, on_delete=models.CASCADE,null=True,blank=True, related_name='%(class)s_user_cad')
    dt_cad = models.DateField(auto_now_add=True)
    id_user_alt = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True,blank=True, related_name='%(class)s_user_alt')
    dt_alt = models.DateField(null=True, blank=True, auto_now=True)

    class Meta:
        abstract = True

class Fornecedores(DadosCadModel):
    id_fornecedor = models.AutoField(primary_key=True)
    razao_social = models.CharField(null=False, max_length=60)
    cnpj = models.CharField(max_length=30, unique=True)
    email = models.CharField(max_length=60, unique=True)
    telefone = models.CharField(max_length=12, null=True, blank=True)
    class Meta:
        ordering = ['razao_social']
        db_table = "Fornecedores"
        verbose_name_plural = 'Fornecedores'

    def __str__(self) -> str:
        return self.razao_social 

class NaturezasDespesa(models.Model):
    id_natureza_despesa = models.AutoField(primary_key=True)
    cod_natureza_despesas = models.CharField(max_length=8)
    desc_natureza_despesa = models.CharField(max_length=60)
    
    class Meta:
        ordering = ['cod_natureza_despesas']
        db_table = "NaturezasDespesas"        
        verbose_name_plural = "Naturezas Despesas"

    def __str__(self) -> str:
        return self.desc_natureza_despesa

class Marcas(DadosCadModel):
    id_marca = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=80)

    class Meta:
        ordering = ['marca']
        db_table = "Marcas"        
        verbose_name_plural = "Marcas"
    
    def __str__(self) -> str:
        return self.marca

class Notas_fiscais(DadosCadModel):
    id_nota_fiscal = models.AutoField(primary_key=True)
    id_fornecedor = models.ForeignKey(Fornecedores, on_delete=models.CASCADE, related_name='Notas_fiscais')
    id_natureza_despesa = models.ForeignKey(NaturezasDespesa,on_delete=models.CASCADE, related_name='Notas_fiscais')
    numero = models.PositiveIntegerField()
    ano = models.IntegerField()
    class Meta:
        ordering = ['id_nota_fiscal']
        db_table = "NotasFiscais"
        verbose_name_plural = "Notas Fiscais"
    def __str__(self) -> str:
        return self.id_fornecedor.razao_social + "/" + str(self.numero)

class ItensNotaFiscal(DadosCadModel):
    id_item_nota_fiscal = models.AutoField(primary_key=True)
    id_nota_fiscal = models.ForeignKey(Notas_fiscais, on_delete=models.CASCADE, related_name='ItensNotaFiscal')
    qtd = models.IntegerField()
    produto_servico = models.CharField(max_length=100,null=True)
    valor_unitario = models.FloatField()
    vinculado = models.BooleanField(default=False)
    class Meta:
        ordering = ['id_item_nota_fiscal']
        db_table = "ItensNotaFiscal"        
        verbose_name_plural = "Itens Notas Fiscais"
    def __str__(self) -> str:
        return str(self.id_nota_fiscal) + "/" + self.produto_servico

estados = (('Bom','Bom'),
            ('Regular','Regular'),
            ('AntiEconomico',"AntiEconomico"),
            ('Precario','Precario'),
            ('Insersivel','Insersivel'))

class EstadoBem(models.Model):
    id_estado_bem = models.AutoField(primary_key=True)
    estado_bem = models.CharField(max_length=80, choices=estados)
    descricao = models.CharField(max_length=255)
    ativo = models.BooleanField(default=True)

    class Meta:
        ordering = ['estado_bem']
        db_table = "EstadoBem"
        verbose_name_plural = "Estado bem"
    def __str__(self) -> str:
        return self.estado_bem

situacao = (('Em uso','Em uso'),
            ('Em cautela','Em cautela'),
            ('Em manutencao',"Em manutencao"),
            ('Em disponibilidade','Em disponibilidade'),
            ('Aguardando recolhimento','Aguardando recolhimento'),
            ('Recolhido','Recolhido'))

class SituacoesUsoBem(models.Model):
    id_situacao_uso_bem = models.AutoField(primary_key=True)
    situacao_uso_bem = models.CharField(max_length=80,choices=situacao)
    descricao = models.CharField(max_length=255)
    ativo = models.BooleanField(default=True)

    class Meta:
        ordering = ['situacao_uso_bem']
        db_table = "SituacoesUsoBem"
        verbose_name_plural = "Situacoes uso bem"
    def __str__(self) -> str:
        return self.situacao_uso_bem

class Bens(DadosCadModel):
    id_bem = models.AutoField(primary_key=True)
    id_nota_fiscal = models.ForeignKey(Notas_fiscais, on_delete=models.CASCADE, related_name='Bens')
    tombamento = models.CharField(max_length=10)
    id_estado_bem = models.ForeignKey(EstadoBem,on_delete=models.CASCADE, related_name='Bens')
    id_situacao_uso_bem = models.ForeignKey(SituacoesUsoBem,on_delete=models.CASCADE, related_name='Bens')
    valor_aquisicao = models.FloatField()
    id_marca = models.ForeignKey(Marcas,on_delete=models.CASCADE, related_name='Bens')
    dt_inicio_uso = models.DateField(null=True, blank=True)
    observacoes = models.TextField(max_length=255,null=True)
    dt_lim_garantia = models.DateField(null=True, blank=True)
    dt_fim_garantia = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['id_bem']
        db_table = "Bens"        
        verbose_name_plural = "Bens"
   
    def __str__(self) -> str:
        return self.tombamento 