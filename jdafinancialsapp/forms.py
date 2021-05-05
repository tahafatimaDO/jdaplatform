from django import forms
from .models import CompanyModel, SectorModel, ShareholderModel, FinancialStatementModel,  \
    FinancialStatementBalLinkModel, FinancialStatementIncLinkModel, FinancialStatementFactModel, FinancialStatementInvAcctLinkModel,Language

from django.utils.translation import ugettext_lazy
#ugettext_lazy('Sector') # this string will be marked for translation
#from django.core.exceptions import ValidationError

#def validate_id_exists(value):
#    company = CompanyModel.objects.filter(id=value)
#    if not company: # check if any object exists
#        raise ValidationError(f'{company} already exist in this {rpt_period}.')

#/////////////////////////// SectorForm //////////////////////////
class SectorForm(forms.ModelForm):
    sector = forms.CharField(max_length=50, label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Sector...'},))

    class Meta:
        model = SectorModel
        fields = ['sector']




#/////////////////////////// CompanyForm //////////////////////////
class CompanyForm(forms.ModelForm):
    CHOICES = (
        ('','Reporting Period'),
        ('Quarterly', 'Quarterly'),
        ('Semi-annually', 'Semi-Annually'),
        ('Annually', 'Annually'),
    )


    corp_name = forms.CharField(max_length=50, label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Denomination Sociale'},))
    company = forms.CharField(max_length=50, label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Non Usuel'},))
    sector = forms.ModelChoiceField(queryset=SectorModel.objects.all(), empty_label='Type de Tier', label='', widget=forms.Select(attrs={'class': 'form-control selectpicker show-tick my_dropdown', 'data-live-search=': 'true'}))
    #rpt_period = forms.ChoiceField(choices=CHOICES, label='', widget=forms.Select(attrs={'class': 'form-control selector selectpicker show-tick', 'placeholder':'Reporting Period'}))
    legl_form = forms.CharField(max_length=50, label='', widget=forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'Forme Juridique'},))
    creatn_dt = forms.DateField(label='', widget=forms.DateInput(attrs={'class': 'form-control selectpicker', 'placeholder': 'Date de creation'}))
    rccm_nbr = forms.CharField(max_length=20, label='', widget=forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'Numero RCCM'}, ))
    id_cntry = forms.IntegerField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Pays du siege social'}, ))
    #flag_pub_ctrl = forms.BooleanField(label='Societe sous control public', required=False, widget=forms.widgets.CheckboxInput(attrs={'class': 'form-control-sm form-check-input checkbox-inline', 'id':'flag_pub_ctrl'})),
    flag_pub_ctrl = forms.BooleanField(initial=True, label='', widget=forms.CheckboxInput(attrs={'class':'form-check-input my_checkbox mt-4','type':'checkbox'}))#forms.BooleanField(label='Visible', required=True, widget=forms.widgets.CheckboxInput(attrs={'class': 'form-control-sm selectpicker'})),
    actvty_sctr =forms.CharField(max_length=30, label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Secteur d\'activite BRVM'}, ))
    actvty_code =forms.CharField(max_length=30, label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Code activites economiques (CIV)'}, ))
    intrnl_actvty_code =forms.CharField(max_length=30, label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Code activites Joseph & Daniel Adv.'}, ))
    othr_bus_sctr =forms.CharField(max_length=30, label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Autre secteur d\'activites'}, ))
    #shrhldr_name = forms.ModelChoiceField(queryset=ShareholderModel.objects.all(), empty_label='Nome de l\'actionnaire', label='', widget=forms.Select(attrs={'class': 'form-control selectpicker show-tick my_dropdown'}))
    shrhldr_name_1 = forms.CharField(max_length=30, label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom de l\'actionnaire'}, ))
    shrhldr_type_1 = forms.CharField(max_length=30, label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type d\'actionnaire'}, ))
    shrs_hld_1 = forms.CharField(max_length=30, label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Part detenue'}, ))
    shrhldr_name_2 = forms.CharField(required = False,max_length=30, label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom de l\'actionnaire'}, ))
    shrhldr_type_2 = forms.CharField(required = False,max_length=30, label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type d\'actionnaire'}, ))
    shrs_hld_2 = forms.CharField(required = False,max_length=30, label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Part detenue'}, ))
    shrhldr_name_3 = forms.CharField(required = False,max_length=30, label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom de l\'actionnaire'}, ))
    shrhldr_type_3 = forms.CharField(required = False,max_length=30, label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type d\'actionnaire'}, ))
    shrs_hld_3 = forms.CharField(required = False,max_length=30, label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Part detenue'}, ))
    shrhldr_name_4 = forms.CharField(required = False,max_length=30, label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom de l\'actionnaire'}, ))
    shrhldr_type_4 = forms.CharField(required = False,max_length=30, label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type d\'actionnaire'}, ))
    shrs_hld_4 = forms.CharField(required = False, max_length=30, label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Part detenue'}, ))


    class Meta:
        model = CompanyModel
        fields = '__all__'
        #fields = ['company', 'sector', 'rpt_period']

#///////////////////////////// ShareholderForm //////////////////////////////////////
class ShareholderForm(forms.ModelForm):
    shrhldr_name = forms.CharField(max_length=30, label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome de l\'actionnaire'}, ))
    #stmt_type = forms.ChoiceField(choices=TYPE_CHOICES, widget=forms.Select(attrs={'class': 'form-control-sm'}))
    #company = forms.ModelChoiceField(queryset=CompanyModel.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))#models.ForeignKey(Company, on_delete=models.CASCADE)
    #financial_statement_line = forms.ModelChoiceField(queryset=FinancialStatementLine.objects.all(), label='', widget=forms.Select(attrs={'class': 'form-control-sm'})) #models.ForeignKey(FinancialStatementLine, on_delete=models.CASCADE)
    #value = forms.DecimalField(max_digits=13, decimal_places=2, label='Value', widget=forms.TextInput(attrs={'onBlur':'calc();', 'class': 'form-control-sm', 'placeholder':'0.00'}))#models.DecimalField(max_digits=13, decimal_places=2)

    class Meta:
        model = CompanyModel
        fields = ['shrhldr_name']

#///////////////////////////// fin_stmt_dash_form //////////////////////////////////////

class FinStmtDashForm(forms.Form):

    PERIODS = (
        ('Q1', 'Quarter 1'),
        ('Q2', '1/2 Year'),
        ('Q3', 'Quarter 3'),
        ('Q4', 'Full Year'),
    )

    sector = forms.ModelChoiceField(queryset=SectorModel.objects.all(), empty_label=ugettext_lazy('Sector'), label='',
                                     widget=forms.Select(attrs={'class': 'form-control selectpicker show-tick',
                                                                'data-live-search=': 'true'}))

    company = forms.ModelChoiceField(queryset=CompanyModel.objects.all(), empty_label=ugettext_lazy('Company'), label='',
                                     widget=forms.Select(attrs={'class': 'form-control selectpicker show-tick',
                                                                'data-live-search=': 'true'}))

    statement = forms.ModelChoiceField(queryset=FinancialStatementModel.objects.all(), empty_label=ugettext_lazy('Statement'), label='',
                                     widget=forms.Select(attrs={'class': 'form-control selectpicker show-tick',
                                                                'data-live-search=': 'true'}))

    date = forms.DateField(label='', widget=forms.DateInput(attrs={'class': 'form-control selectpicker', 'placeholder':'Date'}))
    #date = forms.DateTimeField(input_formats=['%d/%m/%Y'], label='')

    """
    def clean(self):
        cleaned_data = super(FinStmtDashForm, self).clean()
        sector = cleaned_data.get('sector')
        company = cleaned_data.get('company')
        statement = cleaned_data.get('statement')
        date = cleaned_data.get('date')

        if not sector and not company and not statement and not date:
            raise forms.ValidationError('You have to write something!')
    """

#///////////////////////// BalanceSheetForm /////////////////////
class BalanceSheetForm(forms.ModelForm):
    brut_0 = forms.DecimalField(max_digits=19, decimal_places=2,  label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder':'0.00'}))
    brut_1 = forms.DecimalField(max_digits=19, decimal_places=2,  label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder':'0.00'}))
    brut_2 = forms.DecimalField(max_digits=19, decimal_places=2,  label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_3 = forms.DecimalField(max_digits=19, decimal_places=2,  label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_4 = forms.DecimalField(max_digits=19, decimal_places=2,  label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_5 = forms.DecimalField(max_digits=19, decimal_places=2,  label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_6 = forms.DecimalField(max_digits=19, decimal_places=2,  label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_7 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_8 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_9 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_10 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_11 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_12 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_13 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_14 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_15 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_16 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_17 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_18 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_19 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_20 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_21 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_22 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_23 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_24 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_25 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_26 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_27 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_28 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_29 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_30 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_31 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_32 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_33 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_34 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_35 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_36 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_37 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_38 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_39 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_40 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_41 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_42 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_43 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_44 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_45 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_46 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_47 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_48 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_49 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_50 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_51 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_52 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_53 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_54 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_55 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_56 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_57 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_58 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    #brut_59 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))

    amort_0 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder':'0.00'}))
    amort_1 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder':'0.00'}))
    amort_2 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    amort_3 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    amort_4 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur': 'calc();', 'class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    amort_5 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur': 'calc();', 'class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    amort_6 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur': 'calc();', 'class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    amort_7 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur': 'calc();', 'class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    amort_8 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur': 'calc();', 'class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    amort_9 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur': 'calc();', 'class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    amort_10 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur': 'calc();', 'class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    amort_11 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur': 'calc();', 'class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    amort_12 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur': 'calc();', 'class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    amort_13 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur': 'calc();', 'class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    amort_14 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur': 'calc();', 'class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    amort_15 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur': 'calc();', 'class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    amort_16 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur': 'calc();', 'class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    amort_17 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur': 'calc();', 'class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    amort_18 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur': 'calc();', 'class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    amort_19 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur': 'calc();', 'class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    amort_20 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur': 'calc();', 'class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    amort_21 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur': 'calc();', 'class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    amort_22 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur': 'calc();', 'class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    amort_23 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur': 'calc();', 'class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    amort_24 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur': 'calc();', 'class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    amort_25 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur': 'calc();', 'class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    amort_26 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur': 'calc();', 'class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    amort_27 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur': 'calc();', 'class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    amort_28 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur': 'calc();', 'class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    amort_29 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur': 'calc();', 'class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    amort_30 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur': 'calc();', 'class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    amort_31 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur': 'calc();', 'class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    amort_32 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur': 'calc();', 'class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    amort_33 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur': 'calc();', 'class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    amort_34 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur': 'calc();', 'class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    amort_35 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur': 'calc();', 'class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    amort_36 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur': 'calc();', 'class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    amort_37 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur': 'calc();', 'class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    amort_38 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur': 'calc();', 'class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    amort_39 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur': 'calc();', 'class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    amort_40 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur': 'calc();', 'class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    amort_41 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur': 'calc();', 'class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    amort_42 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur': 'calc();', 'class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    amort_43 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur': 'calc();', 'class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    amort_44 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur': 'calc();', 'class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    amort_45 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur': 'calc();', 'class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    amort_46 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur': 'calc();', 'class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    amort_47 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur': 'calc();', 'class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    amort_48 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur': 'calc();', 'class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    amort_49 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur': 'calc();', 'class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    amort_50 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur': 'calc();', 'class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    amort_51 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur': 'calc();', 'class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    amort_52 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur': 'calc();', 'class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    amort_53 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur': 'calc();', 'class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    amort_54 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur': 'calc();', 'class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    amort_55 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur': 'calc();', 'class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    amort_56 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur': 'calc();', 'class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    amort_57 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur': 'calc();', 'class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    amort_58 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur': 'calc();', 'class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    #amort_59 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur': 'calc();', 'class': 'form-control form-control-sm', 'placeholder': '0.00'}))

    net_0 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder':'0.00'}))
    net_1 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder':'0.00'}))
    net_2 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    net_3 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    net_4 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    net_5 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    net_6 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    net_7 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    net_8 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    net_9 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    net_10 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    net_11 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    net_12 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    net_13 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    net_14 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    net_15 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    net_16 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    net_17 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    net_18 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    net_19 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    net_20 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    net_21 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    net_22 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    net_23 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    net_24 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    net_25 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    net_26 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    net_27 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    net_28 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    net_29 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    net_30 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    net_31 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    net_32 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    net_33 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    net_34 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    net_35 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    net_36 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    net_37 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    net_38 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    net_39 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    net_40 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    net_41 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    net_42 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    net_43 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    net_44 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    net_45 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    net_46 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    net_47 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    net_48 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    net_49 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    net_50 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    net_51 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    net_52 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    net_53 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    net_54 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    net_55 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    net_56 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    net_57 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    net_58 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    #net_59 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))

    class Meta:
        model = FinancialStatementBalLinkModel
        fields = ['brut_0','brut_1','brut_2','brut_3','brut_4','brut_5','brut_6','brut_7','brut_8','brut_9','brut_10','brut_11',
                  'brut_12','brut_13','brut_14','brut_15','brut_16','brut_17','brut_18','brut_19','brut_20','brut_21',
                  'brut_22','brut_23','brut_24','brut_25','brut_26','brut_27','brut_28','brut_29','brut_30','brut_31',
                  'brut_32','brut_33','brut_34','brut_35','brut_36','brut_37','brut_38','brut_39','brut_40','brut_41',
                  'brut_42','brut_43','brut_44','brut_45','brut_46','brut_47','brut_48','brut_49','brut_50','brut_51',
                  'brut_52','brut_53','brut_54','brut_55','brut_56','brut_57','brut_58',

                  'amort_0','amort_1','amort_2','amort_3','amort_4','amort_5','amort_6','amort_7','amort_8','amort_9','amort_10','amort_11',
                  'amort_12','amort_13','amort_14','amort_15','amort_16','amort_17','amort_18','amort_19','amort_20','amort_21',
                  'amort_22','amort_23','amort_24','amort_25','amort_26','amort_27','amort_28','amort_29','amort_30','amort_31',
                  'amort_32','amort_33','amort_34','amort_35','amort_36','amort_37','amort_38','amort_39','amort_40','amort_41',
                  'amort_42','amort_43','amort_44','amort_45','amort_46','amort_47','amort_48','amort_49','amort_50','amort_51',
                  'amort_52','amort_53','amort_54','amort_55','amort_56','amort_57','amort_58',

                  'net_0','net_1','net_2','net_3','net_4','net_5','net_6','net_7','net_8','net_9','net_10','net_11',
                  'net_12','net_13','net_14','net_15','net_16','net_17','net_18','net_19','net_20','net_21',
                  'net_22','net_23','net_24','net_25','net_26','net_27','net_28','net_29','net_30','net_31',
                  'net_32','net_33','net_34','net_35','net_36','net_37','net_38','net_39','net_40','net_41',
                  'net_42','net_43','net_44','net_45','net_46','net_47','net_48','net_49','net_50','net_51',
                  'net_52','net_53','net_54','net_55','net_56','net_57','net_58'
                 ]
        #fields = '__all__'

    def clean(self):
        cleaned_data = super(BalanceSheetForm, self).clean()
        #bal_type = cleaned_data.get('bal_type')
        #bal_company = cleaned_data.get('bal_company')
        #bal_date = cleaned_data.get('bal_date')

        #if not bal_type and not bal_company and not bal_date:
        #    raise forms.ValidationError('BalanceSheetForm: Missing values!')
    """
    def clean_bal_date(self):
        date = self.cleaned_data['bal_date']
        rpt_date = self.bal_company__rpt_period
        if (rpt_date == 'Quarterly'):
            print(f"70: rpt_date{rpt_date} date.month: {date.month}")
            if date.month in range(10, 13):  # Q4 range takes 1 month out
                lst_range = [10, 13]
                print(f"73: lst_range: {lst_range}")
            elif date.month in range(7, 10):
                print(f"75: rpt_date{rpt_date}")
                lst_range = [7, 10]
            elif date.month in range(4, 7):
                print(f"78: rpt_date{rpt_date}")
                lst_range = [4, 7]
            elif date.month in range(1, 4):
                print(f"81: rpt_date{rpt_date}")
                lst_range = [1, 4]
        elif (rpt_date == 'Semi-annually'):
            pass
        elif (rpt_date == 'Annually'):
            lst_range = [1, 13]
        else:
            print("88:////////////Ukn rpt_date")
        if rpt_date is None:
            raise forms.ValidationError("Item name is a required field", code="invalid", )
        #if len(name) < 1:
        #    raise forms.ValidationError("Item name is a required field", code="invalid", )

        return self.cleaned_data['bal_date']
    """
#///////////////////////// IncomeStatementForm /////////////////////
class IncomeStatementForm(forms.ModelForm):
    brut_0 = forms.DecimalField(max_digits=19, decimal_places=2,  label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder':'0.00'}))
    brut_1 = forms.DecimalField(max_digits=19, decimal_places=2,  label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder':'0.00'}))
    brut_2 = forms.DecimalField(max_digits=19, decimal_places=2,  label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_3 = forms.DecimalField(max_digits=19, decimal_places=2,  label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_4 = forms.DecimalField(max_digits=19, decimal_places=2,  label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_5 = forms.DecimalField(max_digits=19, decimal_places=2,  label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_6 = forms.DecimalField(max_digits=19, decimal_places=2,  label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_7 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_8 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_9 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_10 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_11 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_12 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_13 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_14 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_15 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_16 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_17 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_18 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_19 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_20 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_21 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_22 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_23 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_24 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_25 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_26 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_27 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_28 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_29 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_30 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_31 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_32 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_33 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_34 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_35 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_36 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_37 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_38 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_39 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_40 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_41 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_42 = forms.DecimalField(max_digits=19, decimal_places=2, label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))

    class Meta:
        model = FinancialStatementIncLinkModel
        #fields = ['brut_0','brut_1','brut_2','brut_3','brut_4']
        fields = ['brut_0','brut_1','brut_2','brut_3','brut_4','brut_5','brut_6','brut_7','brut_8','brut_9','brut_10','brut_11',
                  'brut_12','brut_13','brut_14','brut_15','brut_16','brut_17','brut_18','brut_19','brut_20','brut_21',
                  'brut_22','brut_23','brut_24','brut_25','brut_26','brut_27','brut_28','brut_29','brut_30','brut_31',
                  'brut_32','brut_33','brut_34','brut_35','brut_36','brut_37','brut_38','brut_39','brut_40','brut_41',
                  'brut_42'
                  ]



#///////////////////////// InvestmentAccountForm /////////////////////
class InvestmentAccountForm(forms.ModelForm):
    brut_0 = forms.DecimalField(max_digits=19, decimal_places=2,  label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder':'0.00'}))
    brut_1 = forms.DecimalField(max_digits=19, decimal_places=2,  label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder':'0.00'}))
    brut_2 = forms.DecimalField(max_digits=19, decimal_places=2,  label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_3 = forms.DecimalField(max_digits=19, decimal_places=2,  label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_4 = forms.DecimalField(max_digits=19, decimal_places=2,  label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_5 = forms.DecimalField(max_digits=19, decimal_places=2,  label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    brut_6 = forms.DecimalField(max_digits=19, decimal_places=2,  label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))

    amort_0 = forms.DecimalField(max_digits=19, decimal_places=2,  label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder':'0.00'}))
    amort_1 = forms.DecimalField(max_digits=19, decimal_places=2,  label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder':'0.00'}))
    amort_2 = forms.DecimalField(max_digits=19, decimal_places=2,  label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    amort_3 = forms.DecimalField(max_digits=19, decimal_places=2,  label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    amort_4 = forms.DecimalField(max_digits=19, decimal_places=2,  label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    amort_5 = forms.DecimalField(max_digits=19, decimal_places=2,  label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))
    amort_6 = forms.DecimalField(max_digits=19, decimal_places=2,  label='', widget=forms.TextInput(attrs={'onBlur':'calc();','class': 'form-control form-control-sm', 'placeholder': '0.00'}))


    class Meta:
        model = FinancialStatementInvAcctLinkModel
        fields = ['brut_0','brut_1','brut_2','brut_3','brut_4','brut_5','brut_6','amort_0','amort_1','amort_2','amort_3','amort_4','amort_5','amort_6']
# #///////////////////////// BalanceSheetSearchForm /////////////////////
# class BalanceSheetSearchForm(forms.ModelForm):
#     TYPE_CHOICES = (
#         ('', 'Type'),
#         ('Active', 'Active'),
#         ('Passive', 'Passive'),
#     )
#     bal_type = forms.ChoiceField(choices=TYPE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
#     bal_company = forms.ModelChoiceField(queryset=CompanyModel.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
#     bal_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}))
#
#     class Meta:
#         model = BalanceSheetModel
#         fields =  ['bal_type', 'bal_company', 'bal_date']
#
#     """
#     def clean_name(self):
#         name = self.cleaned_data['name']
#         if name is None:
#             raise forms.ValidationError("Item name is a required field", code="invalid", )
#         if len(name) < 1:
#             raise forms.ValidationError("Item name is a required field", code="invalid", )
#
#         return self.cleaned_data['name']
#     """
#///////////////////////// ContactForm test //////////////////
class ContactForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)
    message = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(),
        help_text='Write here your message!'
    )
    source = forms.CharField(       # A hidden input for internal use
        max_length=50,              # tell from which page the user sent the message
        widget=forms.HiddenInput()
    )

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        message = cleaned_data.get('message')
        if not name and not email and not message:
            raise forms.ValidationError('You have to write something!')


"""  Test """


class FinancialStatementFactForm(forms.ModelForm):
    #company = forms.ModelChoiceField(queryset=CompanyModel.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    #entry_date = forms.DateField()
    #financial_statement_line = forms.ModelChoiceField(queryset=FinancialStatementLineModel.objects.all(), label='',widget=forms.Select(attrs={'class': 'form-control-sm'}))
    #val_1= forms.DecimalField(initial=0.00, max_digits=18, decimal_places=2, label='val_1', widget=forms.TextInput(attrs={'onBlur':'calc();', 'class': 'form-control form-control-sm', 'placeholder':'0.00'}))#models.DecimalField(max_digits=13, decimal_places=2)
    #val_2= forms.DecimalField(initial=0.00, max_digits=18, decimal_places=2, label='val_2', widget=forms.TextInput(attrs={'onBlur':'calc();', 'class': 'form-control form-control-sm', 'placeholder':'0.00'}))#models.DecimalField(max_digits=13, decimal_places=2)

    #actif_brut= forms.DecimalField(initial=0.00, max_digits=18, decimal_places=2, label='actif_value_brut', widget=forms.TextInput(attrs={'onBlur':'calc();', 'class': 'form-control form-control-sm', 'placeholder':'0.00'}))
    #Immobilisations_incorporelles_brut= forms.DecimalField(initial=0.00, max_digits=18, decimal_places=2, label='Immobilisations_incorporelles_brut', widget=forms.TextInput(attrs={'onBlur':'calc();', 'class': 'form-control form-control-sm', 'placeholder':'0.00'}))


    #stmt_type = forms.ChoiceField(choices=TYPE_CHOICES, widget=forms.Select(attrs={'class': 'form-control-sm'}))
    #company = forms.ModelChoiceField(queryset=CompanyModel.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))#models.ForeignKey(Company, on_delete=models.CASCADE)
    #entry_date = forms.DateField()
    value_brut = forms.DecimalField(initial=0.00, max_digits=18, decimal_places=2, label='value_brut', widget=forms.TextInput(attrs={'onBlur':'calc();', 'class': 'form-control form-control-sm', 'placeholder':'0.00'}))
    #value_amort = forms.DecimalField(initial=0.00, max_digits=18, decimal_places=2, label='value_amort', widget=forms.TextInput(attrs={'onBlur':'calc();', 'class': 'form-control form-control-sm', 'placeholder':'0.00'}))
    #value_net = forms.DecimalField(initial=0.00, max_digits=18, decimal_places=2, label='value_net',widget=forms.TextInput(attrs={'onBlur': 'calc();', 'class': 'form-control form-control-sm','placeholder': '0.00'}))
    #value_net_prev_yr = forms.DecimalField(initial=0.00, max_digits=18, decimal_places=2, label='value_net_prev_yr',widget=forms.TextInput(attrs={'onBlur': 'calc();', 'class': 'form-control form-control-sm','placeholder': '0.00'}))

    class Meta:
        model = FinancialStatementFactModel
        fields = ['value_brut']#, 'value_amort', 'value_net', 'value_net_prev_yr']




class LanguageForm(forms.ModelForm):
    #name = forms.ModelChoiceField(queryset=Language.objects.all(), label='', widget=forms.TextInput(attrs={'class': 'form-control-sm', 'placeholder':'Language Name'}))
    name = forms.CharField(max_length=50, label='', widget=forms.TextInput(attrs={'class': 'form-control-sm', 'placeholder':'Language Name'}))
    #name = forms.CharField(max_length=50, label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sector...'}, ))
    class Meta:
        model = Language
        fields =  ['name']

# class FinancialStatementFact(models.Model):
#     company = models.ForeignKey(Company, on_delete=models.CASCADE)
#     financial_statement_line = models.ForeignKey(FinancialStatementLine, on_delete=models.CASCADE)
#     value = models.DecimalField(max_digits=13, decimal_places=2)
#
#     class Meta:
#         verbose_name_plural ='FinancialStatementFact'

